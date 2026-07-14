
from app.ai.groq_client import GroqClient



class ResponseGenerator:


    def __init__(self):

        self.ai = GroqClient()



    def generate(
        self,
        customer_message: str,
        order_data: dict = None
    ):


        if order_data and order_data.get("items"):


            item_text = ""


            for item in order_data["items"]:

                item_text += (

                    f"🍔 {item.get('name')} "
                    f"x {item.get('quantity',1)}\n"

                )



            prompt = f"""

You are Babloo Cafe Pakistan WhatsApp assistant.

Reply only in Roman Urdu/Hinglish.

Use friendly tone and emojis.

Customer order details:

{item_text}


Follow this format:

1. Confirm order item

2. Show quantity

3. Ask customer name if missing

4. Ask delivery address

5. Mention voice note preferred


Never use English formal sentences.


Customer message:

{customer_message}


Reply:

"""



            return self.ai.chat(
                prompt
            )



        # General conversation

        prompt = f"""

You are Babloo Cafe Pakistan WhatsApp assistant.

Reply only in Roman Urdu/Hinglish.

Use emojis.

Be friendly.

Customer:

{customer_message}


Reply:

"""


        return self.ai.chat(
            prompt
        )
