import pandas as pd

filename = "교육신청리스트_2026-07-16.xls"

with open(filename, "r", encoding="utf-8") as f:
    html = f.read()

tables = pd.read_html(html)

df = tables[0]

print(df.head())