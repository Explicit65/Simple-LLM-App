from model import chat_bot
import os
from fastapi import FastAPI, requests, HTTPException
from fastapi.responses import StreamingResponse, PlainTextResponse
import groq
from dotenv import load_dotenv

# Initialize your Applications
app = FastAPI()
chat_bot = chat_bot()

# Set GROQ_API_KEY = "your api key" in the .env file, then load it below
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = groq.Groq(api_key=GROQ_API_KEY)

@app.route("/chat_batch", methods=["POST"])
async def chat_batch(request: requests):
    user_input = await request.json()
    user_message = user_input.get("message")
    temperature = float(user_input.get("temperature"))
    selected_model = user_input.get("model")


    # Generate a response
    try:
        response = chat_bot.get_response_batch(message = user_message, temperature = temperature, model = selected_model)
        output = response.choices[0].message.content
        return PlainTextResponse(content=output, status_code=200)
    except Exception as e:
        return PlainTextResponse({"error": str(e)})
    