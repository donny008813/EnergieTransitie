import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

# Laad de datasets
url_load_csv = 'https://raw.githubusercontent.com/donny008813/EnergieTransitie/main/monthly_hourly_load_values_2023.csv'
url_opp_csv = 'https://raw.githubusercontent.com/donny008813/EnergieTransitie/main/Oppervlakte3.csv'
verbruik_data = pd.read_csv(url_opp_csv, sep=';')
data = pd.read_csv(url_load_csv, sep = '\t')

# Functie om verbruik te berekenen met dictionaries
def bereken_verbruik_met_dict(verbruik_data):
    for index, row in verbruik_data.iterrows():
        sector = row['Sector']
        koeling = row['koeling']
        oppervlakte = row['oppervlakte']

        # Selecteer de juiste dictionary op basis van sector en koeling
        if sector == 'Detailhandel' and koeling == 'Ja':
            dict_gas = dict_gas_Detailhandel_met_koeling
            dict_ele = dict_ele_Detailhandel_met_koeling
        elif sector == 'Detailhandel' and koeling == 'Nee':
            dict_gas = dict_gas_Detailhandel_zonder_koeling
            dict_ele = dict_ele_Detailhandel_zonder_koeling
        elif sector == 'Groothandel' and koeling == 'Ja':
            dict_gas = dict_gas_Groothandel_met_koeling
            dict_ele = dict_ele_Groothandel_met_koeling
        elif sector == 'Groothandel' and koeling == 'Nee':
            dict_gas = dict_gas_Groothandel_zonder_koeling
            dict_ele = dict_ele_Groothandel_zonder_koeling
        else:
            dict_gas = dict_gas_Groothandel_zonder_koeling
            dict_ele = dict_ele_Groothandel_zonder_koeling

        # Bepaal de oppervlakteklasse
        if oppervlakte < 250:
            oppervlakte_klasse = "0 tot 250 m²"
        elif oppervlakte < 500:
            oppervlakte_klasse = "250 tot 500 m²"
        elif oppervlakte < 1000:
            oppervlakte_klasse = "500 tot 1 000 m²"
        elif oppervlakte < 2500:
            oppervlakte_klasse = "1 000 tot 2 500 m²"
        elif oppervlakte < 5000:
            oppervlakte_klasse = "2 500 tot 5 000 m²"
        elif oppervlakte < 10000:
            oppervlakte_klasse = "5 000 tot 10 000 m²"
        else:
            oppervlakte_klasse = "10 000 tot 25 000 m²"

        # Haal verbruikscijfers op uit de dictionaries
        aardgas_per_m2 = dict_gas.get(oppervlakte_klasse, 0)
        elektriciteit_per_m2 = dict_ele.get(oppervlakte_klasse, 0)

        # Bereken het totale verbruik
        if aardgas_per_m2 is not None:
            verbruik_data.at[index, 'aardgas_verbruik'] = aardgas_per_m2 * oppervlakte
        if elektriciteit_per_m2 is not None:
            verbruik_data.at[index, 'elektriciteit_verbruik'] = elektriciteit_per_m2 * oppervlakte

    return verbruik_data

# Verwijder onbenutte kolommen
verbruik_data = verbruik_data[['bedrijf', 'oppervlakte', 'koeling', 'Sector', "Sector-koeling"]]

