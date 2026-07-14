
from app.ai.customer_memory import CustomerMemory
from app.ai.repeat_order import RepeatOrder
from app.ai.order_extractor import OrderExtractor
from app.ai.response_generator import ResponseGenerator



class ConversationManager:



    def __init__(self):

        self.extractor = OrderExtractor()

        self.generator = ResponseGenerator()



    def handle_message(
        self,
        restaurant_id,
        customer_id,
        message
    ):


        response_data = {

            "type": "",

            "reply": "",

            "order": None

        }



        # Repeat order check

        if RepeatOrder.is_repeat_request(
            message
        ):


            last_order = RepeatOrder.get_last_order(

                customer_id

            )


            response_data["type"] = "repeat_order"


            response_data["reply"] = (

                RepeatOrder
                .create_repeat_summary(
                    last_order
                )

            )


            return response_data



        # Normal order extraction


        order_data = self.extractor.extract(

            restaurant_id,

            message

        )


        response_data["order"] = order_data



        if order_data.get(
            "items"
        ):


            response_data["type"] = "new_order"


            response_data["reply"] = self.generator.generate(

                message,

                order_data

            )


            return response_data



        # General message


        response_data["type"] = "chat"


        response_data["reply"] = self.generator.generate(

            message

        )


        return response_data
