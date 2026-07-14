
class VariantMatcher:


    VARIANTS = {

        "small": [
            "small",
            "sm",
            "chota",
            "choti"
        ],

        "medium": [
            "medium",
            "med",
            "normal",
            "regular"
        ],

        "large": [
            "large",
            "lg",
            "bara",
            "bari"
        ],

        "jumbo": [
            "jumbo",
            "xl",
            "extra large"
        ]

    }


    @staticmethod
    def detect_variant(
        text: str
    ):

        if not text:
            return None


        text = text.lower()


        for variant, words in VariantMatcher.VARIANTS.items():

            for word in words:

                if word in text:

                    return variant


        return None



    @staticmethod
    def match_product_variant(
        variants,
        requested_variant
    ):

        if not variants:
            return None


        if not requested_variant:
            return variants[0]


        for variant in variants:

            name = (
                variant
                .get("name", "")
                .lower()
            )


            if requested_variant in name:

                return variant


        return variants[0]
