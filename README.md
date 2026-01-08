# 🤖 AI Chatbot Mentor

An interactive, AI-powered mentoring application designed to provide focused, module-specific guidance to learners across multiple technical domains. Unlike generic chatbots, this system strictly responds only within the selected module, ensuring relevant, accurate, and distraction-free mentorship.

## 🚀 Features

- **Module-Based Mentoring**: Dedicated AI mentors for Python, SQL, Power BI, EDA, Machine Learning, Deep Learning, Generative AI, and Agentic AI.
- **Domain-Restricted Responses**: Answers only relevant questions; rejects off-topic queries with a standard message.
- **Conversation Memory**: Maintains full chat history per module using LangChain's memory system.
- **Multi-Page Interface**: Clean, dedicated pages for each module with seamless navigation.
- **Download Conversations**: Export chat history as .txt files for offline learning and notes.
- **Module Switching**: Switch between modules directly from any mentoring page without losing progress.
- **Attractive UI**: Emoji-rich, responsive design with custom styling for an engaging user experience.

## 🛠️ Tech Stack

- **Frontend**: Streamlit (for interactive web UI and multi-page navigation)
- **AI Orchestration**: LangChain (for LLM integration, prompt engineering, and conversation memory)
- **LLM**: Google Gemini (via `langchain-google-genai`)
- **Memory Management**: LangChain Core (InMemoryChatMessageHistory for session-based conversations)
- **File Export**: Text (.txt) downloads
- **Environment**: Python 3.13, Virtual Environment (mentor)

## 📁 Project Structure

```
AI_Chatbot_Mentor/
├── app.py                    # Home page: Module selection and navigation
├── pages/                    # Module-specific pages
│   ├── __init__.py
│   ├── python.py
│   ├── sql.py
│   ├── power_bi.py
│   ├── eda.py
│   ├── machine_learning.py
│   ├── deep_learning.py
│   ├── generative_ai.py
│   └── agentic_ai.py
├── prompts/                  # Prompt templates for each module
│   ├── __init__.py
│   ├── python_prompt.py
│   ├── sql_prompt.py
│   ├── powerbi_prompt.py
│   ├── eda_prompt.py
│   ├── ml_prompt.py
│   ├── dl_prompt.py
│   ├── genai_prompt.py
│   └── agentic_ai_prompt.py
├── utills/                   # Utility functions
│   ├── __init__.py
│   ├── llm.py                # LLM loading and configuration
│   ├── memory.py             # Memory setup (updated for LangChain 1.x)
│   └── download.py           # Chat export functionality
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (API keys)
└── README.md                 # This file
```

## 🔧 Installation & Setup

1. **Clone or Navigate to the Project Directory**:
   ```
   cd mentor/AI_Chatbot_Mentor
   ```

2. **Create and Activate Virtual Environment**:
   ```
   python -m venv mentor
   mentor\Scripts\activate  # On Windows
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

5. **Run the Application**:
   ```
   streamlit run app.py
   ```
   - Open the provided URL (usually `http://localhost:8501`) in your browser.

## 🎯 How It Works

### 1. **Home Page (app.py)**
   - **Welcome Screen**: Attractive UI with title, description, and module selection.
   - **Module Selection**: Dropdown with emoji icons for each technical domain.
   - **Start Mentoring**: Click the button to navigate to the selected module's dedicated page.

### 2. **Module-Specific Pages (pages/*.py)**
   - **Dedicated Interface**: Each module has its own page with a unique title and prompt.
   - **Chat Interface**:
     - Input field for user questions.
     - Send button to query the AI mentor.
     - Real-time display of conversation history.
   - **Domain Control**: AI responds only to module-relevant questions; otherwise, returns: "Sorry, I don't know about this question. Please ask something related to the selected module."
   - **Memory Persistence**: Conversations are stored per module using `RunnableWithMessageHistory` and `InMemoryChatMessageHistory`.

### 3. **Key Interactions**
   - **Ask Questions**: Type in the input box and click "Send" for AI responses.
   - **Download Chat**: Click "📥 Download Conversation" to save the session as a .txt file.
   - **Switch Modules**: Use the "Move to Other Module" dropdown and "Switch to Selected Module" button to navigate to another module's page instantly.

### 4. **Behind the Scenes**
   - **Prompt Engineering**: Each module uses a tailored prompt template defining rules and context.
   - **LLM Integration**: Google Gemini processes queries with temperature 0.2 for focused responses.
   - **Memory Management**: LangChain handles conversation history, ensuring coherent, continuous mentoring.
   - **Page Navigation**: Streamlit's `st.switch_page` enables seamless transitions between modules.

## 📋 Requirements Fulfillment

This project meets all specified requirements:
- ✅ Module-based AI mentoring with strict domain control.
- ✅ Irrelevant question rejection.
- ✅ Session-based conversation memory.
- ✅ Chat history download.
- ✅ Clean, interactive Streamlit UI.
- ✅ Dedicated interfaces for each module.
- ✅ Seamless module switching.

## 🧠 Learning Outcomes

By building this project, you'll understand:
- Designing domain-restricted AI systems with prompt engineering.
- Implementing conversation memory in LangChain.
- Creating multi-page Streamlit applications.
- Integrating LLMs for educational AI assistants.
- Structuring real-world AI mentor applications.

## 🤝 Contributing

Feel free to enhance the project by:
- Adding more modules or topics.
- Improving UI/UX with advanced Streamlit components.
- Integrating other LLMs or memory backends.
- Adding user authentication or progress tracking.

## 📞 Support

For issues or questions:
- Check the conversation logs for debugging.
- Ensure your `.env` file has a valid `GOOGLE_API_KEY`.
- Verify all dependencies are installed in the virtual environment.

---


**Happy Learning!** 🎓 Explore the modules, ask questions, and master your technical skills with AI-powered mentorship.
