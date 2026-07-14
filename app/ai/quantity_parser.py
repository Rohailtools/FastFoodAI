
import re


class QuantityParser:


    NUMBERS = {

        "ek": 1,
        "aik": 1,
        "one": 1,

        "do": 2,
        "two": 2,

        "teen": 3,
        "three": 3,

        "char": 4,
        "chaar": 4,
        "four": 4,

        "paanch": 5,
        "panch": 5,
        "five": 5

    }


    @staticmethod
    def extract_quantity(text: str):

        if not text:

            return 1


        text = text.lower()


        # Numeric quantity
        number = re.search(
            r"\b(\d+)\b",
            text
        )


        if number:

            return int(
                number.group(1)
            )


        # Roman Urdu quantity
        words = text.split()


        for word in words:

            if word in QuantityParser.NUMBERS:

                return QuantityParser.NUMBERS[word]


        return 1



    @staticmethod
    def remove_quantity(
        text: str
    ):

        if not text:

            return ""


        text = re.sub(
            r"\b\d+\b",
            "",
            text
        )


        words = text.split()


        words = [

            word

            for word in words

            if word not in QuantityParser.NUMBERS

        ]


        return " ".join(words).strip()
