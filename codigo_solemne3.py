import streamlit as st
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv("valorant champions istanbul.csv")

# Rutas de imágenes
image_yay = "yay.jpeg"
image_Cryocells = "Cryocells.jpg"
image_ANGE1 = "ANGE1.jpg"
image_Derke = "Derke.jpg"
image_MaKo = "MaKo.jpg"
image_Scream = "Scream.jpg"
image_kiNgg = "kiNgg.jpg"
image_suygetsu = "suygetsu.jpg"
image_Less = "Less.jpeg"
image_LEV = "LEV.jpg"
image_DRX = "DRX.jpg"
image_XSET = "XSET.jpg"
image_FNC = "FNC.jpg"
image_FPX = "FPX.jpg"
image_OPTC = "OPTC.jpg"
image_TL = "TL.jpg"
image_LOUD = "LOUD.jpg"

# Funciones para mostrar las estadísticas
def mejor_rendimiento():
    filas_seleccionadas = df.iloc[[5]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)

def peor_rendimiento():
    filas_seleccionadas = df.iloc[[19]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)

def mas_kills():
    filas_seleccionadas = df.iloc[[5]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)

def mejor_rendimiento_por_equipo():
    filas_seleccionadas = df.iloc[[3, 5, 10, 17, 22, 25, 32, 35]]  # Cambia el índice según tu CSV
    st.dataframe(filas_seleccionadas)

# Inicializar la página si no está definida
if "page" not in st.session_state:
    st.session_state.page = "home"

# Función para redimensionar imágenes
def resize_image(image_path, width=130, height=152):
    img = Image.open(image_path)
    img_resized = img.resize((width, height))
    return img_resized

# Función para mostrar imagen con su pie de foto
def display_image_with_caption(image_path, caption):
    img_resized = resize_image(image_path)
    st.image(img_resized)
    
    st.markdown(
        f"""
        <style>
        .caption {{
            font-family: 'Arial Black', sans-serif;
            font-size: 15px;
            font-weight: bold;
        }}
        </style>
        <p class="caption">{caption}</p>
        """, unsafe_allow_html=True
    )

# Función para mostrar los logos de los equipos
def imagenes_logos(image_path, width=200, height=200):
    try:
        img = Image.open(image_path)
        img_resized = img.resize((width, height))
        return img_resized
    except Exception as e:
        st.error(f"Error al cargar la imagen {image_path}: {e}")
        return None

# Función para mostrar la imagen con su nombre
def display_logo(image_path, name, width=100, height=100):
    img_resized = imagenes_logos(image_path, width, height)
    if img_resized:
        st.image(img_resized)
        st.caption(name)

# Función para mostrar los logos de los equipos con tamaño 300x300
def imagenes_logos_300(image_path, width=300, height=300):
    try:
        img = Image.open(image_path)
        img_resized = img.resize((width, height))  # Tamaño actualizado a 300x300
        return img_resized
    except Exception as e:
        st.error(f"Error al cargar la imagen {image_path}: {e}")
        return None

# Función para mostrar la imagen con su nombre con tamaño 300x300
def display_logo_300(image_path, name, width=300, height=300):  # Tamaño 300x300
    img_resized = imagenes_logos_300(image_path, width, height)
    if img_resized:
        st.image(img_resized)
        st.caption(name)

