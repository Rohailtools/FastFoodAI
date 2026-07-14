
from app.db.client import supabase



class CustomerMemory:


    @staticmethod
    def find_customer(
        restaurant_id,
        phone
    ):

        if not phone:

            return None



        result = (

            supabase
            .table("customers")
            .select("*")
            .eq(
                "restaurant_id",
                restaurant_id
            )
            .eq(
                "whatsapp_number",
                phone
            )
            .execute()

        )


        if result.data:

            return result.data[0]


        return None



    @staticmethod
    def remember_customer(
        restaurant_id,
        customer_data
    ):


        existing = CustomerMemory.find_customer(

            restaurant_id,

            customer_data.get(
                "phone",
                ""
            )

        )


        # Existing customer

        if existing:

            update = (

                supabase
                .table("customers")
                .update({

                    "full_name":
                    customer_data.get(
                        "name",
                        existing.get(
                            "full_name"
                        )
                    ),

                    "delivery_address":
                    customer_data.get(
                        "address",
                        existing.get(
                            "delivery_address"
                        )
                    ),

                    "last_seen":
                    "now()"

                })
                .eq(
                    "id",
                    existing["id"]
                )
                .execute()

            )


            return update.data[0]



        # New customer

        new_customer = (

            supabase
            .table("customers")
            .insert({

                "restaurant_id":
                restaurant_id,


                "full_name":
                customer_data.get(
                    "name",
                    "Guest"
                ),


                "whatsapp_number":
                customer_data.get(
                    "phone",
                    ""
                ),


                "delivery_address":
                customer_data.get(
                    "address",
                    ""
                ),


                "preferred_language":
                "roman_urdu"

            })
            .execute()

        )


        return new_customer.data[0]



    @staticmethod
    def get_last_order(
        customer_id
    ):


        result = (

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


        if result.data:

            return result.data[0]


        return None
