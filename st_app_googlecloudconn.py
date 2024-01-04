import streamlit as st
from google.cloud import storage
import pandas as pd
import gcsfs
import os


# Step 1: Create a storage client
storage_client = storage.Client.from_service_account_json(
    './black-heading-405002-e11b4e15b0e5.json')

# Create a GCS file system instance
fs = gcsfs.GCSFileSystem(token='./black-heading-405002-e11b4e15b0e5.json')

# Specify the GCS file path
gcs_file_path = 'gs://hw3_bucket2/myfile2.csv'

# Read the CSV file from GCS into a pandas DataFrame
with fs.open(gcs_file_path, 'r') as f:
    df = pd.read_csv(f)

# Initialize session state
if 'logged_in' not in st.session_state:  # Check if 'logged_in' already exists
    st.session_state['logged_in'] = False  # Set default value to be 'False'

# Login page
if not st.session_state['logged_in']:
    st.title("Login Page")
    with st.form(key='login_form'):
        username = st.text_input("Enter your username:")
        password = st.text_input("Enter your password:", type='password')
        submit_button = st.form_submit_button('Login')

        if submit_button:
            # Authenticate the user
            if df[(df['username'] == username) & (df['password'] == password)].empty:
                st.error('Invalid username or password')
            else:
                st.session_state['logged_in'] = True
                # Store the username in session state
                st.session_state['username'] = username
else:
    # User input page
    st.title("Quiz 1")
    with st.form(key='input_form'):
        user_input = st.text_input("Enter your homework answer")
        submit_button = st.form_submit_button('Submit Homework')

        if submit_button:
            # Use the username from session state
            file_name = f'{st.session_state["username"]}_output.html'
            with open(file_name, 'w') as f:
                f.write('<html><body><p>{}</p></body></html>'.format(user_input))

            # Step 3: Upload the HTML file to GCS
            bucket_name = 'hw3_bucket2'
            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(file_name)
            blob.upload_from_filename(file_name)
            st.success(
                'Homework submitted successfully!  \n You can now close the browser to logout!')


# To run this app, open a terminal and run the following commands:
# cd "C:\Users\aembaye\OneDrive - University of Arkansas\C2-embaye\Rh\Learn\_Python\myProjects\saving_stfile2cloud"
# conda activate venv4saving2cloud
# streamlit run app4st_tutorial2connecting2googlecloud2.py