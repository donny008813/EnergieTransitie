import streamlit as st

# Ele consumption details for retail with cooling based on area
dict_ele_Detailhandel_met_koeling = {
    "0 tot 250 m²": 231.8,
    "250 tot 500 m²": 174.8,
    "500 tot 1 000 m²": 243.6,
    "1 000 tot 2 500 m²": 279.7,
    "2 500 tot 5 000 m²": 201.8,
    "5 000 tot 10 000 m²": None,
    "10 000 tot 25 000 m²": None
}

# Ele consumption details for retail without cooling based on area
dict_ele_Detailhandel_zonder_koeling = {
    "0 tot 250 m²": 105.2,
    "250 tot 500 m²": 84.8,
    "500 tot 1 000 m²": 70.6,
    "1 000 tot 2 500 m²": 76.1,
    "2 500 tot 5 000 m²": 70,
    "5 000 tot 10 000 m²": 64.7,
    "10 000 tot 25 000 m²": 74.1
}

# Ele consumption details for wholesale with cooling based on area
dict_ele_Groothandel_met_koeling = {
    "0 tot 250 m²": 95.6,
    "250 tot 500 m²": 83.8,
    "500 tot 1 000 m²": 126.2,
    "1 000 tot 2 500 m²": 178.9,
    "2 500 tot 5 000 m²": 139.5,
    "5 000 tot 10 000 m²": 173.8,
    "10 000 tot 25 000 m²": None
}

# Ele consumption details for wholesale without cooling based on area
dict_ele_Groothandel_zonder_koeling = {
    "0 tot 250 m²": 64.9,
    "250 tot 500 m²": 50.9,
    "500 tot 1 000 m²": 46.1,
    "1 000 tot 2 500 m²": 47.3,
    "2 500 tot 5 000 m²": 50,
    "5 000 tot 10 000 m²": 53.7,
    "10 000 tot 25 000 m²": 69.8
}

# Function to find gas usage based on area for retail with cooling
def get_energy_usage_with_cooling(area):
    if area <= 250:
        return dict_ele_Detailhandel_met_koeling["0 tot 250 m²"]
    elif 250 < area <= 500:
        return dict_ele_Detailhandel_met_koeling["250 tot 500 m²"]
    elif 500 < area <= 1000:
        return dict_ele_Detailhandel_met_koeling["500 tot 1 000 m²"]
    elif 1000 < area <= 2500:
        return dict_ele_Detailhandel_met_koeling["1 000 tot 2 500 m²"]
    elif 2500 < area <= 5000:
        return dict_ele_Detailhandel_met_koeling["2 500 tot 5 000 m²"]
    elif 5000 < area <= 10000:
        return dict_ele_Detailhandel_met_koeling["5 000 tot 10 000 m²"]
    else:
        return dict_ele_Detailhandel_met_koeling["10 000 tot 25 000 m²"]

# Function to find gas usage based on area for retail without cooling
def get_energy_usage_without_cooling(area):
    if area <= 250:
        return dict_ele_Detailhandel_zonder_koeling["0 tot 250 m²"]
    elif 250 < area <= 500:
        return dict_ele_Detailhandel_zonder_koeling["250 tot 500 m²"]
    elif 500 < area <= 1000:
        return dict_ele_Detailhandel_zonder_koeling["500 tot 1 000 m²"]
    elif 1000 < area <= 2500:
        return dict_ele_Detailhandel_zonder_koeling["1 000 tot 2 500 m²"]
    elif 2500 < area <= 5000:
        return dict_ele_Detailhandel_zonder_koeling["2 500 tot 5 000 m²"]
    elif 5000 < area <= 10000:
        return dict_ele_Detailhandel_zonder_koeling["5 000 tot 10 000 m²"]
    else:
        return dict_ele_Detailhandel_zonder_koeling["10 000 tot 25 000 m²"]

