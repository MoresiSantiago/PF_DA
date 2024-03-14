import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from model2 import recomendar_servicio
from model1 import generar_nuevos_bancos
#config
st.set_page_config(page_title="Data Banks", page_icon="🤖", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")
email_address ="emailcontact@gmail.com"

lottie_file ="https://assets9.lottiefiles.com/packages/lf20_ggwq3ysg.json"

with st.container():
    st.subheader("Hola, somos Data Banks :wave:")
    st.title("Obtén la mejor información sobre bancos y clientes en Estados Unidos.")
    st.write(
        "Somos unos apasionados de la tecnología y la innovación, especializados en el sector de bancos. Nos gusta crear soluciones para resolver problemas y mejorar procesos."
    )
    st.write("[Saber más >](https://databanks.com/)")

    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/Databankslogo.png")
        st.image(image, use_column_width=True)

# Primer Modelo: Predicción de nuevas sucursales de bancos:
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Primer Modelo: Predicción de nuevas sucursales de bancos.")
        st.write(
            """
            Usted elige el número de sucursales que necesita y el umbral debajo del rating del cual toma los bancos y el modelo le dará las localizaciones óptimas según los niveles de satisfaccion de los clientes:

            - El número de nuevos bancos a instalar es definido por el usuario.
            - Utiliza aprendizaje no supervisado, específicamente el algoritmo de K-Means clustering.

            Uso: Usted ingresa dos argumentos.
             - Primero el numero de bancos que quiere crear.
             - Segundo el rating de los bancos tomados.
             - El resultado serán las localizaciones de los nuevos bancos.

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
            """
        )

        num_new_banks = st.number_input("Número de nuevos bancos", min_value=1, max_value=10, value=5)
        # ahora min_rating debe ser el minimo valor mayor que 1
        min_rating = st.number_input("Rating mínimo", min_value=1.1, max_value=5.0, value=3.0, step=0.1)
        if num_new_banks:
            result = generar_nuevos_bancos(num_new_banks, min_rating)
            # result es un DataFrame con las coordenadas de los nuevos bancos por lo que debemos mostrarlo renderizado como tabla
            st.write(result)

    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/mapamodelo.png")
        st.image(image, use_column_width=True)

        st.write("[Más sobre nosotros>](https://databanks.com/about/)")



    with right_column:
        st_lottie(load_lottieurl(lottie_file),key="modelo1", height=400)




# Segundo Modelo: Predicción de nuevas sucursales de bancos:
with st.container():
    st.write("---")
    left_column, right_column= st.columns((2))
    with left_column:
        st.header("Segundo Modelo: Sistema de Recomendación de servicios finacieros a clientes.")
        st.write(
            """
            Usted podrá recomendar a sus clientes distintos servicios financieros.

            - Sugiere dos servicios financieros diferentes a los usuarios de acuerdo a sus satisfacción con su servicio bancario.
            - Utiliza aprendizaje supervisado, específicamente RandomForestClassifier.

            Uso: Usted ingresa 1 argumento.
             - Ingresa el user_id del cliente.
             - Obtendrá un servicio financiero personalizado para el cliente.

            user_id:
             - Plan 1: 1.030135e+20
             - Plan 2: 1.059413e+20

            ***Si esto suena interesante para ti puedes contactarnos a través del formulario que encontrarás al final de la página*** 
            """
    
        )
        user_id = st.text_input("Ingresa el ID del cliente")
        if user_id:
            result = recomendar_servicio(user_id)
            st.write(result)
            
        
        st.write("[Más sobre nosotros>](https://databanks.com/about/)")
    with right_column:
        st_lottie(load_lottieurl(lottie_file),key="modelo2", height=400)







# servicios
with st.container():
    st.write("---")
    st.header("Nuestros servicios")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/apps.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Modelos Machine Learning Bancarios")
        st.write(
            """
            Potencie la toma de decisiones en su institución financiera mediante modelos de machine learning personalizados. Nuestros modelos avanzados analizan datos financieros para proporcionar predicciones precisas, detectar patrones y optimizar estrategias, permitiéndole tomar decisiones informadas y estratégicas.    
            """
        )
        st.write("[Ver servicios >](https://databanks.com/services/)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/automation.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Automatización de procesos bancarios")
        st.write(
            """
            Optimice la eficiencia operativa en su entidad financiera mediante nuestra solución de Automatización de Procesos Bancarios. Desde la gestión de documentos hasta la ejecución de tareas rutinarias, nuestra automatización agiliza los procesos, reduce errores y libera tiempo para que su equipo se enfoque en tareas más estratégicas. Mejore la productividad y la precisión en cada etapa operativa.
            """
        )
        st.write("[Ver servicios >](https://databanks.com/services/)")

with st.container():
    st.write("---")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        image = Image.open("images/visualizacion.png")
        st.image(image, use_column_width=True)
    with text_column:
        st.subheader("Dashboards Bancarios")
        st.write(
            """
            Experimente la transparencia y eficiencia en la gestión financiera con nuestros Dashboards Bancarios intuitivos. Visualice en tiempo real el rendimiento financiero, riesgos, y otros indicadores clave, facilitando la toma de decisiones estratégicas. Obtenga una perspectiva clara y rápida que transformará la manera en que su institución maneja la información financiera.
            """
        )
        st.write("[Ver servicios >](https://databanks.com/services/)")

# contacto
with st.container():
    st.write("---")
    st.header("Ponte en contacto con nosotros!")
    st.write("##")
    contact_form = f"""
    <form action="https://formsubmit.co/{email_address}" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Tu nombre" required>
        <input type="email" name="email" placeholder="Tu email" required>
        <textarea name="message" placeholder="Tu mensaje aquí" required></textarea>
        <button type="submit">Enviar</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
