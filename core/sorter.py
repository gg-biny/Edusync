from core.columns import TYPE, NAME


class StudentSorter:

    @staticmethod
    def sort(df):

        temp = df.copy()

        temp["_sort"] = temp[TYPE].map({
            "법인": 0,
            "개인": 1
        })

        temp = temp.sort_values(
            by=["_sort", NAME]
        )

        temp = temp.drop(columns="_sort")

        return temp