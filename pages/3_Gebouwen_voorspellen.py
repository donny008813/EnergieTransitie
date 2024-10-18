import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url_load_csv = 'https://raw.githubusercontent.com/donny008813/EnergieTransitie/main/monthly_hourly_load_values_2023.csv'
url_DFP_csv = 'https://raw.githubusercontent.com/donny008813/EnergieTransitie/main/UitkomstenPythonDutchFreshPort(MetAfrondingEnJuisteGetallen).csv'
data = pd.read_csv(url_load_csv, sep = '\t')
toekomst = pd.read_csv(url_DFP_csv, sep = ';')

data_nl = data[data['CountryCode'] == 'NL']

# Gebied verbruik jaar maken aan de hand van csv voor toekomstige jaren
verbruik_2023 = toekomst['Totaal Energieverbruik (in kWh)'][0]
verbruik_2024 = toekomst['Totaal Energieverbruik (in kWh)'][1]
verbruik_2025 = toekomst['Totaal Energieverbruik (in kWh)'][2]
verbruik_2026 = toekomst['Totaal Energieverbruik (in kWh)'][3]
verbruik_2027 = toekomst['Totaal Energieverbruik (in kWh)'][4]
verbruik_2028 = toekomst['Totaal Energieverbruik (in kWh)'][5]
verbruik_2029 = toekomst['Totaal Energieverbruik (in kWh)'][6]
verbruik_2030 = toekomst['Totaal Energieverbruik (in kWh)'][7]

country_yearly_consumption = data_nl['Value'].sum()  # Total kWh per year for the country
country_yearly_consumption_Twh = country_yearly_consumption / 1000000
country_yearly_consumption_kwh = country_yearly_consumption_Twh * 1000000000

factor_2023 = verbruik_2023 / country_yearly_consumption_kwh
factor_2024 = verbruik_2024 / country_yearly_consumption_kwh
factor_2025 = verbruik_2025 / country_yearly_consumption_kwh
factor_2026 = verbruik_2026 / country_yearly_consumption_kwh
factor_2027 = verbruik_2027 / country_yearly_consumption_kwh
factor_2028 = verbruik_2028 / country_yearly_consumption_kwh
factor_2029 = verbruik_2029 / country_yearly_consumption_kwh
factor_2030 = verbruik_2030 / country_yearly_consumption_kwh

data_nl['2023'] = (data_nl['Value'] * 1000) * factor_2023
data_nl['2024'] = (data_nl['Value'] * 1000) * factor_2024
data_nl['2025'] = (data_nl['Value'] * 1000) * factor_2025
data_nl['2026'] = (data_nl['Value'] * 1000) * factor_2026
data_nl['2027'] = (data_nl['Value'] * 1000) * factor_2027
data_nl['2028'] = (data_nl['Value'] * 1000) * factor_2028
data_nl['2029'] = (data_nl['Value'] * 1000) * factor_2029
data_nl['2030'] = (data_nl['Value'] * 1000) * factor_2030

data_nl['DateUTC'] = pd.to_datetime(data_nl['DateUTC'], format="%d-%m-%Y %H:%M")

data_nl['Uur'] = data_nl['DateUTC'].dt.hour
data_nl['Uur'] = data_nl['Uur'].astype(int)
data_nl['Dag_nummer'] = data_nl['DateUTC'].dt.day
data_nl['Dag_nummer'] = data_nl['Dag_nummer'].astype(int)
data_nl['Maand_nummer'] = data_nl['DateUTC'].dt.month
data_nl['Maand_nummer'] = data_nl['Maand_nummer'].astype(int)

