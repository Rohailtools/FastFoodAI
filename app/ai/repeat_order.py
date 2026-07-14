
from app.db.client import supabase



class RepeatOrder:



    @staticmethod
    def is_repeat_request(
        message
    ):


        text = message.lower()


        keywords = [

            "same order",

            "wahi order",

            "pichla order",

            "last order",

            "repeat",

            "dobara",

            "phir se",

            "wahi bhej do"

        ]


        for word in keywords:

            if word in text:

                return True


        return False



    @staticmethod
    def get_last_order(
        customer_id
    ):


        order = (

            supabase
            .table("orders")
            .select(
                "*"
            )
            .eq(
                "customer_id",
                customer_id
            )
            .order(
                "created_at",
                desc=True
            )
            .limit(1)
            .execute()

        )


        if not order.data:

            return None


        order_data = order.data[0]



        items = (

            supabase
            .table("order_items")
            .select(
                "*"
            )
            .eq(
                "order_id",
                order_data["id"]
            )
            .execute()

        )


        return {

            "order": order_data,

            "items": items.data

        }



    @staticmethod
    def create_repeat_summary(
        last_order
    ):


        if not last_order:

            return "Aapka koi purana order nahi mila 😊"



        text = "Aapka last order tha:\n"



        for item in last_order.get(
            "items",
            []
        ):


            text += (

                f"🍕 {item.get('notes')} "

                f"x {item.get('quantity')}\n"

            )


        text += "\nKya ye order dobara kar doon? 😊"


        return text
