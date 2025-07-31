import pandas as pd
import numpy as np

def extract():
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Alice', None],
        'age': [25, 30, 35, 25, np.nan],
        'city': ['New York', 'Paris', 'London', 'New York', None],
        'email': ['alice@mail.com', 'bob@mail.com', 'charlie@mail.com', 'alice@mail.com', None],
        'salary': [70000, 80000, 90000, 70000, None],
        'experience': [2, 5, 7, 2, None],
        'role': ['Data Analyst', 'Manager', 'Engineer', 'Data Analyst', None],
        'team': ['A', 'B', 'C', 'A', None],
        'gender': ['F', 'M', 'M', 'F', None],
        'status': ['Active', 'Active', 'Inactive', 'Active', None]
    }
    df = pd.DataFrame(data)
    print("✅ Extracted data")
    return df

def transform(df):
    df = df.drop_duplicates()
    df = df.fillna({
        'name': 'Unknown',
        'age': 0,
        'city': 'Unknown',
        'email': 'unknown@mail.com',
        'salary': 0,
        'experience': 0,
        'role': 'Unknown',
        'team': 'Unknown',
        'gender': 'Unknown',
        'status': 'Unknown'
    })
    print("✅ Transformed data")
    return df

def load(df):
    df.to_csv("Cleaned_Data.csv", index=False)
    print("✅ Loaded data to output.csv")

def etl():
    df = extract()
    df = transform(df)
    load(df)

if __name__ == "__main__":
    etl()
