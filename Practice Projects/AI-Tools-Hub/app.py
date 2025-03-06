import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Tools Hub", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "AI Tool Recommender", "About"])

# --- HOME PAGE ---
if page == "Home":
    st.title("🤖 AI Tools Hub")
    st.write("Discover the best AI tools for different use cases!")
    
    # AI image (optional, uncomment if you have an image)
    # st.image("images.jpg", use_column_width=True)

    st.subheader("🚀 Features:")
    st.markdown("""
    - **Get AI tool recommendations** based on your needs
    - **Learn about AI-powered software**
    - **Simple, fast, and interactive UI**
    """)

    st.subheader("📖 Latest AI Articles:")
    
    articles = {
        "How AI is Transforming Content Creation": "https://www.forbes.com/sites/forbestechcouncil/2023/10/01/how-ai-is-transforming-content-creation/",
        "The Rise of AI in Software Development": "https://www.techradar.com/news/how-ai-is-changing-software-development",
        "AI-Powered Chatbots: Future of Customer Service": "https://www.ibm.com/blogs/think/2023/09/ai-chatbots-future/",
        "Generative AI and its Impact on Business": "https://hbr.org/2023/08/the-rise-of-generative-ai-in-business",
        "AI for Everyone: How to Get Started with AI": "https://www.coursera.org/articles/how-to-get-started-in-ai"
    }

    for title, link in articles.items():
        st.markdown(f"- **[{title}]({link})**", unsafe_allow_html=True)

# --- AI TOOL RECOMMENDER ---
elif page == "AI Tool Recommender":
    st.title("🔍 Find the Best AI Tools!")
    st.write("Select your purpose, and we’ll recommend AI-powered tools with links.")

    # Dropdown for selecting use case
    use_case = st.selectbox("Select Your Purpose:", 
                            ["Choose...", "Text Generation", "Image Generation", "Code Assistance", "Chatbots"])

    # Dictionary for AI tools and their links
    tool_links = {
        "Text Generation": {
            "ChatGPT": "https://chat.openai.com",
            "Jasper AI": "https://www.jasper.ai",
            "Copy.ai": "https://www.copy.ai"
        },
        "Image Generation": {
            "DALL·E": "https://openai.com/dall-e",
            "MidJourney": "https://www.midjourney.com",
            "Stable Diffusion": "https://stability.ai"
        },
        "Code Assistance": {
            "GitHub Copilot": "https://github.com/features/copilot",
            "Codeium": "https://www.codeium.com",
            "Tabnine": "https://www.tabnine.com"
        },
        "Chatbots": {
            "Rasa": "https://rasa.com",
            "Dialogflow": "https://cloud.google.com/dialogflow",
            "OpenAI GPT API": "https://openai.com/research/chatgpt"
        }
    }

    # Display AI tool recommendations with clickable links
    if use_case in tool_links:
        st.success("Recommended Tools:")
        for tool, link in tool_links[use_case].items():
            st.markdown(f"- **[{tool}]({link})**", unsafe_allow_html=True)

# --- ABOUT PAGE ---
elif page == "About":
    st.title("📌 About This App")
    st.write("This is a simple AI tools recommender built using **Streamlit**. 🚀")
    st.markdown("---")
    st.write("💡 Created by Abdul Rehman")  
