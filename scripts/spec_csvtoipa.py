import pandas
import eng_to_ipa as ipa
df_requred_column = pandas.read_csv('source.csv')
text_trans = []
text_trans_A = []
text_trans_B = []
for row in df_requred_column.itertuples(): 
  text_trans.append(ipa.convert(row[1]))
  text_trans_A.append(ipa.convert(row[2]))
  text_trans_B.append(ipa.convert(row[3]))
df_requred_column['C'] = text_trans
df_requred_column['D'] = text_trans_A
df_requred_column['E'] = text_trans_B
print(df_requred_column)
df_requred_column.to_csv('output.csv')