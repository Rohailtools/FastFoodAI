from app.db.client import supabase


class ProductService:
    """Service class for Product operations."""

    @staticmethod
    def get_all_products():
        """Get all available products."""
        response = (
            supabase.table("products")
            .select("*")
            .eq("available", True)
            .order("name")
            .execute()
        )
        return response.data

    @staticmethod
    def get_product_by_id(product_id: str):
        """Get a product by ID."""
        response = (
            supabase.table("products")
            .select("*")
            .eq("id", product_id)
            .single()
            .execute()
        )
        return response.data

    @staticmethod
    def create_product(product_data: dict):
        """Create a new product."""
        response = (
            supabase.table("products")
            .insert(product_data)
            .execute()
        )
        return response.data

    @staticmethod
    def update_product(product_id: str, product_data: dict):
        """Update an existing product."""
        response = (
            supabase.table("products")
            .update(product_data)
            .eq("id", product_id)
            .execute()
        )
        return response.data

    @staticmethod
    def delete_product(product_id: str):
        """Delete a product."""
        response = (
            supabase.table("products")
            .delete()
            .eq("id", product_id)
            .execute()
        )
        return response.data

    @staticmethod
    def search_products(keyword: str):
        """Search products by name."""
        response = (
            supabase.table("products")
            .select("*")
            .ilike("name", f"%{keyword}%")
            .eq("available", True)
            .execute()
        )
        return response.data

    @staticmethod
    def get_products_by_category(category_id: str):
        """Get all available products in a category."""
        response = (
            supabase.table("products")
            .select("*")
            .eq("category_id", category_id)
            .eq("available", True)
            .order("name")
            .execute()
        )
        return response.data

    @staticmethod
    def get_featured_products():
        """Get featured products."""
        response = (
            supabase.table("products")
            .select("*")
            .eq("featured", True)
            .eq("available", True)
            .order("name")
            .execute()
        )
        return response.data
