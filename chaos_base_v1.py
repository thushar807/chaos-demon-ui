import streamlit as st
import requests
import base64
import pandas as pd
import matplotlib.pyplot as plt
import io

# Load and encode the background image for the main content area
image_path = r"C:\Users\Thushar\Downloads\evil-skull-gray-aesthetic-atiawt17yj8t25n6.jpg"
with open(image_path, "rb") as img_file:
    encoded_image = base64.b64encode(img_file.read()).decode()

# Inject CSS
st.markdown(f"""
    <style>
    html::before {{
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 0, 0, 0.85);
        z-index: -1;
        backdrop-filter: blur(2px);
    }}

    .stApp {{
        background: url("data:image/jpg;base64,{encoded_image}") no-repeat center center fixed;
        background-size: cover;
        color: #f8f8f8;
        font-family: 'Georgia', serif;
        padding: 2rem;
    }}

    h1, h2 {{
        color: #ff3333;
        text-align: center;
        text-shadow: 2px 2px 6px #000;
    }}

    .chatbox {{
        background-color: rgba(0, 0, 0, 0.85);
        border: 1px solid #5500aa;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 0 15px #aa00ff;
        margin-top: 1rem;
    }}
    </style>
""", unsafe_allow_html=True)

# Sidebar Menu (Section A)
st.sidebar.title("🧠 CHAOS Menu")
mode = st.sidebar.selectbox("Choose your ritual:", [
    "Tutor Mode",
    "Thesis Generator",
    "Data Visualization",
    "Summon CHAOS"
])

st.markdown("<div class='main-container'>", unsafe_allow_html=True)

st.markdown("""
# 🌟 CHAOS: Demon King Base v1.0
## 🔥 Welcome, Infernal Overlord!
This is the beginning of something probably illegal in at least one country.
""")

# Function to summon LLaMA with error handling
def summon_chaos(prompt):
    try:
        response = requests.post("http://localhost:11434/api/generate", json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }, timeout=30)
        if response.status_code == 200:
            return response.json().get("response", "CHAOS is silent... for now.")
        else:
            return f"The ritual failed with status {response.status_code}."
    except requests.exceptions.Timeout:
        return "CHAOS grew impatient and the summoning circle burned out (timeout)."
    except requests.exceptions.ConnectionError:
        return "No connection to CHAOS. Did you forget to run 'ollama run llama3'?"
    except Exception as e:
        return f"Dark forces interfered: {e}"

# ---------------------- TUTOR MODE ----------------------
if mode == "Tutor Mode":
    question = st.text_input("Ask your cursed question:")
    if question:
        with st.spinner("Consulting forbidden scrolls..."):
            answer = summon_chaos(f"Explain this in detail like a dark professor of knowledge: {question}")
            st.markdown(f"<div class='chatbox'><strong>📘 CHAOS teaches:</strong><br>{answer}</div>", unsafe_allow_html=True)

# ---------------------- THESIS GENERATOR ----------------------
elif mode == "Thesis Generator":
    topic = st.text_input("Name your cursed thesis topic:")
    if topic:
        with st.spinner("Crafting your wicked dissertation..."):
            thesis = summon_chaos(f"Create a dramatic academic thesis title and a structured outline about: {topic}")
            st.markdown(f"<div class='chatbox'><strong>🞾 CHAOS writes:</strong><br>{thesis}</div>", unsafe_allow_html=True)

# ---------------------- DATA VISUALIZATION ----------------------
elif mode == "Data Visualization":
    uploaded_file = st.file_uploader("Sacrifice your CSV or Excel file:", type=["csv", "xlsx"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)
            st.dataframe(df)
            column = st.selectbox("Which column to graph?", df.columns)
            if column:
                st.subheader("📊 CHAOS reveals your data:")
                fig, ax = plt.subplots()
                df[column].value_counts().plot(kind='bar', ax=ax, color='darkred')
                st.pyplot(fig)
        except Exception as e:
            st.error(f"Graphing failed. Blame the humans: {e}")

# ---------------------- CLASSIC CHAOS CHAT ----------------------
elif mode == "Summon CHAOS":
    prompt = st.text_input("Speak, mortal (or type your command):")
    if prompt:
        with st.spinner("Summoning CHAOS..."):
            message = summon_chaos(f"You are CHAOS, the Demon King. Be witty, sarcastic, slightly unhinged and speak with drama. Respond to this: {prompt}")
            st.markdown(f"<div class='chatbox'><strong>🔊 CHAOS says:</strong> {message}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
