import streamlit as st
import openai

st.set_page_config(page_title="Cofoundr – UAE Company Setup Bot", page_icon="🇦🇪")
st.title("🤖 Cofoundr – Your UAE Company Formation Assistant")

st.markdown("""
Ask me anything about setting up a business in the UAE 🇦🇪  
I’ll help you understand Free Zones, costs, visa options, documents, timelines and more.

**Example Questions**:
- What’s the cheapest Free Zone in the UAE?
- How many visas can I get with a Free Zone license?
- Can a foreigner open a company in Dubai?
""")

openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_response(user_input):
    messages = [
        {"role": "system", "content": """You are Cofoundr, an expert assistant that helps foreigners understand how to set up a company in the UAE.
You provide clear, accurate answers about:
- Free Zone, Mainland and Offshore options
- Visa requirements
- Business license types
- Estimated costs
- Required documents
Your goal is to guide users like an experienced UAE consultant. Keep your tone helpful and informative.
If you are unsure, recommend the user speak to an official business consultant."""},
        {"role": "user", "content": user_input}
    ]
    response = openai.ChatCompletion.create(model="gpt-4o", messages=messages)
    return response.choices[0].message.content.strip()

user_input = st.text_input("Your Question:", placeholder="Type your business setup question here...")

if user_input:
    with st.spinner("Thinking..."):
        reply = get_response(user_input)
        st.markdown("**Answer:**")
        st.write(reply)
