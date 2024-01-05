from google.cloud import storage
import streamlit as st

# Step 1: Create a storage client
storage_client = storage.Client.from_service_account_json(
    './black-heading-405002-e11b4e15b0e5.json')

# Step 2: Generate the HTML file from user input
st.title("Econ 2013 HW3")

firstname = st.text_input("Enter your first name")
lastname = st.text_input("Enter your last name")
user_input = st.text_input("Enter your homework answer")

if st.button('Submit Homework'):
    # Construct the HTML content with user input
    html_content = '<html><body><p>{}</p></body></html>'.format(user_input)

    # Step 3: Upload the HTML content to GCS
    bucket_name = 'hw3_bucket2'
    bucket = storage_client.get_bucket(bucket_name)

    # Create a blob (object) with a unique name
    blob_name = f'{lastname}_{firstname}_output.html'
    blob = bucket.blob(blob_name)

    # Upload the HTML content as the blob's content
    blob.upload_from_string(html_content)

    st.success('Homework submitted successfully!')





