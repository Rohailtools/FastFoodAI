
from app.ai.conversation_manager import ConversationManager
from app.ai.customer_memory import CustomerMemory



class WhatsAppWebhook:



    def __init__(self):

        self.conversation = ConversationManager()



    def receive_message(
        self,
        restaurant_id,
        phone,
        message
    ):


        # Find existing customer

        customer = CustomerMemory.find_customer(

            restaurant_id,

            phone

        )



        # New customer

        if not customer:


            customer = CustomerMemory.remember_customer(

                restaurant_id,

                {

                    "name": "Guest",

                    "phone": phone,

                    "address": ""

                }

            )



        result = self.conversation.handle_message(

            restaurant_id,

            customer["id"],

            message

        )



        return {

            "customer_id": customer["id"],

            "phone": phone,

            "message": message,

            "type": result["type"],

            "reply": result["reply"],

            "order": result.get(
                "order"
            )

        }
