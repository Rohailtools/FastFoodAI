
from groq import Groq
from app.config import settings
import time


class GroqClient:


    def __init__(self):

        if not settings.GROQ_API_KEY:

            raise ValueError(
                "GROQ_API_KEY missing. Please add it in .env"
            )


        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )


        self.model = "llama-3.3-70b-versatile"



    def chat(
        self,
        prompt: str,
        temperature: float = 0.3,
        max_tokens: int = 500
    ):


        try:

            response = (
                self.client
                .chat
                .completions
                .create(

                    model=self.model,

                    messages=[

                        {
                            "role": "system",
                            "content":
                            "You are a helpful AI assistant."
                        },

                        {
                            "role": "user",
                            "content": prompt
                        }

                    ],

                    temperature=temperature,

                    max_tokens=max_tokens

                )
            )


            return (
                response
                .choices[0]
                .message
                .content
                .strip()
            )


        except Exception as e:


            print(
                "Groq API Error:",
                str(e)
            )


            time.sleep(1)


            return (
                "Maazrat 😊 "
                "Abhi AI response generate nahi ho saka."
            )
