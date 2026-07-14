
from app.ai.product_loader import ProductLoader
from app.ai.product_ranker import ProductRanker
from app.ai.quantity_parser import QuantityParser
from app.ai.variant_matcher import VariantMatcher



class ProductSearch:


    @staticmethod
    def search(
        restaurant_id: str,
        query: str
    ):


        quantity = QuantityParser.extract_quantity(
            query
        )


        clean_query = QuantityParser.remove_quantity(
            query
        )


        variant = VariantMatcher.detect_variant(
            query
        )


        products = ProductLoader.get_products(
            restaurant_id
        )


        deals = ProductLoader.get_deals(
            restaurant_id
        )


        all_items = []


        for product in products:

            product["_type"] = "product"

            all_items.append(product)



        for deal in deals:

            deal["_type"] = "deal"

            all_items.append(deal)



        result = ProductRanker.find_best(
            clean_query,
            all_items
        )


        item = result.get("product")


        score = result.get(
            "score",
            0
        )


        if not item or score < 40:

            return {

                "matched": False,
                "score": score,
                "data": None

            }



        # VARIANT PRICE FIX

        selected_variant = None


        if variant and item.get("variants"):


            for v in item["variants"]:

                if v["name"].lower() == variant.lower():

                    selected_variant = v

                    break



        if selected_variant:

            item["selected_variant"] = selected_variant["name"]

            item["price"] = selected_variant["price"]

            item["variant_id"] = selected_variant["id"]



        return {

            "matched": True,

            "type": item.get("_type"),

            "quantity": quantity,

            "variant": variant,

            "score": score,

            "data": item

        }
