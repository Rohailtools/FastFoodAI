
from app.services.customer_service import CustomerService
from app.services.order_service import OrderService
from app.ai.cart_manager import CartManager



class OrderManager:


    @staticmethod
    def process_order(
        restaurant_id: str,
        order_data: dict
    ):


        if not order_data.get(
            "order_confirmed"
        ):

            return {

                "status": "waiting_confirmation",

                "message": "Order confirmation pending"

            }



        if not order_data.get(
            "items"
        ):

            return {

                "status": "failed",

                "message": "No items found"

            }



        customer = CustomerService.get_or_create_customer(

            restaurant_id,

            order_data.get(
                "name",
                "Guest"
            ),

            order_data.get(
                "phone",
                ""
            ),

            order_data.get(
                "address",
                ""
            )

        )



        order = OrderService.create_order(

            restaurant_id,

            customer["id"],

            order_data["items"],

            OrderManager.calculate_total(
                order_data["items"]
            )

        )



        # Clear cart after successful order
        if order.get("order_id"):

            CartManager.clear_cart(
                customer["id"]
            )



        return {

            "status": "success",

            "customer": customer,

            "order": order

        }



    @staticmethod
    def calculate_total(
        items
    ):

        total = 0


        for item in items:


            total += (

                item.get(
                    "price",
                    0
                )

                *

                item.get(
                    "quantity",
                    1
                )

            )


        return total
