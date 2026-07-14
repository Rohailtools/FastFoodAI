
from app.db.client import supabase


class ProductLoader:


    @staticmethod
    def get_products(
        restaurant_id: str
    ):

        result = (
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

        products = result.data or []


        # attach variants
        for product in products:

            variants = (
                supabase
                .table("product_variants")
                .select("*")
                .eq(
                    "product_id",
                    product["id"]
                )
                .eq(
                    "is_available",
                    True
                )
                .execute()
            )


            product["variants"] = variants.data or []


        return products



    @staticmethod
    def get_deals(
        restaurant_id: str
    ):

        result = (
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

        return result.data or []



    @staticmethod
    def get_product_by_id(
        product_id: str
    ):

        result = (
            supabase
            .table("products")
            .select("*")
            .eq(
                "id",
                product_id
            )
            .execute()
        )


        if result.data:
            product = result.data[0]


            variants = (
                supabase
                .table("product_variants")
                .select("*")
                .eq(
                    "product_id",
                    product_id
                )
                .execute()
            )


            product["variants"] = variants.data or []


            return product


        return None



    @staticmethod
    def get_deal_by_id(
        deal_id: str
    ):

        result = (
            supabase
            .table("deals")
            .select("*")
            .eq(
                "id",
                deal_id
            )
            .execute()
        )


        if result.data:
            return result.data[0]


        return None
