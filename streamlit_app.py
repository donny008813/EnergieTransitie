import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Bepalen van de energie behoefte van een industrieterrein"
)

# Streamlit app layout
st.title("Energy Consumption Dashboard")
st.markdown('''Op deze dashboard zal worden getoond hoe de energie behoefte van een industrieterrein is bepaald. Hiervoor is de beschikbare data van Dutch Fresh Port
gebruikt. Met deze informatie is er eerst een beeld gemaakt specifiek voor dit terrein. Na verder onderzoek zal het mogelijk zijn om van een ander terrein gegevens
in te vullen en hiervan het energieverbruik te kunnen tonen over de toekomst. Hierin is vooral gekijken naar het verbruik van vrachtwagens en het verbruik
van de gebouwen per verschillend type bedrijf. ''')
