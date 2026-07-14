
from app.db.client import supabase


class ContextBuilder:


    @staticmethod
    def build(
        restaurant_id: str = None
    ):

        if restaurant_id is None:

            restaurant_id = (
                "ed560f32-0cd5-41bd-a34c-8e6991623542"
            )


        context = []


        # Products load

        products_query = (
            supabase
            .table("products")
            .select("*")
            .eq(
                "restaurant_id",
                restaurant_id
            )
            .eq(
                "available",
                True
            )
            .execute()
        )


        products = products_query.data or []


        for product in products:

            context.append(
                {
                    "type": "product",
                    "name": product.get("name"),
                    "description": product.get("description"),
                    "price": product.get("price"),
                    "keywords": product.get("ai_keywords"),
                    "emoji": product.get("emoji")
                }
            )


        # Deals load

        deals_query = (
            supabase
            .table("deals")
            .select("*")
            .eq(
                "restaurant_id",
                restaurant_id
            )
            .eq(
                "active",
                True
            )
            .execute()
        )


        deals = deals_query.data or []


        for deal in deals:

            context.append(
                {
                    "type": "deal",
                    "name": deal.get("name"),
                    "description": deal.get("description"),
                    "price": deal.get("price"),
                    "emoji": "🔥"
                }
            )


        return context
