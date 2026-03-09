# gemini-text-assistant

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)

## Overview
This application is a conversational AI tool designed to perform meaningful text tasks such as summarization, content generation, and domain-specific Q&A. Built with Python and Streamlit, it provides a seamless user experience for interacting with state-of-the-art Large Language Models.

---

## Technical Stack
* Model Name: gemini-3-flash-preview
* Source: Google AI Studio / Google Gen AI SDK
* Deployment: Streamlit

### Rationale for Selection
I chose the Gemini 3 Flash model for this project because it is optimized for quick response time and efficiency.

1. Quick Answers: Flash models are designed to provide nearly instantaneous responses. This is important in maintaining the flow of a chat interface in a web-based application.
2. Long Context: It has an extremely large token window. This enables it to read long documents without losing context.
3. Lower Cost: It has robust reasoning capabilities at a fraction of the cost of the larger models.

---

## Responsible AI Reflection
When I was building this assistant, I really tried to make sure everything was transparent and secure with the data stuff. Like, for the API keys, I put them in environment variables, you know, that .env file, so they wouldnt show up in the code history on version control. That way, no one sneaky could get to them easily.

I also worried about those AI hallucinations, where the model just makes stuff up. So I added some system instructions to push it towards being more professional and sticking to facts. But honestly, large language models pick up biases from all the data they train on, and I get that as the developer. It seems like its hard to totally avoid that.

To handle it better, the user interface has this Clear Chat button that lets people wipe the session data if they want. And the whole thing follows this idea of human in the loop, meaning users should check what the AI says, especially for important things. I think that keeps a balance between how fast AI can be and needing people to double check. Sometimes it feels a bit messy though, like not everything is perfectly covered yet.

---

## Setup and Installation

1. Clone the Repository:
git clone https://github.com/your-username/gemini-text-assistant.git

2. Install Dependencies:
pip install -r requirements.txt

3. Configure Environment Variables:
Create a .env file in the root directory and add:
GOOGLE_API_KEY=your_actual_key_here

4. Run the App:
streamlit run app.py
