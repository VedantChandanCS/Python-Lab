import pandas as pd

#Data Series in pandas

#data series containing integers (int64)
data_series = pd.Series([x for x in range(10)])
print("This is a data series containing int64 values: ")
print(data_series)

#data series containing strings
string_data_series = pd.Series(["o"*x for x in range(10)], dtype="string")
print("This is a data series containing strings ")
print(string_data_series)

#data series containing objects
object_data_series = pd.Series(["string" if x%2==0 else 0 for x in range(10)])
print("This is a data series containing objects: ")
print(object_data_series)

#Data Frames in pandas
#For two dimensional data

#dummy data to load into the dataframe
myData = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Score': [85, 92, 78, 95, 88]
}

data_frame = pd.DataFrame(data=myData)
# print(data_frame.head())


#getting data by columns in data frames
print("Accessing column Name ONLY:")
print(data_frame['Name'])  # Accessing the 'Name' column
print("Accessing column Name ONLY:")
print(data_frame[['Name', 'Score']])  # Accessing multiple columns


#adding new columns to dataframe
data_frame['Grade'] = ['A', 'B', 'C', 'A', 'B']
print("Data Frame with a new column 'Grade':")
print(data_frame)
print()

# Accessing rows of a Data Frame
print("Accessing rows:")
print("Row at second index is: ")
print(data_frame.iloc[2])  # Accessing the row at index 2
print("Rows from index 1 to 3: ")
print(data_frame.iloc[1:4])  # Accessing rows from index 1 to 3
print()

# Filtering Data Frame rows based on a condition
filtered_data_frame = data_frame[data_frame['Age'] > 30]
print("Filtered Data Frame where Age > 30:")
print(filtered_data_frame)
print()

# Modifying values in a Data Frame
data_frame.loc[0, 'Age'] = 26  # Changing the Age of the first person to 26
print("Modified Data Frame:")
print(data_frame)
print()

# Deleting a column from the Data Frame
data_frame.drop(columns=['Score'], inplace=True)
print("Data Frame after deleting 'Score' column:")