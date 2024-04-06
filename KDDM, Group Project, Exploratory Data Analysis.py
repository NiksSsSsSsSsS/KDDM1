import os
import pandas as pd

# Change the current working directory
os.chdir("C:/Users/schra/OneDrive/Dokumente/CSS/2. Semester/KDDM/Group Project, 17")
# Reading the CSV file into a DataFrame
df = pd.read_csv('data_7.csv')
# Set display options to show all columns
pd.set_option('display.max_columns', None)

# Display the first few rows of the DataFrame
#print(df.head())
#print(df.info())

# Summary Statistics
#print(df.describe())

# Exportiert summary Tabelle
#summary_stats = df.describe()
#summary_stats.to_excel('summary_statistics.xlsx', index=True)

# Handling Missing Values
print(df.isna().sum())

#Drop na (HeatingType), removes the 5 missing values across all values
df_cleaned = df.dropna(how='all')
#print(df_cleaned.isna().sum())
#print(df_cleaned.head())


# Count the cases where 'SquareFootageHouse       ' is smaller than 0
negative_square_footage_house_count = (df['SquareFootageHouse       '] < 0).sum()
# Display the count
print("Number of cases where SquareFootageHouse        is smaller than 0:", negative_square_footage_house_count)

# Filter the DataFrame to get rows where 'SquareFootageHouse       ' is smaller than 0
negative_square_footage_house_cases = df[df['SquareFootageHouse       '] < 0]
# Print the cases where 'SquareFootageHouse       ' is smaller than 0
print("Cases where SquareFootageHouse  is smaller than 0:")
print(negative_square_footage_house_cases)