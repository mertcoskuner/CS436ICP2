import streamlit as st
import pandas as pd
import numpy as np
import mysql.connector
from mysql.connector import Error

# Title of the Streamlit app
st.title('Streamlit App with MySQL Database')

# Connect to the database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='YOUR_DB_VM_IP_ADDRESS',
            user='streamlit_user',
            password='password',
            database='streamlit_db'
        )
        st.success("Successfully connected to the database")
    except Error as e:
        st.error(f"The error '{e}' occurred")
    return connection

connection = create_connection()

# Function to fetch data from the database
def fetch_data(connection):
    query = "SELECT * FROM your_table_name"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result

# Display data from the database
if connection:
    data = fetch_data(connection)
    df = pd.DataFrame(data, columns=['column1', 'column2'])  # Adjust columns as per your table
    st.write('Data from the database:')
    st.write(df)

# Display a simple DataFrame
st.write('Here is a sample DataFrame:')
sample_data = pd.DataFrame({
    'x': np.arange(10),
    'y': np.random.randn(10)
})
st.write(sample_data)

# Plot a line chart
st.line_chart(sample_data.set_index('x'))
