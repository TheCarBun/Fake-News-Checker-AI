import streamlit as st
import requests

# API endpoint URL
url = "https://api.langflow.astra.datastax.com/lf/9be127bf-705e-4d94-ac54-e95e0a78d267/api/v1/run/b2e787d4-5a96-4727-945b-08d119c9cab5"
API_TOKEN = st.secrets["API_TOKEN"]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

st.title("AI Fact Checker")

user_input = st.text_input("Enter your query:")

if st.button("Fact Check"):
    # Request payload configuration with user input
    payload = {
        "input_value": user_input,
        "output_type": "chat",
        "input_type": "chat"
    }

    with st.spinner("Fetching response..."):
        try:
            # Send API request
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise exception for bad status codes

            # Parse response and extract output text
            data = response.json()
            output_text = data['outputs'][0]['outputs'][0]['results']['message']['data']['text']

            st.subheader("Output:")
            st.markdown(output_text)

        except Exception as e:
            st.error(f"Error: {e}")