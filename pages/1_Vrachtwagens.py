import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


elek_vspel = [800, 1464, 2679.12, 4901.997, 8968.67, 16406.2, 30004.15]

jaren_elek_vspel = [2024, 2025, 2026, 2027, 2028, 2029, 2030]

grenslijn = [30000, 30000, 30000, 30000, 30000, 30000, 30000]

elek_vspel1 = [18, 33 , 60 , 109, 198, 361, 659]
elek_vspel_die = [580, 562, 547, 520, 471, 308, 10]

# Gegeven waarden
b = 18
g = 1.833
t = 1  # Voor het eerste jaar

# Bereken g^(1/12)
g_daily = g ** (1 / 365)

# Bereken N voor elke maand
N_per_month = [b * (g_daily ** month) for month in range(365)]
N_per_month

#van kwh naar Mva en van aantal wagens naar kwh per oplaadbeurt
elek_vspel_kwh = [x * 10.8 for x in elek_vspel1]
elek_vspel_Mva = [x / 1000 for x in elek_vspel_kwh]

elek_vspel_diel = [x * 180 for x in elek_vspel_die]
tussen_diel = [x / 0.3 for x in elek_vspel_diel]
diel_kwh = [x * 0.018 for x in tussen_diel]

elek_gebouw = [14.762, 15.36, 15.98, 16.63, 17.30, 18.0, 18.73]
#MVA hier je groeifactor vandaan halen

totaal_Mva = np.array([elek_vspel_Mva]) + np.array([elek_gebouw])

# Streamlit App Title
st.title("Vrachtwagens Data Visualization")

# Plot 2: Line Plot for Electric Vehicle Predictions
st.subheader("Line Plot: Electric Vehicle Predictions")
plt.figure(figsize=(10,6))
plt.plot(jaren_elek_vspel, elek_vspel, label='Prediction Line for Electric Trucks')
#plt.axhline(30000, color='green')
plt.legend()
plt.xlabel('Years')
plt.ylabel('Number of Electric Trucks')
plt.title('Electric Truck Predictions')
st.pyplot(plt)

# Plot 3: Electric and Diesel Truck Predictions with Goal Line
st.subheader("Line Plot: Electric and Diesel Truck Predictions with Goal Line")
show_goal_line = st.checkbox("Show Goal Line (658)")
plt.figure(figsize=(10,6))
plt.plot(jaren_elek_vspel, elek_vspel1, label= 'voorspellings lijn van het aantal elektrische vrachtwagens')
plt.plot(jaren_elek_vspel, elek_vspel_die, label='voorspellingslijn van het aantal diesel vrachtwagens')
plt.title('lijngrafiek met voorspellingslijnen over het type vrachtwagen en doelstellingslijn')
plt.xlabel('jaren')
plt.ylabel('aantal vrachtwagens')
if show_goal_line:
    plt.axhline(658, color='green', linestyle='--', label='Goal Line')
plt.legend(loc='lower right', fontsize='small')
st.pyplot(plt)

# Plot 5: Line Plot for kWh and Diesel Usage
st.subheader("Line Plot: kWh and Diesel Usage per Year")
fig, ax1 = plt.subplots()

plt.plot(jaren_elek_vspel, elek_vspel_kwh, color='blue', label='kWh verbruik per jaar op dagbasis')
plt.legend(loc='lower left', fontsize='small')
plt.xlabel('jaartallen')
plt.ylabel('Stroom in kWh')

ax2 = ax1.twinx()

plt.plot(jaren_elek_vspel, elek_vspel_die, color='red', label='liter verbruik per jaar op dagbasis')
plt.ylabel('diesel in liter')
plt.title('Lijngrafiek van diesel in liter en kWh verbruik per jaar op dagbasis')
plt.legend(loc='upper right', fontsize='small')
fig.tight_layout()
st.pyplot(fig)

# Plot 6: Stacked Bar Plot of kWh and Diesel (converted to kWh)
st.subheader("Stacked Bar Plot: kWh and Diesel Usage (in kWh)")
x = np.arange(len(jaren_elek_vspel))

fig, ax = plt.subplots(figsize=(10, 6))

bars1 = ax.bar(x, elek_vspel_kwh, color='lightblue', label='kWh verbruik per jaar')

bars2 = ax.bar(x, diel_kwh, bottom=elek_vspel_kwh, color='darkred', label='Liter verbruik per jaar in kWh')

ax.set_xlabel('Jaartallen')
ax.set_ylabel('Verbruik')
ax.set_title('Stapelbare Barplots van Verbruik per Jaar')
ax.set_xticks(x)
ax.set_xticklabels(jaren_elek_vspel)
ax.legend()

plt.tight_layout()
st.pyplot(fig)

# Plot 7: kW per Hour for Normal Charger
st.subheader("Line Plot: kW per Hour for Normal Charger")
uren1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
aantal_vrachtwagens = [28, 20, 12, 9.6, 8, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 80, 80, 76, 72, 68, 60, 40]
kw_normale_oplader = [616, 440, 264, 211.2, 176, 132, 88, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1760, 1760, 1672, 1584, 1496, 1320, 880]

plt.figure(figsize=(10, 6))
plt.plot(uren1, kw_normale_oplader, marker='o', color='b', linestyle='-')
plt.xlabel('Uren', fontsize=12)
plt.ylabel('kW op basis van een normale oplader', fontsize=12)
plt.title('kW per uur voor normale oplader', fontsize=14)

plt.grid(True)
plt.xticks(uren1)
plt.tight_layout()
st.pyplot(plt)

# Data for plotting
st.subheader('Line Plot: GW per Hour for Normal Charger')
uren1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
kw_normale_oplader_jaar = [6652.8, 4752.0, 2851.2000000000003, 2280.96, 1900.8000000000002, 1425.6000000000001, 950.4000000000001, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 19008.0, 19008.0, 18057.600000000002, 17107.2, 16156.800000000001, 14256.000000000002, 9504.0]

# Creating a simple line plot using uren1 and kw_normale_oplader data
plt.figure(figsize=(10, 6))
plt.plot(uren1, kw_normale_oplader_jaar, marker='o', color='b', linestyle='-')

# Adding labels and title
plt.xlabel('Uren', fontsize=12)
plt.ylabel('GW op basis van een normale oplader jaardruk', fontsize=12)
plt.title('GW per uur voor normale oplader jaardruk', fontsize=14)

# Display the plot
plt.grid(True)
plt.xticks(uren1)
plt.tight_layout()
st.pyplot(plt)
