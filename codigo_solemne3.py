import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("valorant champions istanbul.csv")

if st.button("K/D promedio por equipos"):
  fig = plt.figure(figsize=(10, 6))
  kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
  plt.bar(kd.index,kd.values,color="purple")
  plt.xlabel('Team')
  plt.ylabel('Promedio K/D')
  plt.title('K/D promedio por equipo')
  _ = plt.xticks(rotation="horizontal", ha='right')
  st.pyplot(fig)
