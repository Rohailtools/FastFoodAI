
class CartManager:


    carts = {}


    @staticmethod
    def get_cart(customer_id):

        if customer_id not in CartManager.carts:

            CartManager.carts[customer_id] = []

        return CartManager.carts[customer_id]



    @staticmethod
    def add_item(customer_id, item):


        cart = CartManager.get_cart(customer_id)


        product_id = item.get(
            "product_id"
        )

        variant_id = item.get(
            "variant_id"
        )


        for cart_item in cart:


            if (
                cart_item.get("product_id") == product_id
                and
                cart_item.get("variant_id") == variant_id
            ):


                cart_item["quantity"] += item.get(
                    "quantity",
                    1
                )

                return cart



        cart.append({

            "product_id": product_id,

            "variant_id": variant_id,

            "variant": item.get(
                "variant",
                ""
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

        })


        return cart



    @staticmethod
    def clear_cart(customer_id):

        CartManager.carts[customer_id] = []

        return True



    @staticmethod
    def get_total(customer_id):

        cart = CartManager.get_cart(customer_id)

        total = 0

        for item in cart:

            total += (
                item.get("price",0)
                *
                item.get("quantity",1)
            )

        return total
