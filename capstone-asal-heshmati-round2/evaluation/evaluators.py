"""Necessary structural checks. Semantic factuality requires manual review."""
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mvp.scoring import calculate
def norm(value):return ' '.join(str(value).split()).casefold()
def structural(outputs):
    return isinstance(outputs,dict) and len(outputs.get('reports',[]))==2 and set(outputs.get('cvs',{}))=={'master','tailored_a','tailored_b'} and all(outputs['cvs'][k].get('plain_text','').strip() for k in outputs['cvs'])
def evidence_check(inputs,outputs):
    evidence=outputs.get('evidence',[]); ids={x['id']:x for x in evidence}
    sources=norm(inputs['cv_text']+'\n'+'\n'.join(inputs.get('candidate_answers',[])))
    if len(ids)!=len(evidence):return False
    for e in evidence:
        if not norm(e.get('source_quote','')) or norm(e['source_quote']) not in sources:return False
    for i,report in enumerate(outputs.get('reports',[])):
        jd=norm(inputs['jd_texts'][i])
        for req in report.get('requirement_assessments',[]):
            if not norm(req.get('jd_quote','')) or norm(req['jd_quote']) not in jd:return False
            if any(eid not in ids for eid in req.get('evidence_ids',[])):return False
            if req['status'] in ['direct','partial','contradicted'] and not req.get('evidence_ids'):return False
    return True
def arithmetic_check(outputs):
    for report in outputs.get('reports',[]):
        expected=calculate(report['requirement_assessments'])
        if report.get('overall_score')!=expected['overall_score'] or report.get('alignment_band')!=expected['alignment_band']:return False
        if report.get('category_breakdown')!=expected['category_breakdown']:return False
    return bool(outputs.get('reports'))
def hard_check(outputs,reference):
    for expected in reference.get('expected_hard_conditions',[]):
        actual=outputs['reports'][expected['job_index']].get('hard_requirements',[])
        if not any(norm(expected['contains']) in norm(x['requirement']) and x['status']==expected['status'] for x in actual):return False
    return True
def structural_evaluator(inputs,outputs,reference_outputs):return {'key':'five_outputs','score':int(structural(outputs))}
def evidence_evaluator(inputs,outputs,reference_outputs):
    try:ok=evidence_check(inputs,outputs)
    except (KeyError,TypeError,IndexError):ok=False
    return {'key':'source_provenance','score':int(ok)}
def arithmetic_evaluator(inputs,outputs,reference_outputs):
    try:ok=arithmetic_check(outputs)
    except (KeyError,TypeError,ValueError):ok=False
    return {'key':'score_reproduction','score':int(ok)}
def hard_evaluator(inputs,outputs,reference_outputs):
    try:ok=hard_check(outputs,reference_outputs)
    except (KeyError,TypeError,IndexError):ok=False
    return {'key':'mandatory_condition_status','score':int(ok)}
