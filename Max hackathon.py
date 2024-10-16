#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Laad de datasets
verbruik_data = pd.read_csv(r"C:\Users\maxde\OneDrive\Documenten\Minor\Oppervlakte3.csv", sep=';')
verbruik_df = pd.read_csv(r"C:\Users\maxde\OneDrive\Documenten\Minor\Energiekentallen_utiliteitsbouw_dienstensector__oppervlakteklasse.csv", sep=';', encoding='ISO-8859-1')

# Verwijder onbenutte kolommen
verbruik_data = verbruik_data[['bedrijf', 'oppervlakte', 'koeling', 'Sector', "Sector-koeling"]]

# Verwijder spaties uit kolomnamen
verbruik_df.columns = verbruik_df.columns.str.strip()

# Functie om verbruik te berekenen
def bereken_verbruik(verbruik_data, verbruik_df):
    # Maak nieuwe kolommen voor verbruik
    verbruik_data['aardgas_verbruik'] = 0.0
    verbruik_data['elektriciteit_verbruik'] = 0.0
    
    # Loop door elk bedrijf
    for index, row in verbruik_data.iterrows():
        sector_koeling = row['Sector-koeling']
        oppervlakte = row['oppervlakte']
        
        # Zoek de juiste rij in verbruik_df
        verbruik_row = verbruik_df[verbruik_df['Onderwerp'] == sector_koeling]
        
        # Print een waarschuwing als er geen overeenkomende sector is
        if verbruik_row.empty:
            print(f"No match found for sector: {sector_koeling} in row {index}")
            continue  # Ga naar de volgende iteratie
        
        # Bepaal het verbruik voor aardgas en elektriciteit op basis van oppervlakte
        for i in range(1, 7):  # Er zijn 6 kolommen voor aardgasverbruik
            kolom_aardgas = f'Gemiddeld aardgasverbruik.{i}'
            kolom_electriciteit = f'Gemiddeld elektriciteitsverbruik.{i}'
            
            # Controleer en converteer de aardgaswaarden
            aardgas_value = verbruik_row[kolom_aardgas].values[0]
            if isinstance(aardgas_value, str):
                aardgas_value = aardgas_value.replace(',', '.')  # vervang ',' door '.'
            
            if aardgas_value not in ['.', '']:
                aardgas_per_m2 = float(aardgas_value)
                # Bepaal het verbruik op basis van oppervlakte
                if oppervlakte < 250:
                    verbruik_data.at[index, 'aardgas_verbruik'] += aardgas_per_m2 * oppervlakte
                elif oppervlakte < 500:
                    verbruik_data.at[index, 'aardgas_verbruik'] += aardgas_per_m2 * oppervlakte
                elif oppervlakte < 1000:
                    verbruik_data.at[index, 'aardgas_verbruik'] += aardgas_per_m2 * oppervlakte
                elif oppervlakte < 2500:
                    verbruik_data.at[index, 'aardgas_verbruik'] += aardgas_per_m2 * oppervlakte
                elif oppervlakte < 5000:
                    verbruik_data.at[index, 'aardgas_verbruik'] += aardgas_per_m2 * oppervlakte
                else:
                    verbruik_data.at[index, 'aardgas_verbruik'] += aardgas_per_m2 * oppervlakte

        for j in range(1, 7):  # Er zijn 6 kolommen voor elektriciteitsverbruik
            elektriciteit_value = verbruik_row[kolom_electriciteit].values[0]
            if isinstance(elektriciteit_value, str):
                elektriciteit_value = elektriciteit_value.replace(',', '.')  # vervang ',' door '.'
            
            if elektriciteit_value not in ['.', '']:
                elektriciteit_per_m2 = float(elektriciteit_value)
                # Bepaal het verbruik op basis van oppervlakte
                if oppervlakte < 250:
                    verbruik_data.at[index, 'elektriciteit_verbruik'] += elektriciteit_per_m2 * oppervlakte
                elif oppervlakte < 500:
                    verbruik_data.at[index, 'elektriciteit_verbruik'] += elektriciteit_per_m2 * oppervlakte
                elif oppervlakte < 1000:
                    verbruik_data.at[index, 'elektriciteit_verbruik'] += elektriciteit_per_m2 * oppervlakte
                elif oppervlakte < 2500:
                    verbruik_data.at[index, 'elektriciteit_verbruik'] += elektriciteit_per_m2 * oppervlakte
                elif oppervlakte < 5000:
                    verbruik_data.at[index, 'elektriciteit_verbruik'] += elektriciteit_per_m2 * oppervlakte
                else:
                    verbruik_data.at[index, 'elektriciteit_verbruik'] += elektriciteit_per_m2 * oppervlakte

    return verbruik_data

