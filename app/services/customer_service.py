
from datetime import datetime, timezone
import uuid

from app.db.client import supabase


class CustomerService:
    """
    Customer management service.

    Responsibilities:
    - Find customer by WhatsApp number
    - Create new customer
    - Update existing customer information
    - Maintain restaurant isolation
    """


    @staticmethod
    def generate_customer_code():
        """
        Future friendly customer display code.
        Example: C12345
        """

        return "C" + str(uuid.uuid4().int)[:5]



    @staticmethod
    def get_customer_by_phone(
        restaurant_id: str,
        phone: str
    ):
        """
        Find customer using WhatsApp number.

        Phone lookup is customer facing.
        Internal relations use UUID.
        """

        result = (
            supabase
            .table("customers")
            .select("*")
            .eq("restaurant_id", restaurant_id)
            .eq("whatsapp_number", phone)
            .execute()
        )


        if result.data:
            return result.data[0]


        return None



    @staticmethod
    def create_customer(
        restaurant_id: str,
        name: str,
        phone: str,
        address: str = None,
        voice_address: bool = False
    ):
        """
        Create new customer record.
        """


        customer_data = {

            "restaurant_id": restaurant_id,

            "full_name": name,

            "whatsapp_number": phone,

            "delivery_address": address,

            "notes": "",

            "preferred_language": "roman_urdu",

            "voice_address": voice_address,

            "last_seen": datetime.now(
                timezone.utc
            ).isoformat()

        }


        result = (
            supabase
            .table("customers")
            .insert(customer_data)
            .execute()
        )


        if not result.data:
            raise Exception(
                "Customer creation failed"
            )


        return result.data[0]



    @staticmethod
    def update_customer(
        customer_id: str,
        data: dict
    ):
        """
        Update customer information.
        """


        data["updated_at"] = (
            datetime.now(
                timezone.utc
            ).isoformat()
        )


        result = (
            supabase
            .table("customers")
            .update(data)
            .eq("id", customer_id)
            .execute()
        )


        if result.data:
            return result.data[0]


        return None



    @staticmethod
    def update_last_seen(
        customer_id: str
    ):
        """
        Update customer activity time.
        """


        return (
            CustomerService
            .update_customer(
                customer_id,
                {
                    "last_seen":
                    datetime.now(
                        timezone.utc
                    ).isoformat()
                }
            )
        )



    @staticmethod
    def get_or_create_customer(
        restaurant_id: str,
        name: str,
        phone: str,
        address: str = None,
        voice_address: bool = False
    ):
        """
        Main customer flow.

        Existing customer:
            return customer

        New customer:
            create customer
        """


        customer = (
            CustomerService
            .get_customer_by_phone(
                restaurant_id,
                phone
            )
        )


        if customer:

            CustomerService.update_last_seen(
                customer["id"]
            )

            return customer



        return (
            CustomerService
            .create_customer(
                restaurant_id,
                name,
                phone,
                address,
                voice_address
            )
        )
