import pandas as pd

def read_data(file_path):
    """
    Reads the CSV file from the given file path and returns a DataFrame.
    """
    # TODO: implement this function using pd.read_csv
    # Example: return pd.read_csv(file_path)
    pass

def get_average_salary(df):
    """
    Returns the average salary of the employees.
    """
    # TODO: implement this function
    # Example: return df['Salary'].mean()
    pass

def get_department_counts(df):
    """
    Returns a dictionary with the count of employees per department.
    """
    # TODO: implement this function
    # Example: return df['Department'].value_counts().to_dict()
    pass

def get_top_earners(df, n):
    """
    Returns a DataFrame of the top n earners, sorted by salary in descending order.
    """
    # TODO: implement this function
    # Example: return df.sort_values(by='Salary', ascending=False).head(n)
    pass
