import streamlit as st
import random
import pandas as pd
import numpy as np

def show_prog_gen_page():

    st.title('Generador de Progresiones Funcionales')
    st.markdown('''

        1. Selecciona una tonalidad.
        2. Elige cuántos acordes deseas en tu progresión.
        3. Presiona 'Enter'

        ¿Por qué siempre suena bien? Eso es un secreto que guardamos bajo siete llaves... 🎵
    ''')


    # Define un diccionario con los acordes y los movimientos fuertes asociados.

    acordes_naturales_c = {
        'C': ['Am', 'F'],
        'Dm': ['Bdim', 'G7'],
        'Em': ['C', 'Am'],
        'F': ['Dm', 'Bdim'],
        'G7': ['Em', 'C'],
        'Am': ['F', 'Dm'],
        'Bdim': ['G7', 'Em']
    }

    sustitutos_naturales_c = {
        'C': ['Am', 'F'],
        'Dm': ['Bdim', 'G7'],
        'Em': ['C', 'Am'],
        'F': ['Dm', 'Bdim'],
        'G7': ['Em', 'C', 'Am'],
        'Am': ['F', 'Dm'],
        'Bdim': ['G7', 'Em']
    }

    intercambio_modal_c = {
        'C': ['Am', 'F'],
        'Dm': ['Bdim', 'G7', 'Fm7', 'Abmaj7', 'Bbmaj7'],
        'Em': ['C', 'Am'],
        'F': ['Dm', 'Bdim'],
        'G7': ['Em', 'C', 'Am'],
        'Am': ['F', 'Dm'],
        'Bdim': ['G7', 'Em', 'Fm7', 'Abmaj7', 'Bbmaj7'],
        'Fm7' : ['C', 'Em'],
        'Abmaj7': ['C', 'Em'],
        'Bbmaj7' :  ['C', 'Em', 'Am']
    }

    sustitutos_tritonales_c = {
        'C': ['Am', 'F'],
        'Dm': ['Bdim', 'G7', 'Fm7', 'Abmaj7', 'Bbmaj7', 'Dbmaj7'],
        'Em': ['C', 'Am'],
        'F': ['Dm', 'Bdim'],
        'G7': ['Em', 'C', 'Am'],
        'Am': ['F', 'Dm'],
        'Bdim': ['G7', 'Em', 'Fm7', 'Abmaj7', 'Bbmaj7', 'Dbmaj7'],
        'Fm7' : ['C', 'Em'],
        'Abmaj7': ['C', 'Em'],
        'Bbmaj7' :  ['C', 'Em', 'Am'],
        'Dbmaj7': ['C','Em', 'Am']
    }

    acordes_naturales_d = {
        'D': ['Bm', 'G'],
        'Em': ['C#dim', 'A7'],
        'F#m': ['D', 'Bm'],
        'G': ['Em', 'C#dim'],
        'A7': ['F#m', 'D'],
        'Bm': ['G', 'Em'],
        'C#dim': ['A7', 'F#m'],
        'Gm7' : ['D', 'F#m'],
        'Bbmaj7': ['D', 'F#m'],
        'Cmaj7' :  ['D', 'F#m'],
        'Ebmaj7': ['D', 'F#m']
    }

    sustitutos_naturales_d = {
        'D': ['Bm', 'G'],
        'Em': ['C#dim', 'A7'],
        'F#m': ['D', 'Bm'],
        'G': ['Em', 'C#dim'],
        'A7': ['F#m', 'D', 'Bm'],
        'Bm': ['G', 'Em'],
        'C#dim': ['A7', 'F#m'],
        'Gm7' : ['D', 'F#m'],
        'Bbmaj7': ['D', 'F#m'],
        'Cmaj7' :  ['D', 'F#m', 'Bm'],
        'Ebmaj7': ['D', 'F#m', 'Bm']
    }

    intercambio_modal_d = {
        'D': ['Bm', 'G'],
        'Em': ['C#dim', 'A7', 'Gm7', 'Bbmaj7', 'Cmaj7'],
        'F#m': ['D', 'Bm'],
        'G': ['Em', 'C#dim'],
        'A7': ['F#m', 'D'],
        'Bm': ['G', 'Em'],
        'C#dim': ['A7', 'Gm7', 'Bbmaj7', 'Cmaj7', 'F#m'],
        'Gm7' : ['D', 'F#m'],
        'Bbmaj7': ['D', 'F#m'],
        'Cmaj7' :  ['D', 'F#m'],
        'Ebmaj7': ['D', 'F#m']
    }

    sustitutos_tritonales_d = {
        'D': ['Bm', 'G'],
        'Em': ['C#dim', 'A7', 'Gm7', 'Bbmaj7', 'Cmaj7', 'Ebmaj7'],
        'F#m': ['D', 'Bm'],
        'G': ['Em', 'C#dim'],
        'A7': ['F#m', 'D'],
        'Bm': ['G', 'Em'],
        'C#dim': ['A7', 'Gm7', 'Bbmaj7', 'Cmaj7', 'F#m', 'Ebmaj7'],
        'Gm7' : ['D', 'F#m'],
        'Bbmaj7': ['D', 'F#m'],
        'Cmaj7' :  ['D', 'F#m'],
        'Ebmaj7': ['D', 'F#m']
    }

    acordes_naturales_e = {
        'E': ['C#m', 'A'],
        'F#m': ['D#dim', 'B7'],
        'G#m': ['E', 'C#m'],
        'A': ['F#m', 'D#dim'],
        'B7': ['G#m', 'E'],
        'C#m': ['A', 'F#m'],
        'D#dim': ['B7', 'G#m'],
        'Am7' : ['E', 'G#m'],
        'Cmaj7': ['E', 'G#m'],
        'Dmaj7' :  ['E', 'G#m'],
        'Fmaj7': ['E', 'G#m']
    }

    sustitutos_naturales_e = {
        'E': ['C#m', 'A'],
        'F#m': ['D#dim', 'B7'],
        'G#m': ['E', 'C#m'],
        'A': ['F#m', 'D#dim'],
        'B7': ['G#m', 'E', 'C#m'],
        'C#m': ['A', 'F#m'],
        'D#dim': ['B7', 'G#m'],
        'D#dim': ['B7', 'G#m'],
        'Am7' : ['E', 'G#m'],
        'Cmaj7': ['E', 'G#m'],
        'Dmaj7' :  ['E', 'G#m', 'C#m'],
        'Fmaj7': ['E', 'G#m', 'C#m']
    }

    intercambio_modal_e = {
        'E': ['C#m', 'A'],
        'F#m': ['D#dim', 'B7', 'Am7', 'Cmaj7', 'Dmaj7'],
        'G#m': ['E', 'C#m'],
        'A': ['F#m', 'D#dim'],
        'B7': ['G#m', 'E', 'C#m'],
        'C#m': ['A', 'F#m'],
        'D#dim': ['B7', 'G#m'],
        'D#dim': ['B7', 'Am7', 'Cmaj7', 'Dmaj7', 'G#m'],
        'Am7' : ['E', 'G#m'],
        'Cmaj7': ['E', 'G#m'],
        'Dmaj7' :  ['E', 'G#m', 'C#m'],
        'Fmaj7': ['E', 'G#m', 'C#m']
    }

    sustitutos_tritonales_e = {
        'E': ['C#m', 'A'],
        'F#m': ['D#dim', 'B7', 'Am7', 'Cmaj7', 'Dmaj7', 'Fmaj7'],
        'G#m': ['E', 'C#m'],
        'A': ['F#m', 'D#dim'],
        'B7': ['G#m', 'E', 'C#m'],
        'C#m': ['A', 'F#m'],
        'D#dim': ['B7', 'G#m'],
        'D#dim': ['B7', 'Am7', 'Cmaj7', 'Dmaj7', 'G#m', 'Fmaj7'],
        'Am7' : ['E', 'G#m'],
        'Cmaj7': ['E', 'G#m'],
        'Dmaj7' :  ['E', 'G#m', 'C#m'],
        'Fmaj7': ['E', 'G#m', 'C#m']
    }

    acordes_naturales_f = {
        'F': ['Dm', 'Bb'],
        'Gm': ['Edim', 'C7'],
        'Am': ['F', 'Dm'],
        'Bb': ['Gm', 'Edim'],
        'C7': ['Am', 'F'],
        'Dm': ['Bb', 'Gm'],
        'Edim': ['C7', 'Am'],
        'Bbm7' : ['F', 'Am'],
        'Dbmaj7': ['F', 'Am'],
        'Ebmaj7' :  ['F', 'Am'],
        'Gbmaj7': ['F', 'Am']
    }

    sustitutos_naturales_f = {
        'F': ['Dm', 'Bb'],
        'Gm': ['Edim', 'C7'],
        'Am': ['F', 'Dm'],
        'Bb': ['Gm', 'Edim'],
        'C7': ['Am', 'F', 'Dm'],
        'Dm': ['Bb', 'Gm'],
        'Edim': ['C7', 'Am'],
        'Bbm7' : ['F', 'Am'],
        'Dbmaj7': ['F', 'Am'],
        'Ebmaj7' :  ['F', 'Am', 'Dm'],
        'Gbmaj7': ['F', 'Am', 'Dm']
    }

    intercambio_modal_f = {
        'F': ['Dm', 'Bb'],
        'Gm': ['Edim', 'C7', 'Bbm7', 'Dbmaj7', 'Ebmaj7'],
        'Am': ['F', 'Dm'],
        'Bb': ['Gm', 'Edim'],
        'C7': ['Am', 'F', 'Dm'],
        'Dm': ['Bb', 'Gm'],
        'Edim': ['C7', 'Am', 'Bbm7', 'Dbmaj7', 'Ebmaj7'],
        'Bbm7' : ['F', 'Am'],
        'Dbmaj7': ['F', 'Am'],
        'Ebmaj7' :  ['F', 'Am', 'Dm'],
        'Gbmaj7': ['F', 'Am', 'Dm']
    }

    sustitutos_tritonales_f = {
        'F': ['Dm', 'Bb'],
        'Gm': ['Edim', 'C7', 'Bbm7', 'Dbmaj7', 'Ebmaj7', 'Gbmaj7'],
        'Am': ['F', 'Dm'],
        'Bb': ['Gm', 'Edim'],
        'C7': ['Am', 'F', 'Dm'],
        'Dm': ['Bb', 'Gm'],
        'Edim': ['C7', 'Am', 'Bbm7', 'Dbmaj7', 'Ebmaj7','Gbmaj7'],
        'Bbm7' : ['F', 'Am'],
        'Dbmaj7': ['F', 'Am'],
        'Ebmaj7' :  ['F', 'Am', 'Dm'],
        'Gbmaj7': ['F', 'Am', 'Dm']
    }


    acordes_naturales_g = {
        'G': ['Em', 'C'],
        'Am': ['F#dim', 'D7'],
        'Bm': ['G', 'Em'],
        'C': ['Am', 'F#dim'],
        'D7': ['Bm', 'G'],
        'Em': ['C', 'Am'],
        'F#dim': ['D7', 'Bm'],
        'Cm7' : ['G', 'Bm'],
        'Ebmaj7': ['G', 'Bm'],
        'Fmaj7' :  ['G', 'Bm'],
        'Abmaj7': ['G', 'Bm']
    }

    sustitutos_naturales_g = {
        'G': ['Em', 'C'],
        'Am': ['F#dim', 'D7'],
        'Bm': ['G', 'Em'],
        'C': ['Am', 'F#dim'],
        'D7': ['Bm', 'G', 'Em'],
        'Em': ['C', 'Am'],
        'F#dim': ['D7', 'Bm'],
        'Cm7' : ['G', 'Bm'],
        'Ebmaj7': ['G', 'Bm'],
        'Fmaj7' :  ['G', 'Bm', 'Em'],
        'Abmaj7': ['G', 'Bm', 'Em']
    }

    intercambio_modal_g = {
        'G': ['Em', 'C'],
        'Am': ['F#dim', 'D7', 'Cm7', 'Ebmaj7', 'Fmaj7'],
        'Bm': ['G', 'Em'],
        'C': ['Am', 'F#dim'],
        'D7': ['Bm', 'G', 'Em'],
        'Em': ['C', 'Am'],
        'F#dim': ['D7', 'Bm', 'Cm7', 'Ebmaj7', 'Fmaj7'],
        'Cm7' : ['G', 'Bm'],
        'Ebmaj7': ['G', 'Bm'],
        'Fmaj7' :  ['G', 'Bm', 'Em'],
        'Abmaj7': ['G', 'Bm', 'Em']
    }

    sustitutos_tritonales_g = {
        'G': ['Em', 'C'],
        'Am': ['F#dim', 'D7', 'Cm7', 'Ebmaj7', 'Fmaj7', 'Abmaj7'],
        'Bm': ['G', 'Em'],
        'C': ['Am', 'F#dim'],
        'D7': ['Bm', 'G', 'Em'],
        'Em': ['C', 'Am'],
        'F#dim': ['D7', 'Bm', 'Cm7', 'Ebmaj7', 'Fmaj7','Abmaj7'],
        'Cm7' : ['G', 'Bm'],
        'Ebmaj7': ['G', 'Bm'],
        'Fmaj7' :  ['G', 'Bm', 'Em'],
        'Abmaj7': ['G', 'Bm', 'Em']
    }

    acordes_naturales_a = {
        'A': ['F#m', 'D'],
        'Bm': ['G#dim', 'E7'],
        'C#m': ['A', 'F#m'],
        'D': ['Bm', 'G#dim'],
        'E7': ['C#m', 'A'],
        'F#m': ['D', 'Bm'],
        'G#dim': ['E7', 'C#m'],
        'Dm7' : ['A', 'C#m'],
        'Fmaj7': ['A', 'C#m'],
        'Gmaj7' :  ['A', 'C#m'],
        'Bbmaj7': ['A', 'C#m']
    }

    sustitutos_naturales_a = {
        'A': ['F#m', 'D'],
        'Bm': ['G#dim', 'E7'],
        'C#m': ['A', 'F#m'],
        'D': ['Bm', 'G#dim'],
        'E7': ['C#m', 'A', 'F#m'],
        'F#m': ['D', 'Bm'],
        'G#dim': ['E7', 'C#m'],
        'Dm7' : ['A', 'C#m'],
        'Fmaj7': ['A', 'C#m'],
        'Gmaj7' :  ['A', 'C#m', 'F#m'],
        'Bbmaj7': ['A', 'C#m', 'F#m']
    }

    intercambio_modal_a = {
        'A': ['F#m', 'D'],
        'Bm': ['G#dim', 'E7', 'Dm7', 'Fmaj7', 'Gmaj7'],
        'C#m': ['A', 'F#m'],
        'D': ['Bm', 'G#dim'],
        'E7': ['C#m', 'A', 'F#m'],
        'F#m': ['D', 'Bm'],
        'G#dim': ['E7', 'C#m', 'Dm7', 'Fmaj7', 'Gmaj7'],
        'Dm7' : ['A', 'C#m'],
        'Fmaj7': ['A', 'C#m'],
        'Gmaj7' :  ['A', 'C#m', 'F#m'],
        'Bbmaj7': ['A', 'C#m', 'F#m']
    }

    sustitutos_tritonales_a = {
        'A': ['F#m', 'D'],
        'Bm': ['G#dim', 'E7', 'Dm7', 'Fmaj7', 'Gmaj7', 'Bbmaj7'],
        'C#m': ['A', 'F#m'],
        'D': ['Bm', 'G#dim'],
        'E7': ['C#m', 'A', 'F#m'],
        'F#m': ['D', 'Bm'],
        'G#dim': ['E7', 'C#m', 'Dm7', 'Fmaj7', 'Gmaj7','Bbmaj7'],
        'Dm7' : ['A', 'C#m'],
        'Fmaj7': ['A', 'C#m'],
        'Gmaj7' :  ['A', 'C#m', 'F#m'],
        'Bbmaj7': ['A', 'C#m', 'F#m']
    }

    acordes_naturales_b = {
        'B': ['G#m', 'E'],
        'C#m': ['A#dim'],
        'D#m': ['B', 'G#m'],
        'E': ['C#m', 'A#dim'],
        'F#7': ['D#m', 'B'],
        'G#m': ['E', 'C#m'],
        'A#dim': ['F#7', 'D#m'],
        'Em7' : ['B', 'D#m'],
        'Gmaj7': ['B', 'D#m'],
        'Amaj7' :  ['B', 'D#m', 'G#m'],
        'Cmaj7': ['B', 'D#m', 'G#m']
    }

    sustitutos_naturales_b = {
        'B': ['G#m', 'E'],
        'C#m': ['A#dim', 'F#7'],
        'D#m': ['B', 'G#m'],
        'E': ['C#m', 'A#dim'],
        'F#7': ['D#m', 'B', 'G#m'],
        'G#m': ['E', 'C#m'],
        'A#dim': ['F#7', 'D#m'],
        'Em7' : ['B', 'D#m'],
        'Gmaj7': ['B', 'D#m'],
        'Amaj7' :  ['B', 'D#m', 'G#m'],
        'Cmaj7': ['B', 'D#m', 'G#m']
    }

    intercambio_modal_b = {
        'B': ['G#m', 'E'],
        'C#m': ['A#dim', 'F#7', 'Em7', 'Gmaj7', 'Amaj7'],
        'D#m': ['B', 'G#m'],
        'E': ['C#m', 'A#dim'],
        'F#7': ['D#m', 'B', 'G#m'],
        'G#m': ['E', 'C#m'],
        'A#dim': ['F#7', 'D#m', 'Em7', 'Gmaj7', 'Amaj7'],
        'Em7' : ['B', 'D#m'],
        'Gmaj7': ['B', 'D#m'],
        'Amaj7' :  ['B', 'D#m', 'G#m'],
        'Cmaj7': ['B', 'D#m', 'G#m']
    }

    sustitutos_tritonales_b = {
        'B': ['G#m', 'E'],
        'C#m': ['A#dim', 'F#7', 'Em7', 'Gmaj7', 'Amaj7', 'Cmaj7'],
        'D#m': ['B', 'G#m'],
        'E': ['C#m', 'A#dim'],
        'F#7': ['D#m', 'B', 'G#m'],
        'G#m': ['E', 'C#m'],
        'A#dim': ['F#7', 'D#m', 'Em7', 'Gmaj7', 'Amaj7','Cmaj7'],
        'Em7' : ['B', 'D#m'],
        'Gmaj7': ['B', 'D#m'],
        'Amaj7' :  ['B', 'D#m', 'G#m'],
        'Cmaj7': ['B', 'D#m', 'G#m']
    }


    # Define un diccionario con las tonalidades y sus respectivos diccionarios de acordes.
    tonalidades_naturales = {
        'C': acordes_naturales_c,
        'D': acordes_naturales_d,
        'E': acordes_naturales_e,
        'F': acordes_naturales_f,
        'G': acordes_naturales_g,
        'A': acordes_naturales_a,
        'B': acordes_naturales_b,
    }

    tonalidades_sustitutos_naturales = {
        'C': sustitutos_naturales_c,
        'D': sustitutos_naturales_d,
        'E': sustitutos_naturales_e,
        'F': sustitutos_naturales_f,
        'G': sustitutos_naturales_g,
        'A': sustitutos_naturales_a,
        'B': sustitutos_naturales_b,
    }


    tonalidades_intercambio_modal = {
        'C': intercambio_modal_c,
        'D': intercambio_modal_d,
        'E': intercambio_modal_e,
        'F': intercambio_modal_f,
        'G': intercambio_modal_g,
        'A': intercambio_modal_a,
        'B': intercambio_modal_b,
    }

    tonalidades_sustitutos_tritonales = {
        'C': sustitutos_tritonales_c,
        'D': sustitutos_tritonales_d,
        'E': sustitutos_tritonales_e,
        'F': sustitutos_tritonales_f,
        'G': sustitutos_tritonales_g,
        'A': sustitutos_tritonales_a,
        'B': sustitutos_tritonales_b,
    }


    # Define un diccionario con las tonalidades y sus quintos grados asociados.
    quinto_grado = {
        'C': 'G7',
        'F': 'C7',
        'G': 'D7',
        'D': 'A7',
        'E': 'B7',
        'A': 'E7',
        'B': 'F#7',
    }

    #Evitar generación no solicitada de progresiones:

    def generate_chord_progression(tonalidad, num_acordes):
        acordes_movimientos = tonalidades[tonalidad]
        progresion = [tonalidad]

        for i in range(num_acordes - 1):
            ultimo_acorde = progresion[-1]
            if len(progresion) >= 4 and progresion[-4] == quinto_grado[tonalidad]:
                progresion.append(quinto_grado[tonalidad])
            else:
                siguiente_acorde = random.choice(acordes_movimientos[ultimo_acorde])
                progresion.append(siguiente_acorde)
        return progresion


    # Inicializar 'tonalidades' a tonalidades_naturales por defecto
    tonalidades = tonalidades_naturales

    # Pide al usuario que elija una tonalidad y un número de acordes.
    tonalidad = st.selectbox('Elige una tonalidad', list(tonalidades.keys()))
    num_acordes = st.slider('Elige el número de acordes', 1, 64, 8)

    # Permitir al usuario seleccionar un estilo de progresión de acordes.

    estilos = ['Acordes naturales', 'Sustitutos naturales', 'Intercambio modal', 'Sustitutos tritonales']

    estilo = st.select_slider('Selecciona la complejidad de la progresión', options=estilos)

    st.write(f"Complejizar añadiendo: {estilo}")

    # Define 'tonalidades' en base a la elección del usuario.
    if estilo == 'Acordes naturales':
        tonalidades = tonalidades_naturales
    elif estilo == 'Sustitutos naturales':
        tonalidades = tonalidades_sustitutos_naturales
    elif estilo == 'Intercambio modal':
        tonalidades = tonalidades_intercambio_modal
    elif estilo == 'Sustitutos tritonales':
        tonalidades = tonalidades_sustitutos_tritonales
    else:  
        tonalidades = tonalidades_naturales  # por defecto



    # Comprueba si ya hay una progresión de acordes en el estado de la sesión y si la tonalidad, el número de acordes, o el estilo ha cambiado.
    if 'progresion' not in st.session_state or tonalidad != st.session_state['tonalidad'] or num_acordes != st.session_state['num_acordes'] or estilo != st.session_state['estilo']:

        # Selecciona el diccionario de movimientos armónicos correcto en función de la tonalidad elegida.
        acordes_movimientos = tonalidades[tonalidad]

        # Comienza la progresión en la tónica elegida.
        progresion = [tonalidad]

        # Para cada acorde restante en la progresión...
        for i in range(num_acordes - 1):
            # Si esta es la última posición de acorde, elige el quinto grado.
            if i == num_acordes - 2:
                progresion.append(quinto_grado[tonalidad])
            else:
                # Si no, elige aleatoriamente un acorde que represente un movimiento fuerte desde el acorde actual.
                ultimo_acorde = progresion[-1]
                siguiente_acorde = random.choice(acordes_movimientos[ultimo_acorde])

                # Agrega el nuevo acorde a la progresión.
                progresion.append(siguiente_acorde)

        # Guarda la progresión, la tonalidad, el número de acordes y el estilo en el estado de la sesión
        st.session_state['progresion'] = progresion
        st.session_state['tonalidad'] = tonalidad
        st.session_state['num_acordes'] = num_acordes
        st.session_state['estilo'] = estilo

    else:
        # Usa la progresión de acordes guardada
        progresion = st.session_state['progresion']



    # Muestra la progresión generada.
    st.write("Progresión generada:")
    progresion = ' | '.join(progresion)
    st.markdown(f'## **{progresion}**')


    st.write("")
    st.write("")
    st.write("")
    readme_text = """
    # Generador de Progresiones de Acordes

    Este Generador de Acordes crea progresiones armónicas efectivas y atractivas de una manera simple y divertida.

    ## ¿Cómo funciona?

    La aplicación se basa en principios de composición musical, en particular, en los movimientos armónicos de los acordes. Seleccionas una tonalidad, el número de acordes que deseas en tu progresión y su grado de complejidad armónica, y la aplicación genera una progresión de acordes. 

    ## Los movimientos armónicos

    Los movimientos armónicos son de tres clases:

    1. Movimiento fuerte: en el cambio de un acorde tríada a otro, una o dos notas cambian, pero se mantiene la tónica del primer acorde.
    
    2. Movimiento medio: todas las notas cambian.

    3. Movimiento débil: una o dos notas cambian, pero no se mantiene la tónica del primer acorde.

    La aplicación utiliza principalmente los movimientos fuertes para generar las progresiones de acordes en la modalidad más simple de generación de progresiones con los acordes naturales. 

    Este tipo de movimiento es frecuente en las progresiones populares más comunes. Por ejemplo, en la secuencia:
    
        #### C-Am-Dm-G 
    
    Cada cambio de acorde implica un movimiento fuerte.

    La generación de progresiones, además de los movimientos fuertes como principal recurso para el movimiento de los acordes generados aleatoriamente, se puede personalizar y enriquecer agregando:

    * los acordes sustitutos naturales del primer grado (VIm) para los casos donde un quinto grado dominante resuelve al primer grado.

    * los acordes de intercambio modal pertenecientes al modo menor cuya función armónica es de subdominante menor y que se "toman prestados" para su uso en la tonalidad mayor como sustituto del quinto grado dominante.

    * los acordes sustitutos del quinto grado dominante que comparten el tritono que contiene el quinto grado natural (5b7 de V).



    ## Uso de la aplicación

    Para utilizar la aplicación, sigue estos pasos:

    1. Selecciona una tonalidad.
    2. Elige cuántos acordes deseas en tu progresión.
    3. Selecciona la complejidad de la progresión: conforme avance el deslizador hacia la derecha, la progresión se complejizará:

    | Menos complejo | **Acordes naturales** | **Sustitutos naturales** | **Intercambio modal** | **Sustitutos tritonales** | Más complejo |
    | ------------------ | ----------------- | -------------------- | ----------------- | --------------------- | ---------------- |


    Las opciones se acumulan de forma progresiva. Por ejemplo, la opción "Sustitutos tritonales" incluye los acordes de sustitución tritonal, los de intercambio modal, los sustitutos naturales y los acordes naturales. Por otro lado, la opción "Intercambio modal" incluye los acordes de intercambio modal, así como todas las opciones de la opción anterior, que son los sustitutos naturales y los acordes naturales. Sin embargo, la opción "Intercambio modal" no incluye los sustitutos tritonales. 

    
    4. Presiona 'Enter' y visualiza la progresión generada.
    
    ***Ten en cuenta que la aparición de los acordes correspondientes a cada opción no está garantizada en todas las progresiones, ya que se toman decisiones aleatorias basadas en las reglas de teoría musical descritas arriba.*** 

    
"""

    # Muestra el checkbox "Encuentra las 7 llaves"
    if st.checkbox('Encuentra las 7 llaves'):
        st.markdown(readme_text, unsafe_allow_html=False)

    #Evitar generaciones de progresiones no solicitadas:

    def generate_chord_progression(tonalidad, num_acordes):
        acordes_movimientos = tonalidades[tonalidad]
        progresion = [tonalidad]

        for i in range(num_acordes - 1):
            ultimo_acorde = progresion[-1]
            if len(progresion) >= 4 and progresion[-4] == quinto_grado[tonalidad]:
                progresion.append(quinto_grado[tonalidad])
            else:
                siguiente_acorde = random.choice(acordes_movimientos[ultimo_acorde])
                progresion.append(siguiente_acorde)
        return progresion

