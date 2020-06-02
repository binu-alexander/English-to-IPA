import pandas
import eng_to_ipa as ipa
import csv

#using datafram
df = pandas.read_csv('source.csv')

for index, row in df.iterrows():
    df['IPA'] = ipa.convert(df['State'])

df.to_csv('output.csv')


#single variable
#var = ipa.convert(df['State'])

