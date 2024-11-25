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

c_columns , d_columns , e_columns = st.columns(3)

if c_columns.button("Jugador con más muertes en el torneo"):
  fig = plt.figure(figsize=(15, 6))
  Muertes = df.groupby('Player')['Death'].mean().sort_values(ascending=False)
  plt.bar(Muertes.index, Muertes.values, color="Red")
  plt.xlabel('Jugador')
  plt.ylabel('Muertes')
  plt.title('Jugador con más muertes en el torneo')
  _ = plt.xticks(rotation=45,ha="center", )
  st.pyplot(fig)
if d_columns.button("Equipo con más victorias"):
  fig = plt.figure(figsize=(15, 6))
  Victorias = df.groupby('Team')['Rounds Win'].mean()
  plt.bar(Victorias.index, Victorias.values,color="green")
  plt.xlabel('Equipo')
  plt.ylabel('Victorias')
  plt.title('Equipo con mas victorias')
  _ = plt.xticks(rotation="horizontal",ha="center")
  st.pyplot(fig)
if e_columns.button("Equipo con mas derrotas del torneo"):
  fig = plt.figure(figsize=(15, 6))
  Derrotas = df.groupby('Team')['Rounds Lose'].mean()
  plt.bar(Derrotas.index, Derrotas.values,color="cyan")
  plt.xlabel('Equipo')
  plt.ylabel('Derrotas')
  plt.title('Equipo con mas derrotas del torneo')
  _ = plt.xticks(rotation="horizontal",ha="center")
  st.pyplot(fig)

