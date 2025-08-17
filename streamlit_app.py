import ollama
import streamlit as st

@st.cache_data
def get_ollama_response(prompt):
    return ollama.generate(model='llama3', prompt=prompt, stream=False)

st.title("Ollama Streamlit App")
st.write("This is a simple app to demonstrate Ollama integration with Streamlit.")
user_input = st.text_input("Enter your query:")
if st.button("Submit"):
    with st.spinner("Generating response..."):
        get_ollama_response = get_ollama_response(user_input)
        response = get_ollama_response
    st.success("Response generated!")
    st.write("Response:", response['response'])
        
