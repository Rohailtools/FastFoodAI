
import re

from app.ai.product_search import ProductSearch


class OrderExtractor:


    def extract(
        self,
        restaurant_id,
        message
    ):

        result = {
            "name": "",
            "phone": "",
            "address": "",
            "voice_address": False,
            "items": [],
            "order_confirmed": False
        }


        text = message.lower()



        # confirmation

        if any(word in text for word in [
            "confirm",
            "haan",
            "yes",
            "ok",
            "kar do",
            "bhej do"
        ]):

            result["order_confirmed"] = True



        # phone

        phone_match = re.search(
            r"03\d{9}",
            message
        )

        if phone_match:

            result["phone"] = phone_match.group(0)



        # name

        name_match = re.search(
            r"mera naam\s+(.*?)\s+(?:hai|address)",
            text
        )

        if name_match:

            result["name"] = (
                name_match.group(1)
                .strip()
                .title()
            )



        # product

        product = ProductSearch.search(
            restaurant_id,
            message
        )


        product_name = ""

        variant_name = ""


        if product.get("matched"):


            item = product["data"]

            product_name = item.get(
                "name",
                ""
            ).lower()


            variant_name = str(
                item.get(
                    "selected_variant",
                    ""
                )
            ).lower()



            result["items"].append({

                "product_id": item.get("id"),

                "variant_id": item.get("variant_id"),

                "variant": item.get("selected_variant"),

                "name": item.get("name"),

                "quantity": 1,

                "price": item.get("price",0)

            })



        # address clean

        address = text


        remove_list = [
            "mera naam",
            result["name"].lower(),
            "hai",
            "address",
            result["phone"],
            product_name,
            variant_name,
            "confirm",
            "haan",
            "yes",
            "ok"
        ]


        for word in remove_list:

            if word:

                address = address.replace(
                    word,
                    ""
                )



        result["address"] = (
            address
            .strip()
            .title()
        )



        return result
