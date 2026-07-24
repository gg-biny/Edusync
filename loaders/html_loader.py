import pandas as pd


class HtmlLoader:

    def load(self, path):

        tables = pd.read_html(
            path,
            encoding="utf-8"
        )

        if len(tables) == 0:
            raise Exception("표를 찾지 못했습니다.")

        df = tables[0]

        df = df.dropna(
            how="all"
        )

        df = df.reset_index(
            drop=True
        )

        return df