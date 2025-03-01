import streamlit as st

# Custom CSS for Styling
st.markdown(
    """
    <style>
        
        /* Headings */
        h1, h2, h3 {
            text-align: center;
            font-weight: bold;
        }

        /* Input & Select Box */
        .stTextInput>div>div>input, .stSelectbox>div>div>select {
            background-color: #fff !important;
            color: black !important;
            border-radius: 10px !important;
            padding: 8px;
        }

        /* Buttons */
        div.stButton>button {
            background-color: #ff6b6b;
            color: white;
            border-radius: 10px;
            width: 100%;
            font-size: 16px;
            font-weight: bold;
            padding: 10px;
            cursor: pointer;
            border: none;
        }
        div.stButton>button:hover {
            background-color: #ff4040;
        }

        /* Success & Warning Messages */
        .stAlert {
            background-color: rgba(255, 255, 255, 0.2);
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            font-weight: bold;
        }

        /* Quote Box */
        .quote {
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
            background: linear-gradient(to right, #ff7e5f, #feb47b);
            padding: 12px;
            border-radius: 8px;
            text-align: center;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            margin-bottom: 20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Web App Title
st.markdown("<h1>🔄 Unit Converter</h1>", unsafe_allow_html=True)

# Quote Box
st.markdown('<div class="quote">⚖️ Why guess when you can convert? Precision is just one click away!</div>', unsafe_allow_html=True)

# Conversion Factors Dictionary
conversion_factors = {
    "Length": {
        "meters": {"kilometers": 0.001, "miles": 0.000621371, "feet": 3.28084},
        "kilometers": {"meters": 1000, "miles": 0.621371, "feet": 3280.84},
        "miles": {"meters": 1609.34, "kilometers": 1.60934, "feet": 5280},
        "feet": {"meters": 0.3048, "kilometers": 0.0003048, "miles": 0.000189394}
    },
    "Weight": {
        "grams": {"kilograms": 0.001, "pounds": 0.00220462, "ounces": 0.035274},
        "kilograms": {"grams": 1000, "pounds": 2.20462, "ounces": 35.274},
        "pounds": {"kilograms": 0.453592, "grams": 453.592, "ounces": 16},
        "ounces": {"grams": 28.3495, "kilograms": 0.0283495, "pounds": 0.0625}
    },
    "Time": {
        "seconds": {"minutes": 1/60, "hours": 1/3600, "days": 1/86400},
        "minutes": {"seconds": 60, "hours": 1/60, "days": 1/1440},
        "hours": {"seconds": 3600, "minutes": 60, "days": 1/24},
        "days": {"seconds": 86400, "minutes": 1440, "hours": 24, "weeks": 1/7},
        "weeks": {"days": 7, "hours": 168, "minutes": 10080, "seconds": 604800}
    }
}

# Step 1: User Inputs
value = st.number_input("Enter value", min_value=0.0, format="%.2f")

# Step 2: Select Category
category = st.selectbox("Please Select a category", ["Length", "Weight", "Temperature", "Time"]) 

# Temperature conversion function
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9/5 + 32
    else:
        return value  

# Step 3: Select Units Based on Category
if category in ["Length", "Weight", "Time"]:
    units = list(conversion_factors[category].keys())
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
elif category == "Temperature":
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)

# Step 4: Perform Conversion
if st.button("Convert"):
    if from_unit != to_unit:
        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            result = value * conversion_factors[category][from_unit][to_unit]
        
        st.markdown(
            f'<div class="stAlert">✅ <b>{value} {from_unit} = {result:.4f} {to_unit}</b></div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            '<div class="stAlert">⚠️ Please select different units!</div>',
            unsafe_allow_html=True
        )