# Function to create the energy consumption plots
def plot_energy_consumption(data_nl, time_frame='hourly'):
    fig, axes = plt.subplots(4, 2, figsize=(15, 10))

    if time_frame == 'hourly':
        axes[0, 0].plot(data_nl['2023'], color='steelblue', alpha=0.7)
        axes[0, 0].set_title('Energy Consumption in 2023')
        axes[0, 0].set_xlabel('Hour of Year')
        axes[0, 0].set_ylabel('Energy (KWh)')
        axes[0, 0].set_xticks([])
        axes[0, 0].grid(True)

        axes[0, 1].plot(data_nl['2024'], color='steelblue', alpha=0.7)
        axes[0, 1].set_title('Energy Consumption in 2024')
        axes[0, 1].set_xlabel('Hour of Year')
        axes[0, 1].set_ylabel('Energy (KWh)')
        axes[0, 1].set_xticks([])
        axes[0, 1].grid(True)

        axes[1, 0].plot(data_nl['2025'], color='steelblue', alpha=0.7)
        axes[1, 0].set_title('Energy Consumption in 2025')
        axes[1, 0].set_xlabel('Hour of Year')
        axes[1, 0].set_ylabel('Energy (KWh)')
        axes[1, 0].set_xticks([])
        axes[1, 0].grid(True)

        axes[1, 1].plot(data_nl['2026'], color='steelblue', alpha=0.7)
        axes[1, 1].set_title('Energy Consumption in 2026')
        axes[1, 1].set_xlabel('Hour of Year')
        axes[1, 1].set_ylabel('Energy (KWh)')
        axes[1, 1].set_xticks([])
        axes[1, 1].grid(True)

        axes[2, 0].plot(data_nl['2027'], color='steelblue', alpha=0.7)
        axes[2, 0].set_title('Energy Consumption in 2027')
        axes[2, 0].set_xlabel('Hour of Year')
        axes[2, 0].set_ylabel('Energy (KWh)')
        axes[2, 0].set_xticks([])
        axes[2, 0].grid(True)

        axes[2, 1].plot(data_nl['2028'], color='steelblue', alpha=0.7)
        axes[2, 1].set_title('Energy Consumption in 2028')
        axes[2, 1].set_xlabel('Hour of Year')
        axes[2, 1].set_ylabel('Energy (KWh)')
        axes[2, 1].set_xticks([])
        axes[2, 1].grid(True)

        axes[3, 0].plot(data_nl['2029'], color='steelblue', alpha=0.7)
        axes[3, 0].set_title('Energy Consumption in 2029')
        axes[3, 0].set_xlabel('Hour of Year')
        axes[3, 0].set_ylabel('Energy (KWh)')
        axes[3, 0].set_xticks([])
        axes[3, 0].grid(True)

        axes[3, 1].plot(data_nl['2030'], color='steelblue', alpha=0.7)
        axes[3, 1].set_title('Energy Consumption in 2030')
        axes[3, 1].set_xlabel('Hour of Year')
        axes[3, 1].set_ylabel('Energy (KWh)')
        axes[3, 1].set_xticks([])
        axes[3, 1].grid(True)

    elif time_frame == 'daily':
        data_nl['date'] = data_nl['DateUTC'].dt.date  # Extract just the date (without time)
        daily = data_nl.groupby('date')[['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']].sum().reset_index()

        # Plot each year's data manually on specific subplots
        axes[0, 0].plot(daily['2023'], color='steelblue', alpha=0.7)
        axes[0, 0].set_title('Energy Consumption in 2023')
        axes[0, 0].set_xlabel('Day of Year')
        axes[0, 0].set_ylabel('Energy (KWh)')
        axes[0, 0].set_xticks([])
        axes[0, 0].grid(True)

        axes[0, 1].plot(daily['2024'], color='steelblue', alpha=0.7)
        axes[0, 1].set_title('Energy Consumption in 2024')
        axes[0, 1].set_xlabel('Day of Year')
        axes[0, 1].set_ylabel('Energy (KWh)')
        axes[0, 1].set_xticks([])
        axes[0, 1].grid(True)

        axes[1, 0].plot(daily['2025'], color='steelblue', alpha=0.7)
        axes[1, 0].set_title('Energy Consumption in 2025')
        axes[1, 0].set_xlabel('Day of Year')
        axes[1, 0].set_ylabel('Energy (KWh)')
        axes[1, 0].set_xticks([])
        axes[1, 0].grid(True)

        axes[1, 1].plot(daily['2026'], color='steelblue', alpha=0.7)
        axes[1, 1].set_title('Energy Consumption in 2026')
        axes[1, 1].set_xlabel('Day of Year')
        axes[1, 1].set_ylabel('Energy (KWh)')
        axes[1, 1].set_xticks([])
        axes[1, 1].grid(True)

        axes[2, 0].plot(daily['2027'], color='steelblue', alpha=0.7)
        axes[2, 0].set_title('Energy Consumption in 2027')
        axes[2, 0].set_xlabel('Day of Year')
        axes[2, 0].set_ylabel('Energy (KWh)')
        axes[2, 0].set_xticks([])
        axes[2, 0].grid(True)

        axes[2, 1].plot(daily['2028'], color='steelblue', alpha=0.7)
        axes[2, 1].set_title('Energy Consumption in 2028')
        axes[2, 1].set_xlabel('Day of Year')
        axes[2, 1].set_ylabel('Energy (KWh)')
        axes[2, 1].set_xticks([])
        axes[2, 1].grid(True)

        axes[3, 0].plot(daily['2029'], color='steelblue', alpha=0.7)
        axes[3, 0].set_title('Energy Consumption in 2029')
        axes[3, 0].set_xlabel('Day of Year')
        axes[3, 0].set_ylabel('Energy (KWh)')
        axes[3, 0].set_xticks([])
        axes[3, 0].grid(True)

        axes[3, 1].plot(daily['2030'], color='steelblue', alpha=0.7)
        axes[3, 1].set_title('Energy Consumption in 2030')
        axes[3, 1].set_xlabel('Day of Year')
        axes[3, 1].set_ylabel('Energy (KWh)')
        axes[3, 1].set_xticks([])
        axes[3, 1].grid(True)

    elif time_frame == 'monthly':
        data_nl['Maand'] = data_nl['DateUTC'].dt.to_period('M')  # Extract the month (without specific day)
        monthly = data_nl.groupby('Maand')[['2023', '2024', '2025', '2026', '2027', '2028', '2029', '2030']].sum().reset_index()
        
        # Plot each year's data manually on specific subplots
        axes[0, 0].plot(monthly['2023'], color='steelblue', alpha=0.7)
        axes[0, 0].set_title('Energy Consumption in 2023')
        axes[0, 0].set_xlabel('Month of Year')
        axes[0, 0].set_ylabel('Energy (KWh)')
        axes[0, 0].set_xticks([])
        axes[0, 0].grid(True)

        axes[0, 1].plot(monthly['2024'], color='steelblue', alpha=0.7)
        axes[0, 1].set_title('Energy Consumption in 2024')
        axes[0, 1].set_xlabel('Month of Year')
        axes[0, 1].set_ylabel('Energy (KWh)')
        axes[0, 1].set_xticks([])
        axes[0, 1].grid(True)

        axes[1, 0].plot(monthly['2025'], color='steelblue', alpha=0.7)
        axes[1, 0].set_title('Energy Consumption in 2025')
        axes[1, 0].set_xlabel('Month of Year')
        axes[1, 0].set_ylabel('Energy (KWh)')
        axes[1, 0].set_xticks([])
        axes[1, 0].grid(True)

        axes[1, 1].plot(monthly['2026'], color='steelblue', alpha=0.7)
        axes[1, 1].set_title('Energy Consumption in 2026')
        axes[1, 1].set_xlabel('Month of Year')
        axes[1, 1].set_ylabel('Energy (KWh)')
        axes[1, 1].set_xticks([])
        axes[1, 1].grid(True)

        axes[2, 0].plot(monthly['2027'], color='steelblue', alpha=0.7)
        axes[2, 0].set_title('Energy Consumption in 2027')
        axes[2, 0].set_xlabel('Month of Year')
        axes[2, 0].set_ylabel('Energy (KWh)')
        axes[2, 0].set_xticks([])
        axes[2, 0].grid(True)

        axes[2, 1].plot(monthly['2028'], color='steelblue', alpha=0.7)
        axes[2, 1].set_title('Energy Consumption in 2028')
        axes[2, 1].set_xlabel('Month of Year')
        axes[2, 1].set_ylabel('Energy (KWh)')
        axes[2, 1].set_xticks([])
        axes[2, 1].grid(True)

        axes[3, 0].plot(monthly['2029'], color='steelblue', alpha=0.7)
        axes[3, 0].set_title('Energy Consumption in 2029')
        axes[3, 0].set_xlabel('Month of Year')
        axes[3, 0].set_ylabel('Energy (KWh)')
        axes[3, 0].set_xticks([])
        axes[3, 0].grid(True)

        axes[3, 1].plot(monthly['2030'], color='steelblue', alpha=0.7)
        axes[3, 1].set_title('Energy Consumption in 2030')
        axes[3, 1].set_xlabel('Month of Year')
        axes[3, 1].set_ylabel('Energy (KWh)')
        axes[3, 1].set_xticks([])
        axes[3, 1].grid(True)

    # Adjust layout
    plt.tight_layout()
    st.pyplot(fig)  # Display the plot in Streamlit

# Streamlit app layout
st.set_page_config(page_title="Energie verbruik gebouwen voor de toekomst")
st.markdown("# Energie Verbruik Gebouwen Toekomst")
st.sidebar.header("Energie verbruik gebouwen Toekomst")

# Dropdown for time frame selection
time_frame = st.selectbox("Select Time Frame:", ["hourly", "daily", "monthly"])

# Call the plot function with the selected time frame
plot_energy_consumption(data_nl, time_frame)
