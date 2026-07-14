
from app.ai.synonym_engine import SynonymEngine


class ProductRanker:


    @staticmethod
    def calculate_score(
        query,
        product
    ):

        if not query or not product:
            return 0


        query = SynonymEngine.normalize(
            query
        )


        name = SynonymEngine.normalize(
            product.get("name", "")
        )


        keywords = SynonymEngine.normalize(
            product.get(
                "ai_keywords",
                ""
            )
        )


        description = SynonymEngine.normalize(
            product.get(
                "description",
                ""
            )
        )


        score = 0


        # Exact name match
        if query in name:

            score += 100


        # Word matching
        query_words = query.split()


        for word in query_words:

            if word in name:

                score += 40


            if word in keywords:

                score += 25


            if word in description:

                score += 10


        # Featured products priority

        if product.get(
            "featured",
            False
        ):

            score += 5


        return score



    @staticmethod
    def find_best(
        query,
        products
    ):

        best_product = None
        best_score = 0


        for product in products:

            score = ProductRanker.calculate_score(
                query,
                product
            )


            if score > best_score:

                best_score = score
                best_product = product



        return {

            "product": best_product,

            "score": best_score

        }
