from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("MINHA_CHAVE")
)

for model in client.models.list():
    print(model.name)