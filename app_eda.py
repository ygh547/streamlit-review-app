import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda() :
    df = pd.read_csv('data/review2.csv', index_col=0)

    st.dataframe(df)
