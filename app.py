import streamlit as st

st.title("Streamlit Demo App :cucumber")
st.markdown("Willkommen auf der Website. Hier gibts jarnüscht zu sehen.")

username = st.text_input("Benutzername")

st.write(username)
