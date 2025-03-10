import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Cargar el modelo entrenado
best_model = joblib.load("modelo_xgboost.pkl")

# Crear la interfaz en Streamlit
st.title("Clasificación de Clientes - Chatbot")

st.subheader("Ingrese los datos del cliente")

# Definir TODAS las variables que el modelo espera
producto = st.number_input("Producto (ID)", min_value=0, max_value=10, step=1)
tipo_carroceria = st.number_input("Tipo de Carrocería (ID)", min_value=0, max_value=10, step=1)
combustible = st.number_input("Combustible (ID)", min_value=0, max_value=10, step=1)
potencia = st.number_input("Potencia", min_value=50, max_value=500, step=10)
trans = st.number_input("Transmisión (ID)", min_value=0, max_value=10, step=1)
forma_pago = st.number_input("Forma de Pago (ID)", min_value=0, max_value=10, step=1)
estado_civil = st.number_input("Estado Civil (ID)", min_value=0, max_value=10, step=1)
genero = st.number_input("Género (ID)", min_value=0, max_value=1, step=1)
ocupacion = st.number_input("Ocupación (ID)", min_value=0, max_value=10, step=1)
provincia = st.number_input("Provincia (ID)", min_value=0, max_value=50, step=1)
campanna1 = st.number_input("Descuento por Financiar (0/1)", min_value=0, max_value=1, step=1)
campanna2 = st.number_input("Descuento por Segundo Coche (0/1)", min_value=0, max_value=1, step=1)
campanna3 = st.number_input("Oferta Especial (0/1)", min_value=0, max_value=1, step=1)
zona_renta = st.number_input("Zona de Renta (ID)", min_value=0, max_value=4, step=1)
rev_garantia = st.number_input("Revisión en Garantía (0/1)", min_value=0, max_value=1, step=1)
averia_grave = st.number_input("Avería Grave (0/1)", min_value=0, max_value=3, step=1)
queja_cac = st.number_input("Quejas en Atención al Cliente (0/1)", min_value=0, max_value=1, step=1)
coste_venta = st.number_input("Coste de Venta (€)", min_value=1000, max_value=10000, step=100)
km_anno = st.number_input("Kilómetros por año", min_value=0, max_value=50000, step=1000)
revisiones = st.number_input("Número de Revisiones", min_value=0, max_value=10, step=1)
edad_cliente = st.number_input("Edad del Cliente", min_value=18, max_value=100, step=1)

# Botón para hacer la predicción
if st.button("Clasificar Cliente"):
    # Crear un DataFrame con TODAS las variables
    datos_cliente = pd.DataFrame([{
        "PRODUCTO": producto,
        "TIPO_CARROCERIA": tipo_carroceria,
        "COMBUSTIBLE": combustible,
        "Potencia": potencia,
        "TRANS": trans,
        "FORMA_PAGO": forma_pago,
        "ESTADO_CIVIL": estado_civil,
        "GENERO": genero,
        "OcupaciOn": ocupacion,
        "PROVINCIA": provincia,
        "Campanna1": campanna1,
        "Campanna2": campanna2,
        "Campanna3": campanna3,
        "Zona_Renta": zona_renta,
        "REV_Garantia": rev_garantia,
        "Averia_grave": averia_grave,
        "QUEJA_CAC": queja_cac,
        "COSTE_VENTA": coste_venta,
        "km_anno": km_anno,
        "Revisiones": revisiones,
        "Edad_Cliente": edad_cliente
    }])

    # Hacer la predicción con el modelo
    prediccion = best_model.predict(datos_cliente)[0]

    # Mostrar el resultado
    if prediccion == 1:
        st.subheader("El cliente es: **Compra más de un coche**")
        st.write("Este cliente tiene alta probabilidad de adquirir otro vehículo.")
    else:
        st.subheader("El cliente es: **No compra más de un coche**")
        st.write("Este cliente tiene baja probabilidad de comprar otro vehículo.")