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
    try:
        return ollama.generate(
            model=model,
            prompt=prompt,
            stream=False,
            options={
                'temperature': temperature,
                'num_predict': max_tokens
            },
            request_timeout=30  # 30-second timeout
        )
    except Exception as e:
        if "timeout" in str(e).lower():
            raise TimeoutError("Model response timed out after 30 seconds") from e
        raise

st.title("Ollama Streamlit App")
st.write("This is a simple app to demonstrate Ollama integration with Streamlit.")
model_name = st.selectbox(
    "Model",
    list(MODEL_INFO.keys()),
    index=0,
    help="Select AI model (only installed models will work)"
)
st.caption(MODEL_INFO[model_name])
import re
from datetime import datetime, timedelta

# Rate limiting - 5 requests per minute
if 'last_requests' not in st.session_state:
    st.session_state.last_requests = []

user_input = st.text_input("Enter your query:").strip()
# Basic input sanitization
if not user_input:
    st.error("Please enter a query")
    st.stop()
if len(user_input) > 2000:
    st.error("Query too long (max 2000 characters)")
    st.stop()
if re.search(r"[^\w\s.,?!-]", user_input):
    st.warning("Input contains special characters - responses may be unpredictable")

# Check rate limit
recent_requests = [t for t in st.session_state.last_requests if t > datetime.now() - timedelta(minutes=1)]
if len(recent_requests) >= 5:
    st.error("Too many requests - please wait 1 minute")
    st.stop()
st.session_state.last_requests.append(datetime.now())

temperature = st.slider("Temperature", 0.0, 1.0, 0.7, help="Controls response randomness (0.0 = predictable, 1.0 = creative)")
max_tokens = st.selectbox("Max Response Length", [100, 250, 500, 750, 1000, 1500, 2000], index=2, help="Limits total response length in characters (approximate)")
if st.button("Submit"):
    with st.spinner("Generating response..."):
        try:
            response = get_ollama_response(user_input, model_name, temperature, max_tokens)
        except ResponseError as e:
            st.error(f"Model error: {e.error}")
            response = None
        except TimeoutError as te:
            st.error(f"Request timed out: {str(te)}")
            response = None
        except Exception as e:
            st.error(f"Unexpected error: {str(e)}")
            response = None

    if response:
        st.success("Response generated!")
        st.write("Response:", response['response'])
