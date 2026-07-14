
import re
from difflib import SequenceMatcher


class SearchUtils:

    @staticmethod
    def normalize(text: str) -> str:
        """
        Normalize customer text for searching.
        """

        if not text:
            return ""

        text = text.lower()

        text = text.replace("&", "and")

        text = re.sub(r"[^a-z0-9 ]", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()


    @staticmethod
    def similarity(a: str, b: str) -> float:
        """
        Fuzzy similarity between two strings.
        """

        return SequenceMatcher(
            None,
            SearchUtils.normalize(a),
            SearchUtils.normalize(b)
        ).ratio()


    @staticmethod
    def keyword_score(query, keywords):

        if not keywords:
            return 0

        score = 0

        query = SearchUtils.normalize(query)

        for keyword in keywords.split(","):

            keyword = SearchUtils.normalize(keyword)

            if not keyword:
                continue

            if keyword == query:
                score += 100

            elif keyword in query:
                score += 40

            score += int(
                SearchUtils.similarity(
                    query,
                    keyword
                ) * 25
            )

        return score


    @staticmethod
    def name_score(query, name):

        score = 0

        query = SearchUtils.normalize(query)

        name = SearchUtils.normalize(name)

        if query == name:
            score += 120

        elif query in name:
            score += 80

        elif name in query:
            score += 60

        score += int(
            SearchUtils.similarity(
                query,
                name
            ) * 50
        )

        return score


    @staticmethod
    def calculate_score(
        query,
        name,
        keywords=""
    ):

        return (
            SearchUtils.name_score(
                query,
                name
            )
            +
            SearchUtils.keyword_score(
                query,
                keywords
            )
        )
