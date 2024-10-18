import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Sample Data
jaren_elek_vspel = [2018, 2019, 2020, 2021, 2022, 2023, 2024]
elek_vspel = [800, 1464, 2679.12, 4901.997, 8968.67, 16406.2, 30004.15]
elek_gebouw = [700, 1200, 2300, 4200, 8500, 15000, 29000]
elek_vspel1 = [800, 1500, 3000, 4500, 9000, 16000, 32000]
elek_vspel_die = [1000, 1800, 2500, 4000, 7000, 12000, 18000]
elek_vspel_Mva = [500, 1000, 2000, 3500, 7500, 14000, 28000]
elek_vspel_kwh = [10000, 20000, 40000, 60000, 90000, 150000, 300000]
diel_kwh = [8000, 16000, 32000, 48000, 72000, 120000, 240000]
uren1 = np.arange(0, 24, 1)
kw_normale_oplader = [6652.8, 4752.0, 2851.2, 2280.96, 1900.8, 1425.6, 950.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 19008.0, 19008.0, 18057.6, 17107.2, 16156.8, 14256.0, 9504.0]

# Streamlit App Title
st.title("Vrachtwagens Data Visualization")

# Plot 1: Bar Plot of Electric Building Usage
st.subheader("Bar Plot: Electric Building Usage (MVA)")
plt.figure(figsize=(10,6))
plt.bar(jaren_elek_vspel, elek_gebouw)
plt.axhline(18, color='red', linestyle='--')
plt.xlabel('Years')
plt.ylabel('Electricity Usage in MVA')
plt.title('Electricity Usage (MVA)')
st.pyplot(plt)

# Plot 2: Line Plot for Electric Vehicle Predictions
st.subheader("Line Plot: Electric Vehicle Predictions")
plt.figure(figsize=(10,6))
plt.plot(jaren_elek_vspel, elek_vspel, label='Prediction Line for Electric Trucks')
plt.axhline(30000, color='green')
plt.legend()
plt.xlabel('Years')
plt.ylabel('Number of Electric Trucks')
plt.title('Electric Truck Predictions')
st.pyplot(plt)

# Plot 3: Electric and Diesel Truck Predictions with Goal Line
st.subheader("Line Plot: Electric and Diesel Truck Predictions with Goal Line")
plt.figure(figsize=(10,6))
plt.plot(jaren_elek_vspel, elek_vspel1, label='Electric Truck Prediction')
plt.plot(jaren_elek_vspel, elek_vspel_die, label='Diesel Truck Prediction')
plt.axhline(658, color='green', label='Goal for the Industrial Site')
plt.legend(loc='lower right', fontsize='small')
plt.xlabel('Years')
plt.ylabel('Number of Trucks')
plt.title('Electric vs Diesel Truck Predictions')
st.pyplot(plt)

# Plot 4: Bar Plot with Stacked MVA
st.subheader("Stacked Bar Plot: MVA Usage")
plt.figure(figsize=(10,6))
plt.bar(jaren_elek_vspel, elek_gebouw, label='Building Electricity Usage')
plt.bar(jaren_elek_vspel, elek_vspel_Mva, bottom=elek_gebouw, label='Truck Electricity Usage')
plt.xlabel('Years')
plt.ylabel('Electricity Usage (MVA)')
plt.title('Stacked Bar Plot of Electricity Usage (MVA)')
plt.legend()
st.pyplot(plt)

# Plot 5: Line Plot for kWh and Diesel Usage
st.subheader("Line Plot: kWh and Diesel Usage per Year")
fig, ax1 = plt.subplots()
ax1.plot(jaren_elek_vspel, elek_vspel_kwh, color='blue', label='kWh Usage per Year (Daily)')
ax1.set_xlabel('Years')
ax1.set_ylabel('Electricity in kWh')
ax1.legend(loc='lower left')

ax2 = ax1.twinx()
ax2.plot(jaren_elek_vspel, elek_vspel_die, color='red', label='Diesel Usage per Year (Daily)')
ax2.set_ylabel('Diesel in Liters')
fig.suptitle('Electricity (kWh) vs Diesel Usage per Year (Daily)')
fig.tight_layout()
st.pyplot(fig)

# Plot 6: Stacked Bar Plot of kWh and Diesel (converted to kWh)
st.subheader("Stacked Bar Plot: kWh and Diesel Usage (in kWh)")
x = np.arange(len(jaren_elek_vspel))
fig, ax = plt.subplots(figsize=(10,6))
bars1 = ax.bar(x, elek_vspel_kwh, color='lightblue', label='kWh Usage per Year')
bars2 = ax.bar(x, diel_kwh, bottom=elek_vspel_kwh, color='darkred', label='Diesel Usage per Year (in kWh)')
ax.set_xlabel('Years')
ax.set_ylabel('Usage')
ax.set_title('Stacked Bar Plot of Usage per Year')
ax.set_xticks(x)
ax.set_xticklabels(jaren_elek_vspel)
ax.legend()
st.pyplot(fig)

# Plot 7: kW per Hour for Normal Charger
st.subheader("Line Plot: kW per Hour for Normal Charger")
plt.figure(figsize=(10,6))
plt.plot(uren1, kw_normale_oplader, marker='o', color='b', linestyle='-')
plt.xlabel('Hours')
plt.ylabel('kW based on Normal Charger')
plt.title('kW per Hour for Normal Charger')
plt.grid(True)
plt.tight_layout()
st.pyplot(plt)

