import streamlit as st
from dotenv import load_dotenv
load_dotenv()

from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory

from utills.llm import load_llm
from utills.download import generate_chat_text

from prompts.eda_prompt import EDA_PROMPT

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    return InMemoryChatMessageHistory()

module = "EDA"

st.title(f"Welcome to {module} AI Mentor ")

prompt = PromptTemplate(
    input_variables=["input"],
    template=EDA_PROMPT
)

chain_key = f"chain_{module}"
if chain_key not in st.session_state:
    chain = prompt | load_llm()
    st.session_state[chain_key] = RunnableWithMessageHistory(
        chain,
        get_session_history
    )

chat_log_key = f"chat_log_{module}"
if chat_log_key not in st.session_state:
    st.session_state[chat_log_key] = []

user_input = st.text_input("Ask your question:")

if st.button("Send") and user_input:
    response = st.session_state[chain_key].invoke(
        {"input": user_input},
        config={"configurable": {"session_id": "default"}}
    )
    st.session_state[chat_log_key].append(("user", user_input))
    st.session_state[chat_log_key].append(("mentor", response.content))

for role, msg in st.session_state[chat_log_key]:
    st.markdown(f"**{role.capitalize()}:** {msg}")

if st.session_state[chat_log_key]:
    st.download_button(
        "Download Conversation",
        generate_chat_text(st.session_state[chat_log_key]),
        file_name="ai_chatbot_mentor_chat.txt"
    )

# Module switching
modules = ["Python", "SQL", "Power BI", "EDA", "Machine Learning", "Deep Learning", "Generative AI", "Agentic AI"]
other_modules = [m for m in modules if m != module]
if other_modules:
    selected_module = st.selectbox("Move to Other Module", other_modules)
    if st.button("Switch to Selected Module"):
        module_to_file = {
            "Python": "python",
            "SQL": "sql",
            "Power BI": "power_bi",
            "EDA": "eda",
            "Machine Learning": "machine_learning",
            "Deep Learning": "deep_learning",
            "Generative AI": "generative_ai",
            "Agentic AI": "agentic_ai"
        }
        file_name = module_to_file[selected_module]
        st.switch_page(f"pages/{file_name}.py")