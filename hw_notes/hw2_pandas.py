# Import pandas
import pandas as pd

# Create two DataFrames
df1 = pd.DataFrame([
    {'name': 'Alice', 'age': None, 'city': 'New York'},
    {'name': 'Bob', 'age': 26, 'city': 'Los Angeles'},
    {'name': 'Oliver', 'age': None, 'city': 'Salt Lake'}
])

df2 = pd.DataFrame([
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'},
    {'name': 'Diana', 'age': 82, 'city': 'Miami'}
])

# Display DataFrames
print(f'{df1} \n {df2}')

# Combine DataFrames
combined_df = pd.concat([df1,df2])
# Display the combined DataFrame
print(combined_df)

# Reset the index
combined_df.reset_index(drop=True, inplace=True)

# Display the new DataFrame
print(combined_df)