import pandas as pd

# Laad de datasets
verbruik_data = pd.read_csv("Oppervlakte3.csv", sep=';')


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

# Bekijk de resultaten
print(verbruik_data[['bedrijf', 'oppervlakte', 'aardgas_verbruik', 'elektriciteit_verbruik', "aardgas_verbruik_per_dag",
                     "elektriciteit_verbruik_per_dag"]])

verbruik_data["aardgas_verbruik_naar_kWh"] = verbruik_data["aardgas_verbruik"] * 10
verbruik_data["aardgas_verbruik_per_dag_naar_kWh"] = verbruik_data["aardgas_verbruik_per_dag"] * 10

# Bekijk de resultaten
# print(verbruik_data[['bedrijf', 'oppervlakte', 'aardgas_verbruik', 'elektriciteit_verbruik', "aardgas_verbruik_per_dag", "elektriciteit_verbruik_per_dag"]])
print(verbruik_data[["aardgas_verbruik", "aardgas_verbruik_per_dag", "aardgas_verbruik_naar_kWh",
                     "aardgas_verbruik_per_dag_naar_kWh", 'elektriciteit_verbruik']])

# Bereken de som van de opgegeven kolommen
som_verbruik = verbruik_data[["aardgas_verbruik", "aardgas_verbruik_per_dag",
                              "aardgas_verbruik_naar_kWh", "aardgas_verbruik_per_dag_naar_kWh",
                              'elektriciteit_verbruik']].sum()

# Print de som
print("\nSom van de verbruik kolommen:")
print(som_verbruik)