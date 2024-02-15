import pandas as pd

# Replace 'exelfile.xlsx' with the path to your Excel file
file_path = 'olmazor.xlsx'

# Read the Excel file
df = pd.read_excel(file_path)

# Access 'ism' column
ism_column = df['ism']

# Write 'ism' column to 'name.txt'
ism_column.to_csv('name.txt', index=False, header=False)
