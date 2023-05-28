import streamlit as st
import pandas as pd

# Page setup 
st.set_page_config(page_title="Papeleria Search Engine", page_icon="🐍", layout="wide") 
st.title("Papeleria Search Engine") 
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")


from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
#credentials = service_account.Credentials.from_service_account_info(
#    st.secrets["gcp_service_account"],
#    scopes=[
#        "https://www.googleapis.com/auth/spreadsheets",
#    ],
#)
#conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
#@st.cache_data(ttl=600)
#@st.cache_resource(ttl=600)
#def run_query(query):
#    rows = conn.execute(query, headers=1)
#    rows = rows.fetchall()
#    return rows

#sheet_url = st.secrets["private_gsheets_url"]
#rows = run_query(f'SELECT * FROM "{sheet_url}"')

# Print results.
#for row in rows:
#    st.write(f"{row.product_type_id} has a {row.product_type}")


# Connect to the Google Sheet 
sheet_id = "1m-kuvMvXRNu_M0b00dmc18-fRoxpbqmtAuhKIWV9054" 
sheet_name = "ProductType" 
url = f"<https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}>" 
df = pd.read_csv(url, dtype=str).fillna("") 
# Show the dataframe (we'll delete this later) 
st.write(df)

