import streamlit as st
import pandas as pd
from google.cloud import storage
import gcsfs
import json
from st_files_connection import FilesConnection

import streamlit as st
import pandas as pd
import gcsfs

# Create a connection to GCS
# fs = gcsfs.GCSFileSystem(project='black-heading-405002',
#                          token='black-heading-405002-e11b4e15b0e5.json')

#st.cache.clear()
fs = gcsfs.GCSFileSystem(token='black-heading-405002-e11b4e15b0e5.json')

# Read the CSV file from GCS into a pandas DataFrame
with fs.open('hw3_bucket2/myfile2.csv') as f:
    df = pd.read_csv(f)

# Print results.
for row in df.itertuples():
    st.write(f"{row.username} has a :{row.password}:")



