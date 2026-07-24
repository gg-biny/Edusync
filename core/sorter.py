from core.columns import Columns


class StudentSorter:

    @staticmethod
    def sort(df):

        temp = df.copy()

        # 법인 먼저
        temp["_priority"] = temp[Columns.TYPE].map(
            {
                "법인": 0,
                "개인": 1
            }
        )

        temp = temp.sort_values(
            by=[
                "_priority",
                Columns.NAME
            ],
            ascending=True
        )

        temp = temp.drop(
            columns="_priority"
        )

        temp = temp.reset_index(
            drop=True
        )

        return temp