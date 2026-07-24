from config import OUTPUT_DIR


class ExcelWriter:

    def write_master(self, df):

        file = OUTPUT_DIR / "입교자명단.xlsx"

        df.to_excel(
            file,
            index=False
        )

        print(file)