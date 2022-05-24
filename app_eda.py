import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def run_eda() :
    df = pd.read_csv('data/review2.csv', index_col=0)

    st.dataframe(df)

    st.text('리뷰의 길이별 히스토그램')

    fig1 = plt.figure()
    df['length'].hist()
    st.pyplot(fig1)

    st.text('리뷰의 길이가 가장 긴 데이터')