# Mostrar el contenido de la página principal
if st.session_state.page == "home":
    st.title("Análisis y Estadísticas del VCT Masters Reykjavik 2022: ¡Revive la Emoción del Torneo!")
    
    video_presentación_ = "https://www.youtube.com/watch?v=j2Z4qYJ3Jtc&ab_channel=VALORANTChampionsTour"
    st.video(video_presentación_)
    st.subheader("Presentación de los equipos participantes del torneo")

    # Mostrar logos de los equipos
    col1, col2, col3 = st.columns([1, 1, 1]) 
    with col2:
        display_logo_300(image_LOUD, "1 LOUD")

    col4, col5, col6 = st.columns([1, 1, 1])  
    with col4:
        display_logo_300(image_OPTC, "2 OPTC")
    with col6:
        display_logo_300(image_DRX, "3 DRX")

    col7, col8, col9, col10, col11 = st.columns([1, 1, 1, 1, 1])  
    with col7:
        display_logo(image_FPX, "4 FPX")
    with col8:
        display_logo(image_XSET, "5 XSET")
    with col9:
        display_logo(image_FNC, "6 FNC")
    with col10:
        display_logo(image_TL, "7 TeamLiquid")
    with col11:
        display_logo(image_LEV, "8 Leviatán")

    # Selección de datos adicionales
    page_selection = st.selectbox(
        "Datos que creemos te gustarán saber",
        ["Ház click para desplegar las opciones", 
         "Cuál fue el jugador con mejor rendimiento global del torneo", 
         "Cuál fue el jugador con peor rendimiento global del torneo", 
         "Cuál fue el jugador con más kills?", 
         "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?"]
    )

    # Redirigir a las páginas correspondientes según la selección del `selectbox`
    if page_selection == "Cuál fue el jugador con mejor rendimiento global del torneo":
        st.session_state.page = "mejor_rendimiento"

    elif page_selection == "Cuál fue el jugador con peor rendimiento global del torneo":
        st.session_state.page = "peor_rendimiento"

    elif page_selection == "Cuál fue el jugador con más kills?":
        st.session_state.page = "mas_kills"

    elif page_selection == "Cuáles fueron los jugadores con mejor rendimiento de cada equipo?":
        st.session_state.page = "mejor_rendimiento_por_equipo"

# Mostrar el contenido correspondiente
if st.session_state.page == "mejor_rendimiento":
    st.title("Jugador con mejor rendimiento")
    mejor_rendimiento()
    display_image_with_caption(image_yay, "Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "peor_rendimiento":
    st.title("Jugador con rendimiento más bajo")
    peor_rendimiento()
    display_image_with_caption(image_ANGE1, "Presentación ANGE1")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "mas_kills":
    st.title("Jugador con más bajas")
    mas_kills()
    display_image_with_caption(image_yay, "Presentación yay")
    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

elif st.session_state.page == "mejor_rendimiento_por_equipo":
    st.title("Jugadores con el mejor rendimiento por equipo")
    mejor_rendimiento_por_equipo()
    
    # Primera fila de imágenes
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        display_image_with_caption(image_Less, "Less")
    with col2:
        display_image_with_caption(image_yay, "Yay")
    with col3:
        display_image_with_caption(image_MaKo, "MaKo")
    with col4:
        display_image_with_caption(image_suygetsu, "SUYGETSU")
    
    # Segunda fila de imágenes
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        display_image_with_caption(image_Cryocells, "Cryocells")
    with col6:
        display_image_with_caption(image_Scream, "Scream")
    with col7:
        display_image_with_caption(image_kiNgg, "kiNgg")
    with col8:
        display_image_with_caption(image_ANGE1, "ANGE1")

    if st.button("Volver a la página principal"):
        st.session_state.page = "home"

a_columns, b_columns = st.columns(2)
if a_columns.button("K/D promedio por equipos"):
    st.subheader("¡Descubre el Poder de los Equipos!")
    st.text("Este gráfico muestra cómo se desempeñan los equipos en cuanto a su ratio de Kills/Deaths (K/D). Los equipos con el mejor desempeño suelen tener una mayor proporción de muertes por baja, lo que refleja una ejecución más eficiente en el juego. ¡Ve quién lidera el torneo en rendimiento!")
    fig = plt.figure(figsize=(10, 6))  # Correct indentation
    kd = df.groupby('Team')['K/D'].mean().sort_values(ascending=False)
    plt.bar(kd.index, kd.values, color="purple")
    plt.xlabel('Team')
    plt.ylabel('Promedio K/D')
    plt.title('K/D promedio por equipo')
    _ = plt.xticks(rotation="horizontal", ha='right')
    st.pyplot(fig)

if b_columns.button("Jugador con mas kills"):
    st.subheader("¿Quién es el Rey de las Bajas?")
    st.text("Este gráfico destaca la acumulación de kills de cada jugador a lo largo del torneo. Si estás buscando al jugador con más acción en el campo de batalla, aquí puedes ver quién se lleva la corona de las eliminaciones. ¡El jugador más letal está aquí!")
    fig = plt.figure(figsize=(12, 6))  # Correct indentation
    kills = df.groupby('Player')['Kill'].mean().sort_values(ascending=False)
    plt.bar(kills.index, kills.values)
    plt.xlabel('Jugador')
    plt.ylabel('kills')
    plt.title('Jugador con mas kills')
    _ = plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)

