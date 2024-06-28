import streamlit as st
import pickle
from PIL import Image


# Load logo image
logo = Image.open('logo.png')

# Load the ML model from the pickle file
with open('medical_insurance_model.pkl', 'rb') as f:
    model = pickle.load(f)


# Create sidebar with logo and menu options
st.sidebar.image(logo, use_column_width=True)
st.sidebar.title("Insurance Cost Prediction App")
st.sidebar.caption("Powered by Machine Learning")
st.sidebar.empty()
st.sidebar.caption("Developed by: G8 Analytics")


# Create main UI form
st.title("Insurance Application Form")
form = st.form(key="insurance-form")

# Create a row for Age, BMI, and Children
row1 = form.columns(3)
age = row1[0].text_input("Age", value="", max_chars=3)
bmi = row1[1].text_input("BMI", value="", max_chars=4)
children = row1[2].text_input("Number of Children", value="", max_chars=2)

# Create a row for Sex, Smoker, and Region
row2 = form.columns(3)
sex = row2[0].selectbox("Sex", ["Male", "Female"])
smoker = row2[1].selectbox("Smoker", ["Yes", "No"])
region = row2[2].selectbox("Region", ["South-East", "North-West", "South-West", "North-East"])

sex_value = 0
smoker_value = 0
region_northeast = 0
region_northwest = 0
region_southeast = 0

submit = form.form_submit_button("Predict Insurance Cost")

# Process form data
if submit:
    # Converting sex region & smoker values
    sex_value = 0 if sex == "Male" else 1
    smoker_value = 0 if smoker == "Yes" else 1
    region_northeast = 1 if region == "North-East" else 0
    region_northwest = 1 if region == "North-West" else 0
    region_southeast = 1 if region == "South-East" else 0
    
    # Print form data
    st.write("Form Data:")
    st.write(f"Age: {age}  |  BMI: {bmi}  |  Children: {children}  |  Sex: {sex_value}  |  Smoker: {smoker_value}  |  Region: {region}")
    prediction = model.predict([[float(age), float(bmi), float(children), sex_value, smoker_value, region_northeast, region_northwest, region_southeast]])
    st.markdown("## **Predicted Insurance Charge: ₦** **{:,.2f}**".format(float(prediction[0])))   