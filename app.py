import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Test - App")
X = np.random.normal(0, 10, size=(100, 2))

fig, ax = plt.subplots(1, 2, figsize=(10, 6))

ax[0].hist(X[::, 0])
ax[1].hist(X[::, 1])

st.pyplot(fig)