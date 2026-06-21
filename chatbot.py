from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def get_response(messages):

    # Latest message
    latest_message = messages[-1]["content"]

    latest_message_lower = latest_message.lower()

    # Simple intent handling
    if latest_message_lower in ["hi", "hello", "hey"]:
        return "Hello! How can I help you today?"

    if latest_message_lower in ["bye", "goodbye"]:
        return "Goodbye! Have a great day."

    # Build conversation history
    prompt = ""

    for msg in messages:
        prompt += f"{msg['role']}: {msg['content']}\n"

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"