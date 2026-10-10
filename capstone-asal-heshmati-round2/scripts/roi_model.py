from pathlib import Path
import csv, math, json
ROOT=Path(__file__).resolve().parents[1]
UPFRONT=4000; FIXED=750; CHURN=.03; REFUND=.02; FEE_RATE=.03; FEE_FIXED=.30; API=.40; SUPPORT=1.00
def model(price, conversion, months, members=40000):
    initial=members*conversion
    rows=[]
    for month in range(1,months+1):
        active=initial*(1-CHURN)**(month-1)
        gross=active*price
        receipts=gross*(1-REFUND)
        fees=gross*FEE_RATE+active*FEE_FIXED
        api=active*API;support=active*SUPPORT
        total_cost=fees+api+support+FIXED+(UPFRONT if month==1 else 0)
        net=receipts-total_cost
        rows.append(dict(month=month,active=active,gross=gross,refunds=gross*REFUND,receipts=receipts,fees=fees,api=api,support=support,fixed=FIXED,upfront=UPFRONT if month==1 else 0,total_cost=total_cost,net_benefit=net))
    cost=sum(x['total_cost'] for x in rows); benefit=sum(x['net_benefit'] for x in rows)
    contribution=price*(1-REFUND-FEE_RATE)-FEE_FIXED-API-SUPPORT
    cumulative=0;payback=None
    for row in rows:
        cumulative+=row['net_benefit']
        if cumulative>=0 and payback is None: payback=row['month']
    return dict(price=price,conversion=conversion,members=members,initial_payers=initial,months=months,gross=sum(x['gross'] for x in rows),receipts=sum(x['receipts'] for x in rows),total_cost=cost,net_benefit=benefit,roi_percent=benefit/cost*100,contribution_per_payer=contribution,operating_break_even_payers=math.ceil(FIXED/contribution),payback_month=payback,rows=rows)
def write_csv(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def main():
    folder=ROOT/'business';folder.mkdir(exist_ok=True)
    results=[model(p,c,m) for p in [10,15,20] for c in [.01,.03,.05] for m in [12,36]]
    write_csv(folder/'roi_scenarios.csv',[{k:v for k,v in x.items() if k!='rows'} for x in results])
    base=model(15,.03,36);write_csv(folder/'base_monthly_cashflow.csv',base['rows'])
    (folder/'assumptions.json').write_text(json.dumps(dict(upfront=UPFRONT,fixed_monthly=FIXED,churn_monthly=CHURN,refund_rate=REFUND,payment_percent=FEE_RATE,payment_fixed=FEE_FIXED,api_per_payer_month=API,support_per_payer_month=SUPPORT,member_scenario=40000,acquisition='initial cohort only, no replacement',currency='USD'),indent=2))
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        import numpy as np
        plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
        charts=ROOT/'charts';charts.mkdir(exist_ok=True)
        def save(name):plt.tight_layout();plt.savefig(charts/name,dpi=170,bbox_inches='tight');plt.close()
        fig,ax=plt.subplots(figsize=(8,4.5)); vals=[[40000*c*p for p in [10,15,20]] for c in [.01,.03,.05]]
        im=ax.imshow(vals,cmap='YlGn');ax.set_xticks([0,1,2],['$10','$15','$20']);ax.set_yticks([0,1,2],['1%','3%','5%']);ax.set_xlabel('Monthly price');ax.set_ylabel('Initial conversion');ax.set_title('First-month gross revenue — assumed 40,000-user base')
        for i,row in enumerate(vals):
            for j,v in enumerate(row):ax.text(j,i,f'${v:,.0f}',ha='center',va='center',color='black')
        save('01_revenue_scenarios.png')
        fig,ax=plt.subplots(figsize=(8,4.5));ax.plot([x['month'] for x in base['rows']],[x['active'] for x in base['rows']],color='#527600',lw=3);ax.set_title('Payers decline with 3% monthly churn and no replacement');ax.set_xlabel('Month');ax.set_ylabel('Active payers');ax.set_ylim(bottom=0);save('02_churn_cohort.png')
        fig,ax=plt.subplots(figsize=(8,4.5));cum=0;v=[]
        for x in base['rows']:cum+=x['net_benefit'];v.append(cum)
        ax.plot(range(1,37),v,color='#527600',lw=3);ax.axhline(0,color='grey',lw=1);ax.set_title('Base scenario cumulative net benefit — USD');ax.set_xlabel('Month');ax.set_ylabel('Cumulative net benefit');save('03_cumulative_net_benefit.png')
        fig,ax=plt.subplots(figsize=(8,4.5));ps=[10,15,20];bs=[model(p,.03,12)['operating_break_even_payers'] for p in ps];ax.bar([f'${p}' for p in ps],bs,color='#82a800');ax.set_title('Operating break-even depends on monthly price');ax.set_xlabel('Price per month');ax.set_ylabel('Active payers required')
        for i,v in enumerate(bs):ax.text(i,v+1,str(v),ha='center')
        save('04_operating_break_even.png')
        fig,ax=plt.subplots(figsize=(8,4.5));x=base['rows'][0];cats=['Hosting','Storage','Maintenance','Evaluation','API','Support','Payment fees'];vs=[150,20,500,80,x['api'],x['support'],x['fees']];ax.barh(cats,vs,color='#82a800');ax.set_title('First-month operating cost — base scenario, USD');ax.set_xlabel('Monthly cost');save('05_operating_cost.png')
    except ImportError:
        print('CSV model saved. Install matplotlib to regenerate charts.')
    print(json.dumps({k:v for k,v in model(15,.03,12).items() if k!='rows'},indent=2))
if __name__=='__main__':main()
