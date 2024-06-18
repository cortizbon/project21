import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.title("¿Por qué no rellenar datos faltantes con un estadístico general?")
X = np.random.normal(0, 10, size=(10000, 3))
df = pd.DataFrame(data=X,
                  columns=list("ABC"))

df['C_mv'] = [np.random.choice([i, np.nan], p=(0.8, 0.2)) for i in df['C']]

df['C_mv_mean'] = df['C_mv'].fillna(df['C_mv'].mean())
df['C_mv_median'] = df['C_mv'].fillna(df['C_mv'].median())

df = df.drop(columns=['A', 'B'])
fig, axes = plt.subplots(1, 4, 
                         figsize=(10, 6),
                         sharex=True)

for idx, col in enumerate(df.columns):
    axes[idx].hist(df[col], 
           color='red', 
           alpha=0.4, 
           bins=50)
    axes[idx].spines['top'].set_visible(False)
    axes[idx].spines['right'].set_visible(False)
    axes[idx].set_title("X1", size=14)

st.pyplot(fig)