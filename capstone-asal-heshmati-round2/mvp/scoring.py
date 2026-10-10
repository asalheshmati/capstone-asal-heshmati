"""Pure arithmetic only. No inference and no invented evidence."""
WEIGHTS={'essential':40,'experience':25,'skills':20,'preferred':10,'portfolio':5}
CREDIT={'direct':1.0,'partial':.5,'not_documented':0.0,'contradicted':0.0}
def calculate(requirements):
    groups={c:[] for c in WEIGHTS};seen=set()
    for item in requirements:
        if item['id'] in seen:raise ValueError('Duplicate requirement ID')
        seen.add(item['id'])
        if item['category'] not in groups or item['status'] not in CREDIT:raise ValueError('Invalid category/status')
        groups[item['category']].append(item)
    denominator=sum(WEIGHTS[c] for c,x in groups.items() if x)
    breakdown=[];weighted=0
    for c,items in groups.items():
        component=sum(CREDIT[x['status']] for x in items)/len(items) if items else None
        if component is not None:weighted+=WEIGHTS[c]*component
        breakdown.append({'category':c,'original_weight':WEIGHTS[c],'effective_weight':round(100*WEIGHTS[c]/denominator,6) if items and denominator else 0,'component':component,'contribution':round(100*WEIGHTS[c]*component/denominator,6) if component is not None and denominator else 0,'applicable':bool(items)})
    score=int(100*weighted/denominator+0.5) if denominator else None
    known=sum(x['status']!='not_documented' for x in requirements)
    coverage=known/len(requirements) if requirements else 0
    band='insufficient information' if not denominator or coverage<.5 else 'strong documented alignment' if score>=80 else 'moderate documented alignment' if score>=50 else 'limited documented alignment'
    return {'overall_score':score,'alignment_band':band,'evidence_coverage':round(coverage,6),'category_breakdown':breakdown,'scoring_version':'v1'}
