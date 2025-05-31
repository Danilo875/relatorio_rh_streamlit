import streamlit as st
import pandas as pd

@st.cache_data
def carregar_dados(base):
    df = pd.read_csv(base, sep=";")
    return df