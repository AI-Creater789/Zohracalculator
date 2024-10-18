import streamlit as st

# Function for calculating radiation exposure
def calculate_exposure(kVp, mA, time, distance):
    exposure = (kVp ** 2) * (mA / 1000) * (time / 1000) / (distance ** 2)
    return exposure

# Function for calculating CT dose index (CTDI)
def calculate_ctdi(voltage, current, exposure_time, slice_thickness):
    ctdi = (voltage ** 2) * (current / 1000) * (exposure_time / 1000) / slice_thickness
    return ctdi

# Function for calculating effective dose
def calculate_effective_dose(ctdi, scan_length):
    effective_dose = ctdi * scan_length
    return effective_dose

# Streamlit application
def main():
    st.title("Radiological Calculator")
    st.sidebar.title("Select Calculation Type")

    option = st.sidebar.selectbox("Choose an option:", ["Radiation Exposure", "CT Dose Index (CTDI)", "Effective Dose"])

    if option == "Radiation Exposure":
        kVp = st.number_input("Enter kVp:", min_value=0.0)
        mA = st.number_input("Enter mA:", min_value=0.0)
        time = st.number_input("Enter time (seconds):", min_value=0.0)
        distance = st.number_input("Enter distance (cm):", min_value=0.0)

        if st.button("Calculate"):
            exposure = calculate_exposure(kVp, mA, time, distance)
            st.success(f"Radiation Exposure: {exposure:.2f} mR")

    elif option == "CT Dose Index (CTDI)":
        voltage = st.number_input("Enter voltage (kVp):", min_value=0.0)
        current = st.number_input("Enter current (mA):", min_value=0.0)
        exposure_time = st.number_input("Enter exposure time (seconds):", min_value=0.0)
        slice_thickness = st.number_input("Enter slice thickness (mm):", min_value=0.0)

        if st.button("Calculate"):
            ctdi = calculate_ctdi(voltage, current, exposure_time, slice_thickness)
            st.success(f"CT Dose Index (CTDI): {ctdi:.2f} mGy")

    elif option == "Effective Dose":
        ctdi = st.number_input("Enter CTDI (mGy):", min_value=0.0)
        scan_length = st.number_input("Enter scan length (cm):", min_value=0.0)

        if st.button("Calculate"):
            effective_dose = calculate_effective_dose(ctdi, scan_length)
            st.success(f"Effective Dose: {effective_dose:.2f} mSv")

# Run the application
if __name__ == "__main__":
    main()
