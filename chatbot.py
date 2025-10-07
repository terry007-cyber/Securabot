import os
import sys
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS 
from dotenv import load_dotenv
# --- SPECIAL CODE FOR PYINSTALLER ---
# This function helps the script find files when it's a bundled .exe
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# --- 1. INITIAL SETUP AND API KEY CONFIGURATION ---

# Use the function to find the .env file
dotenv_path = resource_path('.env')
load_dotenv(dotenv_path=dotenv_path)

# Get the API key from the environment variables
api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is available
if not api_key:
    raise ValueError("Error: GEMINI_API_KEY is not set. Please create a .env file and add your API key.")

# Configure the generative AI model with the API key
try:
    genai.configure(api_key=api_key)
    # Use the correct model name discovered from our tests
    model = genai.GenerativeModel('models/gemini-pro-latest')
except Exception as e:
    raise ValueError(f"Error configuring the Gemini API: {e}")

# --- 2. THE CORE CHATBOT LOGIC ---

def get_chatbot_response(user_question):
    """
    Generates a response from the AI and parses out structured sources.
    """
    try:
        # Find the knowledge base file, whether in dev or as an .exe
        knowledge_path = resource_path('knowledge_base.txt')
        with open(knowledge_path, 'r', encoding='utf-8') as f:
            knowledge = f.read()

        # 2a. This is the "Prompt Engineering" step.
        prompt = f"""
        You are "SecuraBot," a world-class AI assistant for cybersecurity professionals.
        Your sole purpose is to answer questions about web application security.
        You must adhere to the following rules strictly:
        1. Use ONLY the information provided in the 'Knowledge Base' below to answer the user's question.
        2. When you use a knowledge block that contains a 'SOURCES:' section, you MUST include that section verbatim at the end of your answer.
        3. If the answer is not found in the 'Knowledge Base', you must reply with exactly this phrase:
           "I do not have sufficient information on that topic. My knowledge is focused on the provided security materials."
        4. When a user asks for a specific item number from a list you have access to in the Knowledge Base, you MUST provide that specific item. For example, if the user asks for "number 10" from a list of payloads, you must find the 10th payload and provide it.
        5. If a user asks a follow-up question that refers to a previous answer (e.g., "tell me more about the third one"), you should assume they are referring to the most recently discussed topic.

        ---
        Knowledge Base:
        {knowledge}
        ---

        User's Question:
        {user_question}

        Expert Answer:
        """

        # 2b. Send the complete prompt to the AI model
        response = model.generate_content(prompt)
        
        # 2c. *** NEW CODE *** Parse the AI's raw text to separate answer and sources
        raw_text = response.text
        answer_part = raw_text
        sources_part = []

        if "SOURCES:" in raw_text:
            parts = raw_text.split("SOURCES:", 1)
            answer_part = parts[0].strip()
            # Split the sources by newline and filter out any empty lines
            sources_part = [line.strip() for line in parts[1].strip().split('\n') if line.strip()]

        # Return a dictionary with separate answer and sources fields
        return {"answer": answer_part, "sources": sources_part}

    except FileNotFoundError:
        return {"answer": "Error: The knowledge_base.txt file was not found.", "sources": []}
    except Exception as e:
        return {"answer": f"An error occurred while generating a response: {e}", "sources": []}

    # --- 3. THE API SERVER (Bridge to the UI) ---

app = Flask(__name__)
CORS(app) # <--- NEW LINE HERE. This enables connections from your UI.

@app.route('/ask', methods=['POST'])
def ask_bot():
    """
    This is the API endpoint that the UI will call.
    """
    data = request.get_json()
    if not data or 'question' not in data:
        return jsonify({"error": "Invalid request. Please provide a 'question' in the JSON body."}), 400

    user_question = data['question']

    # 3b. *** MODIFIED CODE *** Get the response object from our chatbot function
    bot_response_object = get_chatbot_response(user_question)

    # 3c. Send the entire object back to the UI in a JSON format
    return jsonify(bot_response_object)

# --- 4. RUN THE APPLICATION ---

if __name__ == '__main__':
    print("Starting SecuraBot API server... Go to http://127.0.0.1:8888")
    app.run(host='0.0.0.0', port=8888, debug=True)
