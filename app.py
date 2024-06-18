import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("Test - App")
X = np.random.normal(0, 10, size=(10000, 3))

fig, ax = plt.subplots(1, 3, figsize=(10, 6))

ax[0].hist(X[::, 0], 
           color='red', 
           alpha=0.4, 
           bins=50)
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].set_title("X1", size=14)
ax[1].hist(X[::, 1], 
           color='orange', 
           alpha=0.6, 
           bins=50)
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].set_title("X2", size=14)

ax[2].hist(X[::, 2], 
           color='blue', 
           alpha=0.2, 
           bins=50)
ax[2].spines['top'].set_visible(False)
ax[2].spines['right'].set_visible(False)
ax[2].set_title("X2", size=14)
st.pyplot(fig)