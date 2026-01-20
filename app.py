import streamlit as st

# Title
st.title("Welcome to BMI Calculator")

# Weight input
weight = st.number_input("Enter your weight (in kgs)", min_value=0.0)

# Height format selection
status = st.radio(
    "Select your height format:",
    ("cms", "meters", "feet")
)

bmi = None  # sécurité

# Height input & BMI calculation
if status == "cms":
    height = st.number_input("Enter your height in centimeters", min_value=0.0)
    if height > 0:
        bmi = weight / ((height / 100) ** 2)

elif status == "meters":
    height = st.number_input("Enter your height in meters", min_value=0.0)
    if height > 0:
        bmi = weight / (height ** 2)

else:  # feet
    height = st.number_input("Enter your height in feet", min_value=0.0)
    if height > 0:
        bmi = weight / ((height / 3.28) ** 2)

# Button
if st.button("Calculate BMI"):
    if bmi is None:
        st.error("Please enter valid height and weight values.")
    else:
        st.text(f"Your BMI Index is {bmi:.2f}")

        # BMI interpretation
        if bmi < 16:
            st.error("You are Extremely Underweight")
        elif 16 <= bmi < 18.5:
            st.warning("You are Underweight")
        elif 18.5 <= bmi < 25:
            st.success("Healthy")
        elif 25 <= bmi < 30:
            st.warning("Overweight")
        else:
            st.error("Extremely Overweight")

