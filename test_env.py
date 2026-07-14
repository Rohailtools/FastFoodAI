
from dotenv import load_dotenv
import os

load_dotenv(".env", override=True)

print("ENV GROQ:", bool(os.getenv("GROQ_API_KEY")))
print("ENV LENGTH:", len(os.getenv("GROQ_API_KEY","")))
