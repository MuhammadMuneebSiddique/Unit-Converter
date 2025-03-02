import streamlit as st

# Title of the app
st.title("Google-Style Unit Converter")
st.markdown("#### Convert between different units effortlessly!")

# Unit conversion functions
def convert_length(value, from_unit, to_unit):
    # Conversion logic for length
    length_conversions = {
        "meters": 1.0,
        "feet": 3.28084,
        "inches": 39.3701,
        "kilometers": 0.001,
        "miles": 0.000621371,
    }
    return value * (length_conversions[to_unit] / length_conversions[from_unit])

# Sidebar for unit category selection
st.sidebar.header("Unit Categories")
unit_category = st.sidebar.selectbox(
    "Select a unit category:",
    ["Length", "Weight", "Temperature", "Volume", "Time", "Area", "Speed", "Data Storage",
     "Data Transfer Rate", "Energy", "Frequency", "Fuel Economy", "Mass", "Plane Angle", "Pressure"]
)

# Main app logic
st.header(f"{unit_category} Converter")

# Input fields
col1, col2 = st.columns(2)
with col1:
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
with col2:
    if unit_category == "Length":
        units = ["meters", "feet", "inches", "kilometers", "miles"]
    elif unit_category == "Weight":
        units = ["kilograms", "grams", "pounds", "ounces"]
    elif unit_category == "Temperature":
        units = ["Celsius", "Fahrenheit"]
    elif unit_category == "Volume":
        units = ["liters", "milliliters", "gallons", "quarts"]
    elif unit_category == "Time":
        units = ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]
    elif unit_category == "Area":
        units = ["square meters", "square feet", "square kilometers", "acres", "hectares"]
    elif unit_category == "Speed":
        units = ["meters per second", "kilometers per hour", "miles per hour", "knots"]
    elif unit_category == "Data Storage":
        units = ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
    elif unit_category == "Data Transfer Rate":
        units = ["bits per second", "kilobits per second", "megabits per second", "gigabits per second", "terabits per second"]
    elif unit_category == "Energy":
        units = ["joules", "kilojoules", "calories", "kilocalories", "watt-hours", "kilowatt-hours", "electronvolts"]
    elif unit_category == "Frequency":
        units = ["hertz", "kilohertz", "megahertz", "gigahertz", "terahertz"]
    elif unit_category == "Fuel Economy":
        units = ["miles per gallon", "kilometers per liter", "liters per 100 kilometers"]
    elif unit_category == "Mass":
        units = ["grams", "kilograms", "metric tons", "ounces", "pounds", "stones"]
    elif unit_category == "Plane Angle":
        units = ["degrees", "radians", "gradians", "arcminutes", "arcseconds"]
    elif unit_category == "Pressure":
        units = ["pascals", "kilopascals", "atmospheres", "bars", "millimeters of mercury", "pounds per square inch"]
    
    from_unit = st.selectbox("From unit:", units)
    to_unit = st.selectbox("To unit:", units)

# Formula description for Length Converter
if unit_category == "Length":
    st.markdown("""
    **Formula for Length Conversion:**
    - 1 meter = 3.28084 feet
    - 1 meter = 39.3701 inches
    - 1 kilometer = 0.001 meters
    - 1 mile = 0.000621371 meters

    The conversion is calculated as:
    ```
    Converted Value = Input Value × (Conversion Factor of To Unit / Conversion Factor of From Unit)
    ```
    """)

# Convert button
if st.button("Convert"):
    if unit_category == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif unit_category == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif unit_category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif unit_category == "Volume":
        result = convert_volume(value, from_unit, to_unit)
    elif unit_category == "Time":
        result = convert_time(value, from_unit, to_unit)
    elif unit_category == "Area":
        result = convert_area(value, from_unit, to_unit)
    elif unit_category == "Speed":
        result = convert_speed(value, from_unit, to_unit)
    elif unit_category == "Data Storage":
        result = convert_data_storage(value, from_unit, to_unit)
    elif unit_category == "Data Transfer Rate":
        result = convert_data_transfer_rate(value, from_unit, to_unit)
    elif unit_category == "Energy":
        result = convert_energy(value, from_unit, to_unit)
    elif unit_category == "Frequency":
        result = convert_frequency(value, from_unit, to_unit)
    elif unit_category == "Fuel Economy":
        result = convert_fuel_economy(value, from_unit, to_unit)
    elif unit_category == "Mass":
        result = convert_mass(value, from_unit, to_unit)
    elif unit_category == "Plane Angle":
        result = convert_plane_angle(value, from_unit, to_unit)
    elif unit_category == "Pressure":
        result = convert_pressure(value, from_unit, to_unit)
    
    st.success(f"**Converted Value:** {result:.2f} {to_unit}")