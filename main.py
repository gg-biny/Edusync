from loaders.data_loader import DataLoader
from generators.master_generator import MasterGenerator
from writers.excel_writer import ExcelWriter


def main():

    loader = DataLoader()

    raw_df = loader.load()

    generator = MasterGenerator()

    master_df, total = generator.generate(raw_df)

    writer = ExcelWriter()

    writer.write_master(master_df)

    print()

    print(f"총 인원 : {total}명")


if __name__ == "__main__":
    main()
    
'''
import pandas as pd

filename = "교육신청리스트_2026-07-16.xls"

with open(filename, "r", encoding="utf-8") as f:
    html = f.read()

tables = pd.read_html(html)

df = tables[0]

print(df.head())
'''