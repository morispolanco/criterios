import streamlit as st
import openai
import os
from dotenv import load_dotenv

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Asigna la clave API de OpenAI
openai.api_key = os.environ.get("OPENAI_API_KEY")


def generar_puntuacion_gpt3(texto_ensayo, criterios):
    prompt = f'Evaluar el siguiente ensayo basado en los criterios: {", ".join(criterios)}.\n\nEnsayo:\n{texto_ensayo}\nPuntuación: '

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        temperature=0.5,
    )

    puntuacion = response.choices[0].text.strip()

    try:
        puntuacion = float(puntuacion)
    except ValueError:
        puntuacion = None

    return puntuacion

st.title('Evaluador de Ensayos con GPT-3')
st.write('Esta aplicación evalúa ensayos de acuerdo a criterios específicos proporcionados por el profesor utilizando GPT-3.')

archivo_ensayo = st.file_uploader('Cargue su ensayo en formato de texto (.txt):')

if archivo_ensayo is not None:
    texto_ensayo = archivo_ensayo.read().decode(errors='replace')
    st.write('Ensayo cargado exitosamente.')

    criterios_input = st.text_input('Ingrese los criterios de evaluación separados por comas (por ejemplo: criterio 1,criterio 2,criterio 3):')

    if criterios_input:
        criterios = [criterio.strip() for criterio in criterios_input.split(',')]
        puntuacion = generar_puntuacion_gpt3(texto_ensayo, criterios)

        if puntuacion is not None:
            st.write(f'La puntuación del ensayo es: {puntuacion}')
        else:
            st.write('GPT-3 no pudo generar una puntuación válida. Intente nuevamente.')

       
