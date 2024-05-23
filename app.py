import streamlit as st
import mysql.connector
from mysql.connector import Error

# Database connection details
db_config = {
    'host': '35.238.104.14',  # Use your database VM's external IP address
    'user': 'streamlit_user',
    'password': 'SecureP@ssw0rd1',
    'database': 'streamlit_db'
}

# Function to create a connection to the database
def create_connection():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)
        st.success("Successfully connected to the database")
    except Error as e:
        st.error(f"The error '{e}' occurred")
    return connection

connection = create_connection()

# Function to fetch data from the database
def fetch_data(connection):
    query = "SELECT * FROM your_table_name"  # Replace with your table name
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

# Close the connection
if connection:
    connection.close()

# Display a simple DataFrame
st.write('Here is a sample DataFrame:')
sample_data = pd.DataFrame({
    'x': range(10),
    'y': [i * 2 for i in range(10)]
})
st.write(sample_data)

# Plot a line chart
st.line_chart(sample_data.set_index('x'))
