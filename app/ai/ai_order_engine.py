
from app.ai.customer_memory import CustomerMemory
from app.ai.repeat_order import RepeatOrder
from app.ai.smart_order_flow import SmartOrderFlow



class AIOrderEngine:



    def __init__(self):

        self.order_flow = SmartOrderFlow()



    def process_message(
        self,
        restaurant_id,
        phone,
        message
    ):


        # Find customer

        customer = CustomerMemory.find_customer(

            restaurant_id,

            phone

        )



        # Create new customer if missing

        if not customer:


            customer = CustomerMemory.remember_customer(

                restaurant_id,

                {

                    "name": "Guest",

                    "phone": phone,

                    "address": ""

                }

            )



        customer_id = customer["id"]



        # Repeat order

        if RepeatOrder.is_repeat_request(

            message

        ):


            last_order = RepeatOrder.get_last_order(

                customer_id

            )


            return {

                "type": "repeat_order",

                "reply":

                RepeatOrder.create_repeat_summary(

                    last_order

                )

            }



        # Normal order

        result = self.order_flow.process(

            restaurant_id,

            customer_id,

            message

        )


        return {

            "type": result.get(
                "status"
            ),

            "reply": self.generate_reply(
                result
            ),

            "data": result

        }



    def generate_reply(
        self,
        result
    ):


        status = result.get(
            "status"
        )



        if status == "cart_updated":


            return (

                "Aapka order cart mein add ho gaya hai 😊\n\n"

                + self.cart_text(
                    result.get(
                        "cart",
                        []
                    )
                )

                + "\n\nKya ye order confirm kar doon? ✅"

            )



        if status == "waiting_name":

            return "Apna naam bata dein 😊"



        if status == "waiting_address":

            return "Delivery address share kar dein 📍"



        if status == "completed":

            return "Aapka order confirm ho gaya hai ✅"



        return "Aapki help kar deta hun 😊"



    def cart_text(
        self,
        cart
    ):


        text = ""


        for item in cart:


            text += (

                f"🍕 {item['name']} "
                f"x {item['quantity']}\n"

            )


        return text
