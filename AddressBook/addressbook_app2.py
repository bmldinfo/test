import streamlit as st
import json, os
import pandas as pd
from geocode import get_coordinates

DATA_FILE = "data2.json"


# Funktion zum Laden der Adressliste aus einer JSON-Datei
def load_data():
    if os.path.isfile(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
    else:
        data = []
    return data


# Funktion zum Speichern der Adressliste in einer JSON-Datei
def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


# Laden der vorhandenen Adressliste
address_list = load_data()

# Titel der App
st.title("Adressbuch App")

# Sidebar zum Hinzufügen neuer Adressen
st.sidebar.header("Neue Adresse hinzufügen")
name = st.sidebar.text_input("Name")
street = st.sidebar.text_input("Straße")
city = st.sidebar.text_input("Stadt")
submit = st.sidebar.button("Adresse hinzufügen")

# Funktion zum Hinzufügen einer neuen Adresse zur Adressliste
if submit:
    address = f"{street}, {city}"
    latitude, longitude = get_coordinates(address)

    new_address = {
        "name": name,
        "street": street,
        "city": city,
        "latitude": latitude,
        "longitude": longitude
    }
    address_list.append(new_address)
    save_data(address_list)

# Darstellung der Adressliste als Tabelle
df = pd.DataFrame(address_list)
st.table(df)
st.map(df)
