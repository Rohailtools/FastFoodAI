
import re


class SynonymEngine:

    SYNONYMS = {

        "tika": "tikka",
        "tikkaa": "tikka",
        "chkn": "chicken",
        "chiken": "chicken",
        "chknn": "chicken",

        "zngr": "zinger",
        "zingr": "zinger",

        "fajitaa": "fajita",
        "fajta": "fajita",

        "piza": "pizza",
        "pizz": "pizza",

        "bbq": "barbecue",
        "bar b q": "barbecue",

        "frise": "fries",
        "fry": "fries",

        "&": "and",
        "+": "and"

    }


    @staticmethod
    def normalize(text: str):

        if not text:
            return ""

        text = text.lower()

        text = re.sub(
            r"[^\w\s]",
            " ",
            text
        )

        words = text.split()

        normalized = []

        for word in words:

            normalized.append(

                SynonymEngine.SYNONYMS.get(
                    word,
                    word
                )

            )

        return " ".join(normalized)
