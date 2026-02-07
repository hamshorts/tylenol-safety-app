import streamlit as st

# Dosing Logic: 15mg/kg, capped at 650mg, rounded for oral syringes
def get_dosing_logic(weight_kg):
    dose_mg = min(weight_kg * 15, 650)
    ml_dose = round((dose_mg / 32) * 4) / 4 # 160mg/5mL = 32mg/mL
    return dose_mg, ml_dose

# Growth Chart Sanity Bounds (Approx 5th-95th percentile in KG)
growth_bounds = {
    0: (2.5, 4.5), 2: (4.5, 7.8), 12: (7.5, 12.5), 24: (10.0, 16.0), 
    60: (14.0, 24.0), 120: (24.0, 52.0), 144: (30.0, 70.0)
}

st.set_page_config(page_title="SafeDose Tylenol", page_icon="🚨")
st.title("🚨 SafeDose: Tylenol Calculator")

with st.container():
    age_yrs = st.number_input("Child's Age (Years)", 0, 17, 2)
    weight = st.number_input("Weight", 2.0, 200.0, 25.0)
    unit = st.radio("Units", ["lbs", "kg"], horizontal=True)
    
    if st.button("Calculate Recommendation", type="primary"):
        w_kg = weight if unit == "kg" else weight * 0.453592
        
        # Determine the closest age bracket for sanity check
        age_mos = age_yrs * 12
        closest_age = min(growth_bounds.keys(), key=lambda x: abs(x - age_mos))
        low_kg, high_kg = growth_bounds[closest_age]
        
        # HARD STOP: If weight is statistically improbable for the age
        if w_kg < low_kg or w_kg > high_kg:
            st.error("### 🛑 Safety Alert: Weight/Age Mismatch")
            
            # Suggest likely unit error
            suggestion = f"{weight} kg" if unit == "lbs" else f"{weight} lbs"
            st.write(f"**The weight entered ({weight} {unit}) is highly unusual for a {age_yrs}-year-old.**")
            st.info(f"👉 **Check your units:** Did you mean to enter **{suggestion}**?")
            
            st.warning("**NO DOSE CALCULATED:** If this weight is correct, please consult your physician or pharmacist directly for specialized dosing guidance. Do not use this app for outliers.")
        
        else:
            # PROCEED: Weight is within the 90% range
            mg, ml = get_dosing_logic(w_kg)
            st.success(f"### Recommended Dose: {ml} mL")
            st.write(f"**Formulation:** Children's Tylenol (160 mg / 5 mL)")
            st.caption(f"Note: This dose is calculated at 15mg/kg ({round(mg)} mg total).")

st.divider()
st.markdown("#### ⚠️ General Safety Rules")
st.write("* Max 5 doses in 24 hours.")
st.write("* Wait at least 4 to 6 hours between doses.")
st.write("* Always use the measuring device (syringe/cup) included with the medication.")
