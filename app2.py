import sqlite3
import streamlit as st
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('student.db')
cursor = conn.cursor()

# Specify the table name
table_name = 'STUDENT'  # Replace with your actual table name

# Query to fetch all data from the table
select_query = f'SELECT * FROM {table_name};'
cursor.execute(select_query)
data = cursor.fetchall()

# Close the database connection
conn.close()

# Streamlit App
st.set_page_config(page_title="SQLite Data Viewer", layout="wide")
st.title("SQLite Data Viewer")


def with_pd():
    conn = sqlite3.connect('student.db')
    query = """
    SELECT * FROM STUDENT;
    """
    query = conn.execute(query)
    cols = [column[0] for column in query.description]
    results_df = pd.DataFrame.from_records(
        data=query.fetchall(),
        columns=cols
    )
    st.dataframe(results_df)
    return results_df


# Display the data in a Streamlit table
st.table(with_pd())
