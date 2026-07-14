
from datetime import datetime, timezone
import uuid

from app.db.client import supabase


class OrderService:


    @staticmethod
    def generate_order_number():

        short_id = str(uuid.uuid4().int)[:6]

        return f"ORD-{short_id}"



    @staticmethod
    def create_order(
        restaurant_id: str,
        customer_id: str,
        items: list,
        total: float
    ):


        order_number = OrderService.generate_order_number()


        order_data = {

            "restaurant_id": restaurant_id,

            "customer_id": customer_id,

            "order_number": order_number,

            "status": "Pending",

            "payment_status": "Pending",

            "subtotal": total,

            "delivery_fee": 0,

            "discount": 0,

            "total": total,

            "order_source": "whatsapp",

            "created_at": datetime.now(
                timezone.utc
            ).isoformat()

        }


        order_result = (
            supabase
            .table("orders")
            .insert(order_data)
            .execute()
        )


        if not order_result.data:

            raise Exception(
                "Order creation failed"
            )


        order = order_result.data[0]

        order_id = order["id"]


        order_items = []


        for item in items:


            quantity = item.get(
                "quantity",
                1
            )


            price = item.get(
                "price",
                0
            )


            item_data = {


                "order_id": order_id,


                "product_id": item.get(
                    "product_id"
                ),


                "quantity": quantity,


                "unit_price": price,


                "total_price": price * quantity,


                "notes":
                OrderService.build_item_note(
                    item
                )

            }


            item_result = (
                supabase
                .table("order_items")
                .insert(item_data)
                .execute()
            )


            if item_result.data:

                order_items.append(
                    item_result.data[0]
                )


        return {

            "order_id": order_id,

            "order_number": order_number,

            "customer_id": customer_id,

            "items": order_items,

            "total": total

        }



    @staticmethod
    def build_item_note(item):


        name = item.get(
            "name",
            ""
        )


        variant = item.get(
            "variant",
            ""
        )


        if variant:

            return f"{name} ({variant})"


        return name



    @staticmethod
    def get_order_by_id(
        order_id: str
    ):

        result = (
            supabase
            .table("orders")
            .select("*")
            .eq(
                "id",
                order_id
            )
            .execute()
        )


        if result.data:

            return result.data[0]


        return None



    @staticmethod
    def update_order_status(
        order_id: str,
        status: str
    ):


        result = (
            supabase
            .table("orders")
            .update(
                {
                    "status": status,

                    "updated_at":
                    datetime.now(
                        timezone.utc
                    ).isoformat()
                }
            )
            .eq(
                "id",
                order_id
            )
            .execute()
        )


        if result.data:

            return result.data[0]


        return None
