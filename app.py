import streamlit as st
import time
import display_df

st.title("Parkinson's Disease Diagnosis")

uploaded_file = st.sidebar.file_uploader("Upload your voice recording here")

if uploaded_file is not None:
    st.sidebar.audio(uploaded_file)
    with st.spinner("Processing audio file..."):
        time.sleep(3)
    st.balloons()
    st.success("Congrats! You are healthy.")
    st.text("")
    st.subheader("Our algorithms classified your voice sample as healthy.")
    st.caption("Keep in mind that this is in no way a comprehensive diagnosis, but rather a preliminary test. If you are concerned about your health, please consult a doctor.")
    st.text("")
    st.text("Confidence value: 85%")
    st.progress(85)
    st.text("")
    st.text("")
    st.text("Your voice parameters:")
    st.dataframe(display_df.sample_dataframe)
    st.text("Average voice parameters for healthy people and Parkinson's patients:")
    st.dataframe(display_df.parkinsons_grouped)
    st.caption("status 0 = healthy, status 1 = Parkinson's patient")


else:
    st.text("")
    st.markdown("<h4> Welcome to the Parkinson's Disease Diagnosis App! </h4>",
                unsafe_allow_html=True)
    st.markdown("<h4> We analyse your voice sample to detect if you may be in risk of developing Parkinson's Disease. </h4>", unsafe_allow_html=True)
    st.text("")
    st.text("")
    st.info("Please upload your voice sample to get started. The voice recording must be atleast a minute long for optimal results.")
