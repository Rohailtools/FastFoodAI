
from app.ai.order_extractor import OrderExtractor
from app.ai.cart_manager import CartManager
from app.ai.order_manager import OrderManager



class SmartOrderFlow:


    def __init__(self):

        self.extractor = OrderExtractor()



    def process(
        self,
        restaurant_id,
        customer_id,
        message
    ):


        extracted = self.extractor.extract(
            restaurant_id,
            message
        )


        for item in extracted.get(
            "items",
            []
        ):

            cart_item = {

                "product_id": item.get(
                    "product_id"
                ),

                "variant_id": item.get(
                    "variant_id"
                ),

                "variant": item.get(
                    "variant"
                ),

                "name": item.get(
                    "name"
                ),

                "quantity": item.get(
                    "quantity",
                    1
                ),

                "price": item.get(
                    "price",
                    0
                )

            }


            CartManager.add_item(
                customer_id,
                cart_item
            )



        cart = CartManager.get_cart(
            customer_id
        )



        if extracted.get(
            "order_confirmed"
        ):


            order_data = {

                "name": extracted.get(
                    "name",
                    "Guest"
                ),

                "phone": extracted.get(
                    "phone",
                    ""
                ),

                "address": extracted.get(
                    "address",
                    ""
                ),

                "order_confirmed": True,

                "items": cart

            }


            order = OrderManager.process_order(
                restaurant_id,
                order_data
            )


            return {

                "status": "completed",

                "cart": cart,

                "order": order

            }



        return {

            "status": "cart_updated",

            "cart": cart,

            "total": CartManager.get_total(
                customer_id
            )

        }
