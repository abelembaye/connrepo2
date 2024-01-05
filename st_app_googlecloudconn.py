import streamlit as st
import pandas as pd
from google.cloud import storage
import gcsfs
import json
import st-files-connection


# streamlit_app.py

import streamlit as st
from st_files_connection import FilesConnection

# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('gcs', type=FilesConnection)
#df = conn.read("streamlit-bucket/myfile.csv", input_format="csv", ttl=600)
df = conn.read("streamlit-bucket/myfile.csv", input_format="csv", ttl=0)

# Print results.
for row in df.itertuples():
    st.write(f"{row.Owner} has a :{row.Pet}:")


