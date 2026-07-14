from app.db.client import supabase


class ProductService:
    """Service class for Product operations."""

    @staticmethod
    def get_all_products():
        response = (
            supabase.table("products")
            .select("*")
            .eq("available", True)
            .order("name")
            .execute()
        )
        return response.data


    @staticmethod
    def get_products_with_variants():
        """
        Get products with their pricing variants.
        Used by AI menu engine.
        """

        products = (
            supabase.table("products")
            .select("*")
            .eq("available", True)
            .order("name")
            .execute()
        ).data


        formatted_products = []

        for product in products:

            variants = (
                supabase.table("product_variants")
                .select("*")
                .eq("product_id", product["id"])
                .eq("is_available", True)
                .execute()
            ).data


            product["variants"] = variants

            # fallback price
            if product.get("price", 0) == 0 and variants:
                product["display_price"] = min(
                    v["price"] for v in variants
                )
            else:
                product["display_price"] = product.get("price", 0)


            formatted_products.append(product)


        return formatted_products
