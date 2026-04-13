import httpx
from fastapi import HTTPException

GENDERIZE_API_URL = "https://api.genderize.io"

async def fetch_gender_prediction(name:str)->dict:
    """
    """
    async with httpx.AsyncClient(timeout=2.0) as client:
        try:
            response = await client.get(f"{GENDERIZE_API_URL}/", params={"name":name})

            response.raise_for_status()

            return response.json()
        except httpx.TimeoutException:
            raise HTTPException(
                status_code= 504,
                detail="Gateway Timeout: The external API took too long to respond"
            )
        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code = 502,
                detail=f"Bad Gateway: External API returned an error ({exc.response.status_code})"
            )
        except httpx.RequestError:
            raise HTTPException(
                status_code=502,
                detail= "Bad Gateway: Could not connect to external API"
            )