# Dictionaries voor gas en elektriciteitsverbruik per sector/koeling
dict_gas_Detailhandel_met_koeling = {
    "0 tot 250 m²": 18.7,
    "250 tot 500 m²": 17.2,
    "500 tot 1 000 m²": 13.7,
    "1 000 tot 2 500 m²": 11.1,
    "2 500 tot 5 000 m²": 7.3,
    "5 000 tot 10 000 m²": None,
    "10 000 tot 25 000 m²": None
}
dict_ele_Detailhandel_met_koeling = {
    "0 tot 250 m²": 231.8,
    "250 tot 500 m²": 174.8,
    "500 tot 1 000 m²": 243.6,
    "1 000 tot 2 500 m²": 279.7,
    "2 500 tot 5 000 m²": 201.8,
    "5 000 tot 10 000 m²": None,
    "10 000 tot 25 000 m²": None
}
dict_gas_Detailhandel_zonder_koeling = {
    "0 tot 250 m²": 17,
    "250 tot 500 m²": 11.9,
    "500 tot 1 000 m²": 8.8,
    "1 000 tot 2 500 m²": 6.9,
    "2 500 tot 5 000 m²": 6.2,
    "5 000 tot 10 000 m²": 5.8,
    "10 000 tot 25 000 m²": 6.4
}
dict_ele_Detailhandel_zonder_koeling = {
    "0 tot 250 m²": 105.2,
    "250 tot 500 m²": 84.8,
    "500 tot 1 000 m²": 70.6,
    "1 000 tot 2 500 m²": 76.1,
    "2 500 tot 5 000 m²": 70,
    "5 000 tot 10 000 m²": 64.7,
    "10 000 tot 25 000 m²": 74.1
}
dict_gas_Groothandel_met_koeling = {
    "0 tot 250 m²": 18.1,
    "250 tot 500 m²": 12.3,
    "500 tot 1 000 m²": 9,
    "1 000 tot 2 500 m²": 8.2,
    "2 500 tot 5 000 m²": 7,
    "5 000 tot 10 000 m²": None,
    "10 000 tot 25 000 m²": None
}
dict_ele_Groothandel_met_koeling = {
    "0 tot 250 m²": 95.6,
    "250 tot 500 m²": 83.8,
    "500 tot 1 000 m²": 126.2,
    "1 000 tot 2 500 m²": 178.9,
    "2 500 tot 5 000 m²": 139.5,
    "5 000 tot 10 000 m²": 173.8,
    "10 000 tot 25 000 m²": None
}
dict_gas_Groothandel_zonder_koeling = {
    "0 tot 250 m²": 16.6,
    "250 tot 500 m²": 11.9,
    "500 tot 1 000 m²": 8.9,
    "1 000 tot 2 500 m²": 7.3,
    "2 500 tot 5 000 m²": 6.7,
    "5 000 tot 10 000 m²": 6,
    "10 000 tot 25 000 m²": 6.6
}
dict_ele_Groothandel_zonder_koeling = {
    "0 tot 250 m²": 64.9,
    "250 tot 500 m²": 50.9,
    "500 tot 1 000 m²": 46.1,
    "1 000 tot 2 500 m²": 47.3,
    "2 500 tot 5 000 m²": 50,
    "5 000 tot 10 000 m²": 53.7,
    "10 000 tot 25 000 m²": 69.8
}

# Roep de functie aan
verbruik_data = bereken_verbruik_met_dict(verbruik_data)

detailhandel_met_koeling_data = verbruik_data[verbruik_data['Sector-koeling'] == 'Detailhandel met koeling']
detailhandel_zonder_koeling_data = verbruik_data[verbruik_data['Sector-koeling'] == 'Detailhandel zonder koeling']
groothandel_met_koeling_data = verbruik_data[verbruik_data['Sector-koeling'] == 'Groothandel met koeling']
groothandel_zonder_koeling_data = verbruik_data[verbruik_data['Sector-koeling'] == 'Groothandel zonder koeling']
transport_data = verbruik_data[verbruik_data['Sector'] == 'Transport / logistiek']

verbruik_data["aardgas_verbruik_naar_kWh"] = verbruik_data["aardgas_verbruik"] * 10

# Bereken de som van de opgegeven kolommen
som_verbruik = verbruik_data[["aardgas_verbruik", "aardgas_verbruik_naar_kWh", 'elektriciteit_verbruik']].sum()

# Print de som
#print("\nSom van de verbruik kolommen:")
#print(som_verbruik)

gebied_verbruik_jaar = verbruik_data['elektriciteit_verbruik'].sum()
gebied_gas_verbruik_jaar = verbruik_data['aardgas_verbruik_naar_kWh'].sum()
detailhandel_koeling_jaar = detailhandel_met_koeling_data['elektriciteit_verbruik'].sum()
detailhandel_jaar = detailhandel_zonder_koeling_data['elektriciteit_verbruik'].sum()
groothandel_koeling_jaar = groothandel_met_koeling_data['elektriciteit_verbruik'].sum()
groothandel_jaar = groothandel_zonder_koeling_data['elektriciteit_verbruik'].sum()
transport_jaar = transport_data['elektriciteit_verbruik'].sum()

gebied_gas_verbuik_uur = gebied_gas_verbruik_jaar / (365 * 24)
gebied_diesel_uur = 2147023.2 / (365 * 24)

data_nl = data[data['CountryCode'] == 'NL']

# Step 3: Calculate the country's total yearly energy consumption
country_yearly_consumption = data_nl['Value'].sum()  # Total kWh per year for the country
country_yearly_consumption_Twh = country_yearly_consumption / 1000000
country_yearly_consumption_kwh = country_yearly_consumption_Twh * 1000000000
#print('jaarlijks verbruik', country_yearly_consumption)
#print('jaarlijks verbruik Twh', country_yearly_consumption_Twh)
#print('jaarlijks verbruik kwh', country_yearly_consumption_kwh)

# Step 4: Calculate the scaling factor building_yearly_consumption
scaling_factor = gebied_verbruik_jaar / country_yearly_consumption_kwh

