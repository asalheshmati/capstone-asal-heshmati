"""Calls the actual protected CTO app. Never substitutes a toy inference chain."""
import os,json,urllib.request,datetime,sys,urllib.parse
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from evaluation.evaluators import structural_evaluator,evidence_evaluator,arithmetic_evaluator,hard_evaluator
def main():
    from langsmith import Client,traceable
    for key in ['LANGSMITH_API_KEY','MVP_EVAL_URL','MVP_EVAL_TOKEN']:
        if not os.getenv(key):raise SystemExit(f'Missing backend/private environment variable: {key}')
    endpoint=os.environ['MVP_EVAL_URL'];scheme=urllib.parse.urlparse(endpoint).scheme
    if scheme!='https':raise SystemExit('MVP_EVAL_URL must use HTTPS for the protected hosted app')
    client=Client()
    cases=json.loads((Path(__file__).parent/'synthetic_cases.json').read_text())
    stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    dataset=client.create_dataset(dataset_name='TechTalk-synthetic-'+stamp,description='Seven synthetic cases, actual CTO application target, scoring v1')
    client.create_examples(dataset_id=dataset.id,examples=[{'inputs':x['inputs'],'outputs':x['reference_outputs'],'metadata':{'case_id':x['case_id']}} for x in cases])
    @traceable(name='actual_cto_app_pipeline')
    def target(inputs):
        req=urllib.request.Request(endpoint,data=json.dumps(inputs).encode(),headers={'Authorization':'Bearer '+os.environ['MVP_EVAL_TOKEN'],'Content-Type':'application/json'},method='POST')
        with urllib.request.urlopen(req,timeout=180) as res:
            return json.loads(res.read())
    results=client.evaluate(target,data=dataset.id,evaluators=[structural_evaluator,evidence_evaluator,arithmetic_evaluator,hard_evaluator],experiment_prefix='techtalk-actual-app',max_concurrency=1,metadata={'scoring_version':'v1','note':'Manually review semantic factuality. Record app/model/prompt/commit before final submission.'})
    print('Dataset:',dataset.name)
    print('Experiment complete. Open LangSmith for results, traces and export. Fill the manual review sheet before declaring factual fidelity.')
    for row in results:
        print(json.dumps({'feedback':str(row.get('evaluation_results',{}))}))
if __name__=='__main__':main()
