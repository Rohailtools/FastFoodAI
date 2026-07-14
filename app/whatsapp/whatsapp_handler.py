
from app.ai.order_extractor import OrderExtractor
from app.ai.response_generator import ResponseGenerator
from app.ai.order_manager import OrderManager



class WhatsAppHandler:


    def __init__(self):

        self.extractor = OrderExtractor()

        self.generator = ResponseGenerator()



    def process_message(
        self,
        restaurant_id: str,
        message: str
    ):


        # Step 1: Extract order data

        order_data = self.extractor.extract(

            restaurant_id,

            message

        )


        # Step 2: Save order if confirmed

        if order_data.get(
            "order_confirmed"
        ):


            order_result = OrderManager.process_order(

                restaurant_id,

                order_data

            )


            order_data["saved_order"] = order_result



        # Step 3: Generate reply

        reply = self.generator.generate(

            message,

            order_data

        )


        return {

            "reply": reply,

            "order_data": order_data

        }
