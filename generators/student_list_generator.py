#기준 데이터 생성

from utils.sorter import StudentSorter


class MasterGenerator:

    def generate(self, raw_df):

        master_df = raw_df.copy()

        master_df = StudentSorter.sort(master_df)

        total = len(master_df)

        return master_df, total