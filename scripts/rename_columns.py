import pandas as pd
output_file_path = "/Users/a.s.pravieen/Downloads/updated_census_data.csv"
input_file_path = "/Users/a.s.pravieen/Downloads/census_2011 - census_2011.csv.csv"
df = pd.read_csv(input_file_path)
# print(df.columns)

rename_columns = {
    "State name" : "State/UT",
 "District name" : "District",
 "Male_Literate" : "Literate_Male",
"Female_Literate" : "Literate_Female",
 "Rural_Households" : "Households_Rural",
 "Urban_ Households" : "Households_Urban",
 "Age_Group_0_29" : "Young_and_Adult",
 "Age_Group_30_49" : "Middle_Aged",
 "Age_Group_50 to" : "Senior_Citizen",
 "Age not stated" : "Age_Not_Stated"
}

df.rename(columns=rename_columns, inplace=True)
print(df.columns)

df["State/UT"] = df["State/UT"].str.title().str.replace('And','and')
print(df["State/UT"])

df.to_csv(output_file_path)