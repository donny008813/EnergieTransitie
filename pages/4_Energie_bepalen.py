import streamlit as st

# Function to calculate based on area and business type
def calculate_value(area, business_type):
    # You can customize these formulas for each business type
    if business_type == "Retail":
        return area * 50
    elif business_type == "Restaurant":
        return area * 100
    elif business_type == "Office":
        return area * 75
    else:
        return area * 40  # Default calculation

# Streamlit app
def main():
    st.title("Business Area Value Calculator")

    # Input field for square area
    area = st.number_input("Enter the area in square meters", min_value=0.0, step=1.0)

    # Dropdown menu to select business type
    business_type = st.selectbox("Select a business type", ["Retail", "Restaurant", "Office", "Other"])

    # Button to trigger the calculation
    if st.button("Calculate"):
        result = calculate_value(area, business_type)
        st.success(f"The calculated value for a {business_type} business with an area of {area} square meters is: ${result}")

if __name__ == "__main__":
    main()
