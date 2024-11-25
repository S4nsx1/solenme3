import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv("valorant champions istanbul.csv")
a_columns , b_columns = st.columns(2)
if a_columns.button("K/D promedio por equipos"):
  fig = plt.figure(figsize=(10, 6))
  kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
  plt.bar(kd.index,kd.values,color="purple")
  plt.xlabel('Team')
  plt.ylabel('Promedio K/D')
  plt.title('K/D promedio por equipo')
  _ = plt.xticks(rotation="horizontal", ha='right')
  st.pyplot(fig)
  
if b_columns.button("Jugador con mas kills"):
  fig = plt.figure(figsize=(12, 6))
  kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
  plt.bar(kills.index, kills.values)
  plt.xlabel('Jugador')
  plt.ylabel('kills')
  plt.title('Jugador con mas kills')
  _ = plt.xticks(rotation=45, ha='right')
  st.pyplot(fig)
