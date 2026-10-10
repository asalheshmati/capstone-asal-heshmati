import unittest,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from mvp.scoring import calculate
from evaluation.evaluators import evidence_check,arithmetic_check,hard_check
def req(id,category,status):return {'id':id,'category':category,'status':status}
class Checks(unittest.TestCase):
    def test_exact_weighting(self):
        r=calculate([req('1','essential','direct'),req('2','experience','partial'),req('3','skills','direct'),req('4','preferred','not_documented'),req('5','portfolio','contradicted')])
        self.assertEqual(r['overall_score'],73)
    def test_no_requested_portfolio_is_na(self):
        r=calculate([req('1','essential','direct'),req('2','experience','direct'),req('3','skills','direct')]);self.assertEqual(r['overall_score'],100);self.assertFalse(r['category_breakdown'][4]['applicable'])
    def test_unknown_is_insufficient(self):
        r=calculate([req('1','essential','direct'),req('2','experience','not_documented'),req('3','skills','not_documented')]);self.assertEqual(r['alignment_band'],'insufficient information')
    def test_known_negative_is_not_unknown(self):
        self.assertEqual(calculate([req('1','essential','contradicted')])['alignment_band'],'limited documented alignment')
    def test_no_requirements(self):self.assertIsNone(calculate([])['overall_score'])
    def test_duplicates_fail(self):
        with self.assertRaises(ValueError):calculate([req('1','essential','direct'),req('1','skills','direct')])
    def test_quote_invention_fails(self):
        self.assertFalse(evidence_check({'cv_text':'Excel reporting','jd_texts':['Excel']},{'evidence':[{'id':'1','source_quote':'SQL expert'}],'reports':[]}))
    def test_unmet_hard_condition_is_checked(self):
        out={'reports':[{'hard_requirements':[{'requirement':'a current architect license','status':'unmet'}]}]}
        self.assertTrue(hard_check(out,{'expected_hard_conditions':[{'job_index':0,'contains':'architect license','status':'unmet'}]}))
        out['reports'][0]['hard_requirements'][0]['status']='met'
        self.assertFalse(hard_check(out,{'expected_hard_conditions':[{'job_index':0,'contains':'architect license','status':'unmet'}]}))
    def test_score_tampering_fails(self):
        rs=[req('1','essential','partial')];r={'requirement_assessments':rs,**calculate(rs)};r['overall_score']=100
        self.assertFalse(arithmetic_check({'reports':[r]}))
    def test_seven_complete_fixtures(self):
        cases=json.loads((Path(__file__).resolve().parents[1]/'evaluation/synthetic_cases.json').read_text());self.assertEqual(len(cases),7)
        for c in cases:
            self.assertEqual(len(c['inputs']['jd_texts']),2);self.assertTrue(c['reference_outputs']['expected_hard_conditions'])
if __name__=='__main__':unittest.main()