# Roep de functie aan
verbruik_data = bereken_verbruik(verbruik_data, verbruik_df)

# Bekijk de resultaten
print(verbruik_data[['bedrijf', 'oppervlakte', 'aardgas_verbruik', 'elektriciteit_verbruik']])


# In[5]:


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


# In[3]:


import pandas as pd

# Laad de datasets
verbruik_data = pd.read_csv(r"C:\Users\maxde\OneDrive\Documenten\Minor\Oppervlakte3.csv", sep=';')
verbruik_df = pd.read_csv(r"C:\Users\maxde\OneDrive\Documenten\Minor\Energiekentallen_utiliteitsbouw_dienstensector__oppervlakteklasse.csv", sep=';', encoding='ISO-8859-1')

# Verwijder onbenutte kolommen
verbruik_data = verbruik_data[['bedrijf', 'oppervlakte', 'koeling', 'Sector', "Sector-koeling"]]

# Verwijder spaties uit kolomnamen
verbruik_df.columns = verbruik_df.columns.str.strip()


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
            print(f"Sector/koeling combinatie niet gevonden voor bedrijf in rij {index}")
            continue
        
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

# Roep de functie aan
verbruik_data = bereken_verbruik_met_dict(verbruik_data)

verbruik_data["aardgas_verbruik_per_dag"] = verbruik_data["aardgas_verbruik"]/365
verbruik_data["elektriciteit_verbruik_per_dag"] = verbruik_data["elektriciteit_verbruik"]/365

# Bekijk de resultaten
print(verbruik_data[['bedrijf', 'oppervlakte', 'aardgas_verbruik', 'elektriciteit_verbruik', "aardgas_verbruik_per_dag", "elektriciteit_verbruik_per_dag"]])

verbruik_data["aardgas_verbruik_naar_kWh"] = verbruik_data["aardgas_verbruik"] * 10
verbruik_data["aardgas_verbruik_per_dag_naar_kWh"] = verbruik_data["aardgas_verbruik_per_dag"] * 10


# Bekijk de resultaten
# print(verbruik_data[['bedrijf', 'oppervlakte', 'aardgas_verbruik', 'elektriciteit_verbruik', "aardgas_verbruik_per_dag", "elektriciteit_verbruik_per_dag"]])
print(verbruik_data[["aardgas_verbruik","aardgas_verbruik_per_dag","aardgas_verbruik_naar_kWh","aardgas_verbruik_per_dag_naar_kWh", 'elektriciteit_verbruik']])

# Bereken de som van de opgegeven kolommen
som_verbruik = verbruik_data[["aardgas_verbruik", "aardgas_verbruik_per_dag", 
                               "aardgas_verbruik_naar_kWh", "aardgas_verbruik_per_dag_naar_kWh", 
                               'elektriciteit_verbruik']].sum()

# Print de som
print("\nSom van de verbruik kolommen:")
print(som_verbruik)




# Definities
start_year = 2022
end_year = 2040
initial_area = 370_000  # m²
increase_rate = 11_111.11  # m² per jaar
initial_energy_use = 22_103_475  # kWh per jaar
avg_energy_per_m2 = 123.83  # kWh/m²

# Lijsten voor jaren, oppervlakte en totaal energieverbruik
years = list(range(start_year, end_year + 1))
areas = []
total_energy = []

# Berekeningen
for year in years:
    area = initial_area + increase_rate * (year - start_year)
    total_energy_use = initial_energy_use + (increase_rate * (year - start_year)) * avg_energy_per_m2
    areas.append(area)
    total_energy.append(total_energy_use)