# Function to find gas usage based on area for wholesale with cooling
def get_energy_usage_groothandel_with_cooling(area):
    if area <= 250:
        return dict_ele_Groothandel_met_koeling["0 tot 250 m²"]
    elif 250 < area <= 500:
        return dict_ele_Groothandel_met_koeling["250 tot 500 m²"]
    elif 500 < area <= 1000:
        return dict_ele_Groothandel_met_koeling["500 tot 1 000 m²"]
    elif 1000 < area <= 2500:
        return dict_ele_Groothandel_met_koeling["1 000 tot 2 500 m²"]
    elif 2500 < area <= 5000:
        return dict_ele_Groothandel_met_koeling["2 500 tot 5 000 m²"]
    elif 5000 < area <= 10000:
        return dict_ele_Groothandel_met_koeling["5 000 tot 10 000 m²"]
    else:
        return dict_ele_Groothandel_met_koeling["10 000 tot 25 000 m²"]

# Function to find gas usage based on area for wholesale without cooling
def get_energy_usage_groothandel_without_cooling(area):
    if area <= 250:
        return dict_ele_Groothandel_zonder_koeling["0 tot 250 m²"]
    elif 250 < area <= 500:
        return dict_ele_Groothandel_zonder_koeling["250 tot 500 m²"]
    elif 500 < area <= 1000:
        return dict_ele_Groothandel_zonder_koeling["500 tot 1 000 m²"]
    elif 1000 < area <= 2500:
        return dict_ele_Groothandel_zonder_koeling["1 000 tot 2 500 m²"]
    elif 2500 < area <= 5000:
        return dict_ele_Groothandel_zonder_koeling["2 500 tot 5 000 m²"]
    elif 5000 < area <= 10000:
        return dict_ele_Groothandel_zonder_koeling["5 000 tot 10 000 m²"]
    else:
        return dict_ele_Groothandel_zonder_koeling["10 000 tot 25 000 m²"]

# Function to calculate based on area and business type
def calculate_value(area, business_type):
    if business_type == "Detailhandel met Koeling":
        energy_usage = get_energy_usage_with_cooling(area)
        if energy_usage is None:
            return "Energy usage data not available for areas larger than 5000 m²."
        else:
            total_energy_usage = area * energy_usage
            return f"Total energy usage for {area} m²: {total_energy_usage:.2f} m³"
    elif business_type == "Detailhandel zonder Koeling":
        energy_usage = get_energy_usage_without_cooling(area)
        if energy_usage is None:
            return "Energy usage data not available for areas larger than 10,000 m²."
        else:
            total_energy_usage = area * energy_usage
            return f"Total energy usage for {area} m²: {total_energy_usage:.2f} m³"
    elif business_type == "Groothandel met Koeling":
        energy_usage = get_energy_usage_groothandel_with_cooling(area)
        if energy_usage is None:
            return "Energy usage data not available for areas larger than 5000 m²."
        else:
            total_energy_usage = area * energy_usage
            return f"Total energy usage for {area} m²: {total_energy_usage:.2f} m³"
    elif business_type == "Groothandel zonder Koeling":
        energy_usage = get_energy_usage_groothandel_without_cooling(area)
        if energy_usage is None:
            return "Energy usage data not available for areas larger than 10,000 m²."
        else:
            total_energy_usage = area * energy_usage
            return f"Total energy usage for {area} m²: {total_gas_usage:.2f} m³"
    else:
        return 0

# Streamlit app
def main():
    st.title("Business Area Value Calculator")

    # Input field for square area
    area = st.number_input("Enter the area in square meters", min_value=0.0, step=1.0)

    # Dropdown menu to select business type
    business_type = st.selectbox("Select a business type", [
        "Detailhandel met Koeling", 
        "Detailhandel zonder Koeling", 
        "Groothandel met Koeling",
        "Groothandel zonder Koeling",
    ])

    # Button to trigger the calculation
    if st.button("Calculate"):
        result = calculate_value(area, business_type)
        st.success(result)

if __name__ == "__main__":
    main()