factor_detail_koeling = detailhandel_koeling_jaar / country_yearly_consumption_kwh
factor_detail = detailhandel_jaar / country_yearly_consumption_kwh
factor_groot_koeling = groothandel_koeling_jaar / country_yearly_consumption_kwh
factor_groot = groothandel_jaar / country_yearly_consumption_kwh
factor_trans = transport_jaar / country_yearly_consumption_kwh

data_nl['energie verbruik gebouw'] = (data_nl['Value'] * 1000) * scaling_factor

data_nl['energie verbruik detailhandel koeling'] = (data_nl['Value'] * 1000) * factor_detail_koeling
data_nl['energie verbruik detailhandel'] = (data_nl['Value'] * 1000) * factor_detail
data_nl['energie verbruik groothandel koeling'] = (data_nl['Value'] * 1000) * factor_groot_koeling
data_nl['energie verbruik groothandel'] = (data_nl['Value'] * 1000) * factor_groot
data_nl['energie verbruik transport'] = (data_nl['Value'] * 1000) * factor_trans

data_nl['energie verbruik overig'] = (data_nl['energie verbruik gebouw'] - data_nl['energie verbruik detailhandel koeling'] - data_nl['energie verbruik detailhandel']
                                      - data_nl['energie verbruik groothandel koeling'] - data_nl['energie verbruik groothandel'] - data_nl['energie verbruik transport'])

# Voeg gasverbruik in Kwh toe
data_nl['gas verbruik gebouw'] = gebied_gas_verbuik_uur
data_nl['diesel verbruik'] = gebied_diesel_uur

data_nl['DateUTC'] = pd.to_datetime(data_nl['DateUTC'], format="%d-%m-%Y %H:%M")

data_nl['Uur'] = data_nl['DateUTC'].dt.hour
data_nl['Uur'] = data_nl['Uur'].astype(int)
data_nl['Dag_nummer'] = data_nl['DateUTC'].dt.day
data_nl['Dag_nummer'] = data_nl['Dag_nummer'].astype(int)
data_nl['Maand_nummer'] = data_nl['DateUTC'].dt.month
data_nl['Maand_nummer'] = data_nl['Maand_nummer'].astype(int)

st.set_page_config(page_title="Energie verbruik gebouwen")
st.markdown("# Energie verbruik gebouwen")
st.sidebar.header("Energie verbruik gebouwen")

# Line plot using seaborn to visualize energy over time
plt.figure(figsize=(14,6))
sns.lineplot(data=data_nl, x='DateUTC', y='energie verbruik gebouw', linewidth=1)
plt.title('Energy Consumption Per Hour in 2023')
plt.xlabel('Datetime')
plt.ylabel('Energy (kWh)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 1: Aggregate the data by day (sum energy consumption for each day)
data_nl['date'] = data_nl['DateUTC'].dt.date  # Extract just the date (without time)
daily_energy = data_nl.groupby('date')['energie verbruik gebouw'].sum().reset_index()

# Step 2: Aggregate the data by month (sum energy consumption for each month)
data_nl['Maand'] = data_nl['DateUTC'].dt.to_period('M')  # Extract the month (without specific day)
monthly_energy = data_nl.groupby('Maand')['energie verbruik gebouw'].sum().reset_index()

# Convert 'month' to string format for plotting
monthly_energy['Maand'] = monthly_energy['Maand'].dt.to_timestamp()

# Step 3: Plot the energy consumption for each day over the year
plt.figure(figsize=(14, 6))
sns.lineplot(data=daily_energy, x='date', y='energie verbruik gebouw', linewidth=1.5)
plt.title('Energy Consumption Per Day Over the Year (2023)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Energy (kWh)', fontsize=12)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()

# Step 4: Plot the energy consumption for each month over the year
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_energy, x='Maand', y='energie verbruik gebouw', linewidth=2)
plt.title('Energy Consumption Per Month Over the Year (2023)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Total Energy (kWh)', fontsize=12)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.grid(True)
plt.tight_layout()
plt.show()

# Setting the datetime as the index
data_nl.set_index('DateUTC', inplace=True)

# Plotting the stacked area plot
plt.figure(figsize=(14, 8))

# Creating the stacked area plot
plt.stackplot(data_nl.index, data_nl['energie verbruik detailhandel koeling'],
              data_nl['energie verbruik detailhandel'],
              data_nl['energie verbruik groothandel koeling'], data_nl['energie verbruik groothandel'],
              data_nl['energie verbruik transport'], data_nl['gas verbruik gebouw'], data_nl['diesel verbruik'],
              labels=['Detailhandel koeling (kWh)','Detailhandel zonder koeling (kWh)','Groothandel koeling (kWh)'
                  ,'Groothandel zonder koeling (kWh)', 'Transport (kWh)', 'Gas Usage (kWh)', 'Brandstof (kWh)'],
              alpha=0.7)

# Customizing the plot
plt.title('Hourly Energy and Gas Usage in 2023', fontsize=16)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Usage', fontsize=14)
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.legend(loc='upper left')
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()

