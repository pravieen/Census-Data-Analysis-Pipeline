import pandas as pd

input_file = "/Users/a.s.pravieen/Desktop/DE Project/t3/updated_census_data.csv"
output_file = "/Users/a.s.pravieen/Desktop/DE Project/t4/updated_census_data.csv"
missing_percentage_data_output_file = "/Users/a.s.pravieen/Desktop/DE Project/t4/updated_missing_percentage_data.csv"

df = pd.read_csv(input_file)

df = df.drop(['Unnamed: 0.1', 'Unnamed: 0', 'Unnamed: 0.2'],axis=1)

df.loc[df['Population'].isna(),'Population'] = df['Male'] + df['Female'] 
df.loc[df['Male'].isna(),'Male'] = df['Population'] -df['Female']
df.loc[df['Female'].isna(),'Female'] = df['Population'] - df['Male']

df.loc[df['Literate'].isna(),'Literate'] = df['Literate_Male'] + df['Literate_Female']
df.loc[df['Literate_Male'].isna(),'Literate_Male'] = df['Literate'] - df['Literate_Female'] 
df.loc[df['Literate_Female'].isna(),'Literate_Female'] = df['Literate'] - df['Literate_Male'] 

df.loc[df['SC'].isna(),'SC'] = df['Male_SC'] + df['Female_SC']
df.loc[df['Male_SC'].isna(),'Male_SC'] = df['SC'] - df['Female_SC'] 
df.loc[df['Female_SC'].isna(),'Female_SC'] = df['SC'] - df['Male_SC'] 

df.loc[df['ST'].isna(),'ST'] = df['Male_ST'] + df['Female_ST']
df.loc[df['Male_ST'].isna(),'Male_ST'] = df['ST'] - df['Female_ST'] 
df.loc[df['Female_ST'].isna(),'Female_ST'] = df['ST'] - df['Male_ST'] 

df.loc[df['Workers'].isna(),'Workers'] = df['Male_Workers'] + df['Female_Workers']
df.loc[df['Male_Workers'].isna(),'Male_Workers'] = df['Workers'] - df['Female_Workers'] 
df.loc[df['Female_Workers'].isna(),'Female_Workers'] = df['Workers'] - df['Male_Workers'] 

df.loc[df['Households'].isna(),'Households'] = df['Urban_Households'] + df['Households_Rural']
df.loc[df['Urban_Households'].isna(),'Urban_Households'] = df['Households'] - df['Households_Rural'] 
df.loc[df['Households_Rural'].isna(),'Households_Rural'] = df['Households'] - df['Urban_Households'] 

df.loc[df['Total_Education'].isna(),'Total_Education'] = df['Literate_Education'] + df['Illiterate_Education']
df.loc[df['Literate_Education'].isna(),'Literate_Education'] = df['Total_Education'] - df['Illiterate_Education'] 
df.loc[df['Illiterate_Education'].isna(),'Illiterate_Education'] = df['Total_Education'] - df['Literate_Education'] 

df['Total_Relegion'] = df[['Hindus','Muslims','Christians','Sikhs','Jains','Buddhists','Others_Religions','Religion_Not_Stated']].sum(axis=1)
df.loc[df['Total_Relegion'].isna(),'Total_Relegion'] = df['Population']
for relegion in ['Hindus','Muslims','Christians','Sikhs','Jains','Buddhists','Others_Religions','Religion_Not_Stated'] :
    df.loc[df[relegion].isna(),relegion] = df[[col for col in ['Hindus','Muslims','Christians','Sikhs','Jains','Buddhists','Others_Religions','Religion_Not_Stated'] if col!=relegion]].sum(axis=1)

df.loc[df['Housholds_with_Electric_Lighting'].isna(), 'Housholds_with_Electric_Lighting'] = df['Households'] * 0.8  # Assuming 80% have electric lighting
df.loc[df['Households_with_Internet'].isna(), 'Households_with_Internet'] = df['Households'] * 0.4

for col in df.columns:
    if df[col].isna().sum() > 0:
        df[col].fillna(df[col].mean(),inplace=True)


missing_percentage_per_col =( df.isnull().sum() / len(df)) * 100

missing_percentage_data = pd.DataFrame(missing_percentage_per_col)
missing_percentage_data.to_csv(missing_percentage_data_output_file)
df.to_csv(output_file,index=False)
