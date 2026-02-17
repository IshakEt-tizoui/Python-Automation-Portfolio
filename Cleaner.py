import pandas as pd

df = pd.read_csv("messy_customers.csv")

df = df.drop_duplicates(subset="Name", keep="first")

df["Email"] = df["Email"].fillna("contact@needed.com")

df_filtered = df[(df['City'] == 'Rabat') & (df['Spent_USD'] > 50)]

total_spent = sum(df_filtered["Spent_USD"])

df_filtered.to_excel("Rabat_VIP_List.xlsx", index=False)

print("-" * 30)

print("Rabat_VIP_List.xlsx' created!")

print(f'Sum of spent USD is : ${total_spent}')

print("-" * 30)
