import os
import groq
from dotenv import load_dotenv
load_dotenv()

class chat_bot():
    # Set GROQ_API_KEY = "your api key" in the .env file, then load it below
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    # print(GROQ_API_KEY)
    # GROQ_API_KEY: str = "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"
    # Run generative search otherwise
    client = groq.Groq(api_key=GROQ_API_KEY)
    query: str
    output: str = ""
    models = [
        # "llama-3.1-405b-reasoning",
        "llama-3.1-70b-versatile",
        "llama-3.1-8b-instant",
        "mixtral-8x7b-32768"
    ]

    output_type = ["Stream", "Batch"]
    sys_prompt = """You are an intelligent generative search assistant. As an expert in trained on diverse knowledge base, \
                        provide to the best of your ability response to my query using the most recent information"""
    
    def get_response(self, message, model="llama-3.1-70b-versatile", temperature=0):
        try:
            response = self.client.chat.completions.create(
                model = model,
                message = [
                    {"role": "system", "content": self.sys_prompt},
                    {"role": "user", "content": message}
                ],
                stream = True,
                temperature = temperature,
                max_tokens = 1536
            )
            return response
        
        except Exception as e:
            return {"error": str(e)}
        
    
    def get_response_batch(self, message, model="llama-3.1-70b-versatile", temperature=0):
        try:
            response = self.client.chat.completions.create(
                model = model,
                messages = [
                    {"role": "system", "content": self.sys_prompt},
                    {"role": "user", "content": message}
                ],
                response_format = {"type": "text"},
                temperature = temperature
            )
            return response

        except Exception as e:
            return {"error": str(e)}



