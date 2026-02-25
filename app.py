# Main code for creating streamlit app

import streamlit as st
import pandas as pd

st.set_page_config(page_title="AEMO Price & Generation", layout="wide")
st.title("AEMO Price & Generation Dashboard - starter")
st.write("If you can read this then streamlit is working")

df = pd.DataFrame({"x": range(10), "y": [i**2 for i in range(10)]})
st.line_chart(df.set_index("x"))