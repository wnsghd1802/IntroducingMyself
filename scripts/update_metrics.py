#!/usr/bin/env python3
"""Recompute public ritual metrics from a user's redacted CSV without uploading raw data.
Usage: python scripts/update_metrics.py --input path/to/private-redacted.csv --out data/new-metrics.json
CSV header: date,assessment    assessment ∈ full,partial,not_done
Do not commit private CSV files. This only emits a candidate JSON, not a live site update.
"""
import argparse,csv,datetime as dt,json,hashlib,pathlib
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--out',default='data/new-metrics.json');args=p.parse_args()
rows={}
with open(args.input,newline='',encoding='utf-8-sig') as f:
    for row in csv.DictReader(f):
        day=dt.date.fromisoformat(row['date']); v=row['assessment'].strip()
        if v not in ('full','partial','not_done'): raise ValueError(f'invalid assessment {v!r} at {day}')
        if day in rows: raise ValueError(f'duplicate date {day}')
        rows[day]=v
if not rows: raise ValueError('no records')
count={k:sum(x==k for x in rows.values()) for k in ('full','partial','not_done')}
out={'source_period':{'from':str(min(rows)),'to':str(max(rows))},'days_with_entries':len(rows),'weeks_with_entries_iso':len({x.isocalendar()[:2] for x in rows}),'self_assessment':count,'note':'13주 과정의 출석/제출 통계가 아닌 입력 CSV의 자기평가 집계'}
s=json.dumps(out,ensure_ascii=False,sort_keys=True,indent=2)+'\n'
f=pathlib.Path(args.out);f.parent.mkdir(parents=True,exist_ok=True);f.write_text(s,encoding='utf-8');print(f'{f} SHA256 {hashlib.sha256(s.encode()).hexdigest()}')