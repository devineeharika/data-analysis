import pandas as pd
sheets=pd.read_excel('stock portfolio\\sda_data.xlsx',sheet_name=['4th period','3rd period','2nd period','1st period','all period'])
df=pd.concat(sheets[frame] for frame in sheets.keys())
print("hii")

