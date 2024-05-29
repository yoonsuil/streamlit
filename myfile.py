import streamlit as st
import pandas as pd
import numpy as np

st.write('# 데이터로 보는 우리')


df = pd.DataFrame(
    np.random.randn(70, 2) + [35.80,127.58],
    columns=['lat','lon'])

st.map(df)