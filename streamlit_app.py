import ollama
import streamlit as st
from ollama import ResponseError

MODEL_INFO = {
    'llama3': "Meta's 8B parameter model - good general purpose",
    'mistral': "7B parameter model excelling at coding",
    'phi3': "Microsoft's 3.8B compact model"
}

@st.cache_data
def get_ollama_response(prompt, model, temperature, max_tokens):
    return ollama.generate(
        model=model,
        prompt=prompt,
        stream=False,
        options={
            'temperature': temperature,
            'num_predict': max_tokens
        }
    )

st.title("Ollama Streamlit App")
st.write("This is a simple app to demonstrate Ollama integration with Streamlit.")
model_name = st.selectbox(
    "Model",
    list(MODEL_INFO.keys()),
    index=0,
    help="Select AI model (only installed models will work)"
)
st.caption(MODEL_INFO[model_name])
user_input = st.text_input("Enter your query:")


temperature = st.slider("Temperature", 0.0, 1.0, 0.7, help="Controls response randomness (0.0 = predictable, 1.0 = creative)")
max_tokens = st.selectbox("Max Response Length", [100, 250, 500, 750, 1000, 1500, 2000], index=2, help="Limits total response length in characters (approximate)")
if st.button("Submit"):
    with st.spinner("Generating response..."):
        try:
            response = get_ollama_response(user_input, model_name, temperature, max_tokens)
        except ResponseError as e:
            st.error(f"Model error: {e.error}")
            response = None

    if response:
        st.success("Response generated!")
        st.write("Response:", response['response'])
