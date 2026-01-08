import streamlit as st
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(
    page_title="AI Chatbot Mentor",
    page_icon="AI",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #1E88E5;
        font-size: 3em;
        font-weight: bold;
        margin-bottom: 10px;
    }
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2em;
        margin-bottom: 30px;
    }
    .module-card {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        border: 2px solid #1E88E5;
        margin: 10px 0;
    }
    .start-button {
        background-color: #1E88E5;
        color: white;
        font-size: 1.2em;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">AI Chatbot Mentor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Your personalized AI learning assistant for mastering technical skills!</p>', unsafe_allow_html=True)

st.markdown("---")

# Module selection
module_options = [
    "Python",
    "SQL", 
    "Power BI",
    "EDA",
    "Machine Learning",
    "Deep Learning",
    "Generative AI",
    "Agentic AI"
]

# Map display names to actual names (identity map after removing emojis)
module_label_map = {name: name for name in module_options}

st.markdown("### Choose Your Learning Module")
selected_display = st.selectbox(
    "Select a module to start your personalized mentoring session:",
    module_options,
    index=0,
    help="Each module has its own domain-specific AI guidance and conversation history."
)

module = module_label_map[selected_display]

st.markdown("---")

# Start button with styling
if st.button(f"Start Mentoring in {selected_display}", key="start_button"):
    module_file_map = {
        "Python": "python",
        "SQL": "sql",
        "Power BI": "power_bi",
        "EDA": "eda",
        "Machine Learning": "machine_learning",
        "Deep Learning": "deep_learning",
        "Generative AI": "generative_ai",
        "Agentic AI": "agentic_ai"
    }
    file_name = module_file_map[module]
    st.switch_page(f"pages/{file_name}.py")

# Footer
st.markdown("---")
st.markdown("**Tip:** Each module maintains separate conversation history. Switch modules anytime from within the mentoring session!")

