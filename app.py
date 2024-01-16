import google.generativeai as genai
import sqlite3
import os
import streamlit as st
from dotenv import load_dotenv
import time
import pandas as pd
load_dotenv()  # load all the environemnt variables

st.set_page_config(page_title="I can Retrieve Any SQL query")

# Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function To Load Google Gemini Model and provide queries as response


def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# debugger gemini


def debug_gemini(err_msg, prompt, response):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[1], err_msg, response])
    return response.text


# Fucntion To retrieve query from the database


def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows


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
    conn.close()
    return results_df


# Define Your Prompt
prompt = [
    """
    You are an expert in converting questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS and MARKS, 
    SECTION \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; \nExample 3 - Give me the all informations about the student name Ali, SELECT * FROM STUDENT WHERE name="Ali", 
    also the sql code should not have ``` in beginning or end and sql word in output

    """,

    """
       You are a debugger and you will analyze the given err messages and according to that message you will regenerate the ONE single complex proper SQL statement,
       You can only execute one statement at a time.
       The SQL database has the name STUDENT and has the following columns - NAME, CLASS and MARKS,
       \n\nFor example, \nExample 1 - err_message : "Unexpected err=Warning('You can only execute one statement at a time.'), type(err)=<class 'sqlite3.Warning'>" query : ["UPDATE STUDENT SET NAME = 'Cabbar' WHERE NAME = 'Krish';" , "SELECT * FROM STUDENT WHERE NAME = 'Cabbar';"] true query : UPDATE STUDENT
        SET NAME = 'Cabbar'
        WHERE NAME = 'Krish'
        RETURNING *;,
        As you saw in the expamle mainly you are gonna generate one proper query accordig to given multiple queries
        Double check the queries and make sure its a proper query for our db and SQL standarts
       also the sql code SHOULD NOT have ``` in beginning or end and sql word in output, ONLY THE SQL proper query

    """


]
# Streamlit App


st.header("Gemini App To Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask the question")
st.table(with_pd())

# if submit is clicked
try:
    if submit:
        response = get_gemini_response(question, prompt)
        print(response)
        st.divider()
        st.subheader("Generated SQL query")
        st.code(response)
        last_response = read_sql_query(response, "student.db")
        st.subheader("The Response is")
        st.table(last_response)
        for row in last_response:
            print(row)
            st.subheader(row, divider="red")
except Exception as err:
    st.error(f"Unexpected {err=}, {type(err)=}")
    time.sleep(3)
    st.subheader("Debugging the error: ")
    debug = debug_gemini(str(err), prompt, response)
    st.code(debug)
    last_response = read_sql_query(debug, "student.db")
    st.subheader("The Debugged Response is")
    st.table(last_response)
    for row in last_response:
        print(row)
        st.subheader(row, divider="blue")


# try:
#     if submit:
#         response = get_gemini_response(question, prompt)
#         print(response)
#         st.divider()
#         st.subheader("Generated SQL query")
#         st.code(response)
#         last_response = with_pd(response, "student.db")
#         st.subheader("The Response is")
#         st.table(last_response)
# except Exception as err:
#     st.error(f"Unexpected {err=}, {type(err)=}")
#     time.sleep(3)
#     st.subheader("Debugging the error: ")
#     debug = debug_gemini(str(err), prompt, response)
#     st.code(debug)
#     last_response = with_pd(debug, "student.db")
#     st.subheader("The Debugged Response is")
#     st.table(last_response)