# Creëer een DataFrame
results_df = pd.DataFrame({
    'Jaar': years,
    'Oppervlakte (m²)': areas,
    'Totaal Energieverbruik (kWh)': total_energy
})

# Weergave van de resultaten
print(results_df)





import pandas as pd

# Laad de datasets
verbruik_data = pd.read_csv(r"C:\Users\maxde\OneDrive\Documenten\Minor\Oppervlakte4.csv", sep=';', encoding='ISO-8859-1')
verbruik_df = pd.read_csv(r"C:\Users\maxde\OneDrive\Documenten\Minor\Energiekentallen_utiliteitsbouw_dienstensector__oppervlakteklasse.csv", sep=';', encoding='ISO-8859-1')

# Verwijder onbenutte kolommen
verbruik_data = verbruik_data[['bedrijf', 'oppervlakte', 'koeling', 'Sector', "Sector-koeling"]]

# Verwijder spaties uit kolomnamen
verbruik_df.columns = verbruik_df.columns.str.strip()

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
            print(f"Sector/koeling combinatie niet gevonden voor bedrijf in rij {index}")
            continue
        
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

# Roep de functie aan
verbruik_data = bereken_verbruik_met_dict(verbruik_data)

verbruik_data["aardgas_verbruik_per_dag"] = verbruik_data["aardgas_verbruik"] / 365
verbruik_data["elektriciteit_verbruik_per_dag"] = verbruik_data["elektriciteit_verbruik"] / 365

verbruik_data["aardgas_verbruik_naar_kWh"] = verbruik_data["aardgas_verbruik"] * 10
verbruik_data["aardgas_verbruik_per_dag_naar_kWh"] = verbruik_data["aardgas_verbruik_per_dag"] * 10

# Bekijk de resultaten
print(verbruik_data[["aardgas_verbruik", "aardgas_verbruik_per_dag", "aardgas_verbruik_naar_kWh", "aardgas_verbruik_per_dag_naar_kWh", 'elektriciteit_verbruik', "elektriciteit_verbruik_per_dag"]])

# Bereken de som van de opgegeven kolommen
som_verbruik = verbruik_data[["aardgas_verbruik", "aardgas_verbruik_per_dag", 
                               "aardgas_verbruik_naar_kWh", "aardgas_verbruik_per_dag_naar_kWh", 
                               'elektriciteit_verbruik', 'elektriciteit_verbruik_per_dag']].sum()

# Print de som
print("\nSom van de verbruik kolommen:")
print(som_verbruik)




import pandas as pd

# Beginwaarden
start_jaar = 2024
eind_jaar = 2040
begin_oppervlakte = 188.9  # in ha
eind_oppervlakte = 297.7    # in ha

# Specifieke energieverbruik beginwaarde in kWh
begin_energieverbruik = 6.274866e+06 + 4.899346e+06  # Totaal energieverbruik in het startjaar

# Jaarlijkse groei in oppervlakte
jaarlijkse_groei = (eind_oppervlakte - begin_oppervlakte) / (eind_jaar - start_jaar)

# Bereken energieverbruik in het startjaar per m², gebaseerd op het beginoppervlakte
energie_per_m2_startjaar = begin_energieverbruik / (begin_oppervlakte * 1e4)  # kWh/m²

# Maak lijsten voor jaren, oppervlaktes en energieverbruik
jaren = list(range(start_jaar, eind_jaar + 1))
oppervlaktes = []
energieverbruik = []

# Bereken de oppervlakte en het energieverbruik voor elk jaar
for jaar in jaren:
    oppervlakte = begin_oppervlakte + jaarlijkse_groei * (jaar - start_jaar)
    energie = energie_per_m2_startjaar * oppervlakte * 1e4  # Energieverbruik aangepast aan oppervlaktegroei
    
    oppervlaktes.append(oppervlakte * 1e4)  # Oppervlakte omrekenen naar m²
    energieverbruik.append(energie)

# Maak een DataFrame
data = {
    'Jaar': jaren,
    'Oppervlakte (m²)': oppervlaktes,
    'Totaal Energieverbruik (kWh)': energieverbruik
}

df = pd.DataFrame(data)

# Print de DataFrame
print(df)