# Group by day and sum the values
print(data_nl['Dag_nummer'])
daily_data = data_nl.groupby('Dag_nummer')[['energie verbruik detailhandel koeling',
                                            'energie verbruik detailhandel',
                                            'energie verbruik groothandel koeling',
                                            'energie verbruik groothandel',
                                            'energie verbruik transport',
                                            'gas verbruik gebouw',
                                            'diesel verbruik']].sum().reset_index()

# Display the daily aggregated data
print(daily_data)

# Group by month and sum the values
monthly_data = data_nl.groupby('Maand_nummer')[['energie verbruik detailhandel koeling',
                                            'energie verbruik detailhandel',
                                            'energie verbruik groothandel koeling',
                                            'energie verbruik groothandel',
                                            'energie verbruik transport',
                                            'gas verbruik gebouw',
                                            'diesel verbruik']].sum().reset_index()

# Display the monthly aggregated data
print(monthly_data)

# Group by hour and sum the values
hourly_data = data_nl.groupby('Uur')[['energie verbruik detailhandel koeling',
                                            'energie verbruik detailhandel',
                                            'energie verbruik groothandel koeling',
                                            'energie verbruik groothandel',
                                            'energie verbruik transport',
                                            'gas verbruik gebouw',
                                      'diesel verbruik']].sum().reset_index()

# Plotting the daily patterns
plt.figure(figsize=(14, 8))

# Creating the stacked area plot for daily data
plt.stackplot(daily_data['Dag_nummer'], daily_data['energie verbruik detailhandel koeling'],
              daily_data['energie verbruik detailhandel'],
              daily_data['energie verbruik groothandel koeling'], daily_data['energie verbruik groothandel'],
              daily_data['energie verbruik transport'], daily_data['gas verbruik gebouw'], daily_data['diesel verbruik'],
              labels=['Detailhandel koeling (kWh)','Detailhandel zonder koeling (kWh)','Groothandel koeling (kWh)'
                  ,'Groothandel zonder koeling (kWh)', 'Transport (kWh)', 'Gas Usage (kWh)', 'Brandstof (kWh)'],
              alpha=0.7)

# Customizing the plot
plt.title('Daily Energy and Gas Usage', fontsize=16)
plt.xlabel('Day of the Month', fontsize=14)
plt.ylabel('Usage', fontsize=14)
plt.xticks(daily_data['Dag_nummer'])  # Show each day on the x-axis
plt.legend(loc='upper left')
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()

# Plotting the monthly patterns
plt.figure(figsize=(14, 8))

# Creating the stacked area plot for monthly data
plt.stackplot(monthly_data['Maand_nummer'], monthly_data['energie verbruik detailhandel koeling'],
              monthly_data['energie verbruik detailhandel'],
              monthly_data['energie verbruik groothandel koeling'], monthly_data['energie verbruik groothandel'],
              monthly_data['energie verbruik transport'], monthly_data['gas verbruik gebouw'],
              labels=['Detailhandel koeling (kWh)','Detailhandel zonder koeling (kWh)','Groothandel koeling (kWh)'
                  ,'Groothandel zonder koeling (kWh)', 'Transport (kWh)', 'Gas Usage (kWh)', 'Brandstof (kWh)'],
              alpha=0.7)

# Customizing the plot
plt.title('Monthly Energy and Gas Usage', fontsize=16)
plt.xlabel('Month', fontsize=14)
plt.ylabel('Usage', fontsize=14)
plt.xticks(monthly_data['Maand_nummer'])  # Show each month on the x-axis
plt.legend(loc='upper left')
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()

# Plotting the hourly data
plt.figure(figsize=(14, 8))

# Creating a stacked area plot for hourly data
plt.stackplot(hourly_data['Uur'], hourly_data['energie verbruik detailhandel koeling'],
              hourly_data['energie verbruik detailhandel'],
              hourly_data['energie verbruik groothandel koeling'], hourly_data['energie verbruik groothandel'],
              hourly_data['energie verbruik transport'], hourly_data['gas verbruik gebouw'],
              labels=['Detailhandel koeling (kWh)','Detailhandel zonder koeling (kWh)','Groothandel koeling (kWh)'
                  ,'Groothandel zonder koeling (kWh)', 'Transport (kWh)', 'Gas Usage (kWh)', 'Brandstof (kWh)'],
              alpha=0.7)

# Customizing the plot
plt.title('Hourly Energy and Gas Usage', fontsize=16)
plt.xlabel('Hour of the Day', fontsize=14)
plt.ylabel('Usage', fontsize=14)
plt.xticks(hourly_data['Uur'])  # Show each hour on the x-axis
plt.legend(loc='upper left')
plt.grid(True)

# Show plot
plt.tight_layout()
plt.show()
