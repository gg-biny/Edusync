from config import INPUT_FILE

from loaders.html_loader import HtmlLoader
from core.sorter import StudentSorter


loader = HtmlLoader()

df = loader.load(INPUT_FILE)

print(df.head())

print()

print(df.columns)

print()

sorted_df = StudentSorter.sort(df)

print(sorted_df.head())