from fastapi import APIRouter
from app.db.client import supabase

router = APIRouter()


@router.get("/health")

async def health():

    try:

        supabase.table("restaurants").select("*").limit(1).execute()

        return {

            "status": "healthy",

            "database": "connected"

        }

    except Exception as e:

        return {

            "status": "error",

            "message": str(e)

        }
