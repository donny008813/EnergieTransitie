import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Bepalen van de energie behoefte van een industrieterrein"
)

# Streamlit app layout
st.title("Energie Verbruik Dashboard")
st.markdown('''Op deze dashboard zal worden getoond hoe de energie behoefte van een industrieterrein is bepaald. 
Hiervoor is beschikbare data van Dutch Fresh Port, data van het CBS, data van Entso-e, data van modeltype vrachtwagen en data beschikbaar gesteld voor de Case gebruikt. 

Met deze informatie is er eerst een beeld gemaakt specifiek voor dit terrein. Er wordt gekeken naar de volgende eigenschappen:
- Energie verbuik van de huidige en toekomstige vrachtwagen aantallen
- Energie verbruik van de gebouwen totaal en per soort bedrijf
- Bepalen energie verbruik van een gebouw
- Energie verbruik van de gebouwen in de toekomst op basis van oppervlakte aan de hand van een model

Na verder onderzoek zal het mogelijk zijn om van een ander terrein gegevens in te vullen en hiervan het energieverbruik te kunnen tonen over de toekomst. 
Hierin is vooral gekijken naar het verbruik van vrachtwagens en het verbruik van de gebouwen per oppervlak. ''')