c_columns, d_columns, e_columns = st.columns(3)

if c_columns.button("Jugador con más muertes en el torneo"):
    st.subheader("¡Las Muertes también Hablan!")
    st.text("A veces el precio del juego es alto, y este gráfico la cantidad de muertes de cada jugador. Aunque no es lo más positivo, saber quién lidera en esta categoría puede dar pistas sobre el estilo de juego o los desafíos a los que se enfrentan los jugadores. ¡Entérate de quiénes son los más golpeados en el torneo!")
    fig = plt.figure(figsize=(15, 6))  # Correct indentation
    Muertes = df.groupby('Player')['Death'].mean().sort_values(ascending=False)
    plt.bar(Muertes.index, Muertes.values, color="Red")
    plt.xlabel('Jugador')
    plt.ylabel('Muertes')
    plt.title('Jugador con más muertes en el torneo')
    _ = plt.xticks(rotation=45, ha="center")
    st.pyplot(fig)

if d_columns.button("Equipo con más victorias"):
    st.subheader("Equipos Triunfadores: ¿Quién Tiene la Mayor Cantidad de Victorias?")
    st.text("El éxito no solo se mide en kills, sino también en victorias. Este gráfico revela a los equipos que más veces han salido victoriosos durante el torneo, mostrando quién tiene el control total en el campo de juego. ¡Descubre al equipo imbatible de esta edición!")
    fig = plt.figure(figsize=(15, 6))  # Correct indentation
    Victorias = df.groupby('Team')['Rounds Win'].mean()
    plt.bar(Victorias.index, Victorias.values, color="green")
    plt.xlabel('Equipo')
    plt.ylabel('Victorias')
    plt.title('Equipo con mas victorias')
    _ = plt.xticks(rotation="horizontal", ha="center")
    st.pyplot(fig)

if e_columns.button("Equipo con mas derrotas del torneo"):
    st.subheader("¿Quién Sufrió Más Derrotas?")
    st.text("Aunque cada derrota es una oportunidad para aprender, algunos equipos han tenido más dificultades que otros. Este gráfico muestra a los equipos con más derrotas, lo que podría reflejar puntos débiles o dificultades para adaptarse al estilo del torneo. ¡Descubre qué equipos tuvieron más trabajo durante la competencia!")
    fig = plt.figure(figsize=(15, 6))  # Correct indentation
    Derrotas = df.groupby('Team')['Rounds Lose'].mean()
    plt.bar(Derrotas.index, Derrotas.values, color="cyan")
    plt.xlabel('Equipo')
    plt.ylabel('Derrotas')
    plt.title('Equipo con mas derrotas del torneo')
    _ = plt.xticks(rotation="horizontal", ha="center")
    st.pyplot(fig)

st.subheader("Si deseas saber más sobre los equipos, revisa las paginas a continuación")


col1, col2, col3, col4, col5, col6, col7, col8 = st.columns([1, 1, 1, 1, 1, 1, 1, 1])
with col1:
    if st.button("LOUD"):
        st.markdown("[LOUD](https://www.vlr.gg/team/6961/loud)", unsafe_allow_html=True)
with col2:
    if st.button("OPTC"):
        st.markdown("[OPTC](https://www.vlr.gg/team/8127/optic-gaming)", unsafe_allow_html=True)
with col3:
    if st.button("DRX"):
        st.markdown("[DRX](https://www.vlr.gg/team/8185/drx)", unsafe_allow_html=True)
with col4:
    if st.button("FPX"):
        st.markdown("[FPX](https://www.vlr.gg/team/11328/funplus-phoenix)", unsafe_allow_html=True)
with col5:
    if st.button("XSET"):
        st.markdown("[XSET](https://www.vlr.gg/team/6314/xset)", unsafe_allow_html=True)
with col6:
    if st.button("FNC"):
        st.markdown("[FNC](https://www.vlr.gg/team/2593/fnatic)", unsafe_allow_html=True)
with col7:
    if st.button("TL"):
        st.markdown("[TL](https://www.vlr.gg/team/474/team-liquid)", unsafe_allow_html=True)
with col8:
    if st.button("LEV"):
        st.markdown("[LEV](https://www.vlr.gg/team/2359/leviat-n)", unsafe_allow_html=True)
