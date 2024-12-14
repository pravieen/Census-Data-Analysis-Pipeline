import pandas as pd

input_file_path = "/Users/a.s.pravieen/Downloads/updated_census_data.csv"
output_file_path = "/Users/a.s.pravieen/Desktop/DE Project/t3/updated_census_data.csv"

rename_state = ['Adilabad', 'Nizamabad', 'Karimnagar', 'Medak', 'Hyderabad', 'Rangareddy', 'Mahbubnagar', 'Nalgonda', 'Warangal', 'Khammam']
ladakh_rename_state = ['Leh', 'Kargil']

df = pd.read_csv(input_file_path)

df.loc[df['District'].isin (rename_state) ,'State/UT' ] = 'Telangana'
df.loc[df['District'].isin (ladakh_rename_state), 'State/UT'] = 'Ladakh'


df.to_csv(output_file_path)


