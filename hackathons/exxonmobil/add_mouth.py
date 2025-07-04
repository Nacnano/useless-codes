import pandas as pd

df = pd.read_csv('merged_column.csv')

df['DATE'] = pd.to_datetime(df['DATE'])

df['MONTH_NAME'] = df['DATE'].dt.strftime('%B')

df.to_csv('merged_column_with_month_name.csv', index=False)

