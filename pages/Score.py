import streamlit as st
import pandas as pd 

df = pd.read_csv('HBO-MAX-Content.csv', encoding='ISO-8859-1', sep=';')

st.write(df)