import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="GetAround Real Model", page_icon="🚗")
st.title("🚗 GetAround - Prédiction du prix de location")

st.markdown("""
Remplis les caractéristiques du véhicule pour estimer le **prix de location par jour (€)** à l'aide d'un vrai modèle entraîné sur des données réelles.
""")

@st.cache_resource
def load_model():
    return joblib.load("model_getaround_real.pkl")

model = load_model()

with st.form("prediction_form"):
    model_key = st.selectbox("Modèle de voiture", ["Citroën", "Peugeot", "Renault", "BMW", "Mercedes"])
    mileage = st.number_input("Kilométrage", min_value=0, value=50000)
    engine_power = st.number_input("Puissance moteur (ch)", min_value=50, value=110)
    fuel = st.selectbox("Carburant", ["diesel", "petrol", "hybrid", "electric"])
    paint_color = st.selectbox("Couleur", ["black", "white", "grey", "blue", "red", "silver", "orange", "beige", "brown", "green", "yellow", "purple", "pink"])
    car_type = st.selectbox("Type de véhicule", ["sedan", "convertible", "coupe", "suv", "wagon", "van"])
    
    private_parking_available = st.checkbox("Parking privé disponible")
    has_gps = st.checkbox("GPS")
    has_air_conditioning = st.checkbox("Climatisation")
    automatic_car = st.checkbox("Boîte automatique")
    has_getaround_connect = st.checkbox("Getaround Connect")
    has_speed_regulator = st.checkbox("Régulateur de vitesse")
    winter_tires = st.checkbox("Pneus hiver")

    submitted = st.form_submit_button("Prédire")

if submitted:
    input_data = pd.DataFrame([{
        "model_key": model_key,
        "mileage": mileage,
        "engine_power": engine_power,
        "fuel": fuel,
        "paint_color": paint_color,
        "car_type": car_type,
        "private_parking_available": private_parking_available,
        "has_gps": has_gps,
        "has_air_conditioning": has_air_conditioning,
        "automatic_car": automatic_car,
        "has_getaround_connect": has_getaround_connect,
        "has_speed_regulator": has_speed_regulator,
        "winter_tires": winter_tires
    }])

    with st.spinner("Prédiction en cours..."):
        try:
            predicted_price = model.predict(input_data)[0]
            st.success(f"💰 Prix estimé : {predicted_price:.2f} € / jour")
        except Exception as e:
            st.error(f"Erreur de prédiction : {e}")
