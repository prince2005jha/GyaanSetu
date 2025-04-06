from flask import Flask, render_template, request, jsonify
from google.cloud import dialogflow_v2 as dialogflow
import os
import uuid  # For generating unique session IDs

app = Flask(__name__)

# Replace with your Dialogflow credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\jhap9\OneDrive\Desktop\dev vscode\Projects\gdg chatbot\client_secret_913949725933-b4an2853b1eknlfe8sejdfiviui6338e.apps.googleusercontent.com (1).json"

dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "gyansetu-453518"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat')
def chat():
    return render_template('chat.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json['message']
    
    # Generate a unique session ID for each user
    session_id = str(uuid.uuid4())
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)

    # Create a text input for Dialogflow
    text_input = dialogflow.types.TextInput(text=user_message, language_code="en")
    query_input = dialogflow.types.QueryInput(text=text_input)

    # Detect intent using Dialogflow
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)

    # Extract the fulfillment text from the response
    reply = response.query_result.fulfillment_text
    return jsonify({"response": reply})

if __name__ == '__main__':
    app.run(debug=True)