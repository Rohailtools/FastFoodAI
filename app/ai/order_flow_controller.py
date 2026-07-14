
from app.ai.order_extractor import OrderExtractor
from app.ai.order_manager import OrderManager
from app.ai.response_generator import ResponseGenerator



class OrderFlowController:


    sessions = {}


    def __init__(self):

        self.extractor = OrderExtractor()

        self.generator = ResponseGenerator()



    def handle(
        self,
        restaurant_id,
        customer_id,
        message
    ):


        if customer_id not in self.sessions:

            self.sessions[customer_id] = {

                "name": "",

                "phone": "",

                "address": "",

                "items": [],

                "confirmed": False

            }



        session = self.sessions[customer_id]



        extracted = self.extractor.extract(

            restaurant_id,

            message

        )



        # Save customer info

        if extracted.get("name"):

            session["name"] = extracted["name"]



        if extracted.get("phone"):

            session["phone"] = extracted["phone"]



        if extracted.get("address"):

            session["address"] = extracted["address"]



        # Save items

        if extracted.get("items"):

            session["items"].extend(

                extracted["items"]

            )



        # Confirmation

        if extracted.get(
            "order_confirmed"
        ):

            session["confirmed"] = True



        # Missing information check


        if not session["name"]:

            return {

                "status": "waiting_name",

                "reply": "Apna naam bata dein 😊"

            }



        if not session["address"]:

            return {

                "status": "waiting_address",

                "reply": "Delivery address share kar dein 📍"

            }



        if not session["items"]:

            return {

                "status": "waiting_order",

                "reply": "Kya order karna hai batayein 🍕"

            }



        if not session["confirmed"]:


            return {

                "status": "waiting_confirmation",

                "reply": self.generator.generate(

                    message,

                    session

                )

            }



        # Final order ready


        order = OrderManager.process_order(

            restaurant_id,

            session

        )


        return {

            "status": "completed",

            "reply": "Aapka order confirm ho gaya hai ✅",

            "order": order

        }
