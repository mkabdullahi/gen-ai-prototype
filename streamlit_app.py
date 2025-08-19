import ollama
import streamlit as st
from ollama import ResponseError
import re

MODEL_INFO = {
    'phi3': "Microsoft's 3.8B compact model",
    'mistral': "7B parameter model excelling at coding",
    'llama3': "Meta's 8B parameter model - good for general purpose"
}

@st.cache_data
def get_ollama_response(prompt, model, temperature, max_tokens):
    try:
        return ollama.generate(
            model=model,
            prompt=prompt,
            stream=False,
            options={
                'temperature': temperature,
                'num_predict': max_tokens
            }
        )
    except Exception as e:
        if "timeout" in str(e).lower():
            raise TimeoutError("Model response timed out") from e
        raise

st.title("Multi Models AI Assistance")
st.write("Seamless Search Experience through Multi Models AI Assistance")
model_name = st.selectbox(
    "Select a Model",
    list(MODEL_INFO.keys()),
    index=0,
    help="Select AI model (only installed models will work)"
)
st.caption(MODEL_INFO[model_name])
user_input = st.text_input("Enter your query:",  help="Type your question or prompt here").strip()
# Basic input sanitization
    
if len(user_input) > 2000:
    st.error("Query too long (max 2000 characters)")
    st.stop()
if re.search(r"[^\w\s.,?!-]", user_input):
    st.warning("Input contains special characters - responses may be unpredictable")



temperature = st.slider("Temperature", 0.0, 1.0, 0.7, help="Controls response randomness (0.0 = predictable, 1.0 = creative)")
max_tokens = st.selectbox("Max Response Length", [100, 250, 500, 750, 1000, 1500, 2000], index=2, help="Limits total response length in characters (approximate)")
if st.button("Submit"):
    if not user_input:
        st.error("Please enter a query, in the text box above.")
        st.stop()
    with st.spinner("Generating response..."):
        try:
            response = get_ollama_response(user_input, model_name, temperature, max_tokens)
        except ResponseError as e:
            st.error(f"Model error: {e.error}")
            response = None

    if response:
        st.success("Response generated!")
        st.write("Response:", response['response'])
        
