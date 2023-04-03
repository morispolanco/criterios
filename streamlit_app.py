import streamlit as st
import pandas as pd
import re

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def evaluar_criterio(texto, criterio):
    ocurrencias = len(re.findall(criterio, texto, re.IGNORECASE))
    return ocurrencias

def evaluar_ensayo(texto, criterios, pesos):
    puntuacion_total = 0
    for criterio, peso in zip(criterios, pesos):
        ocurrencias = evaluar_criterio(texto, criterio)
        puntuacion_total += ocurrencias * peso
    return puntuacion_total

st.title('Evaluador de Ensayos')
st.write('Esta aplicación evalúa ensayos de acuerdo a criterios específicos proporcionados por el profesor.')

archivo_ensayo = st.file_uploader('Cargue su ensayo en formato de texto (.txt):')

if archivo_ensayo is not None:
    texto_ensayo = archivo_ensayo.read().decode(errors='replace')
    st.write('Ensayo cargado exitosamente.')

    criterios_input = st.text_input('Ingrese los criterios de evaluación separados por comas (por ejemplo: criterio 1,criterio 2,criterio 3):')
    pesos_input = st.text_input('Ingrese los pesos de los criterios en el mismo orden y separados por comas (por ejemplo: 1,2,3):')

    if criterios_input and pesos_input:
        try:
            criterios = [criterio.strip() for criterio in criterios_input.split(',')]
            pesos = [int(peso.strip()) for peso in pesos_input.split(',')]
            if len(criterios) != len(pesos):
                raise ValueError('La cantidad de criterios y pesos no coincide.')

            puntuacion = evaluar_ensayo(texto_ensayo, criterios, pesos)
            st.write(f'La puntuación del ensayo es: {puntuacion}')

        except ValueError as e:
            st.write(f'Error en la entrada de los criterios y pesos: {e}')
else:
    st.write('Por favor, cargue su ensayo antes de continuar.') 
