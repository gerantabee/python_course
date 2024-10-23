import pandas as pd

df = pd.read_csv("../data/sat_scores.csv")
df.info()
#Note that in Python shell you need to force a print of the head (vs. Colab)
# Use head(), describe(), shape and info() to explore your data
print(df.head(5))
print(df.describe())
print(df.shape)

#use sort_values to sort on one or more columns
#Add inplace=True after showing the sort the first time
# Use debug and DataFrame view to see the data in real-time
df_sorted = df.sort_values("Student")
print(df)
df.sort_values(["School","Math"],inplace=True)
print(df)
print(df_sorted)

# Let's add more data from another file and join them
df_more = pd.read_csv("../data/sat_scores_more.csv")
df_all = pd.concat([df,df_more])

# Use eval() to calculate and add columns ( 'feature engineering')
df_all['Total'] = df_all.eval('Math + Reading')

print(df_all.shape)

# Finally we can write our DataFrame to a CSV
df_all.to_csv("../data/sat_scores_all.csv",index=False)

# Query a subset of the data to make a new DataFrame
df_best_grades = df_all.query('Math >= 700 and Reading >=700')
# OR
# df_best_grades = df_all[(df_all.Math > 700) & (df_all.Reading > 700)]
print(df_best_grades.head())