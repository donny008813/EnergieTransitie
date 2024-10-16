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


# In[ ]:





# In[ ]:





# In[ ]:




