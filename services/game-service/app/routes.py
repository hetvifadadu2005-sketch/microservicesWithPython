from fastapi import APIRouter, Request, HTTPException
import httpx
from fastapi.responses import Response

router = APIRouter()

ROUTES = {
    "users": "http://localhost:8001",
    "games": "http://localhost:8002",
}

@router.api_route("/v1/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE"])
async def proxy(service: str, path: str, request: Request):

    if service not in ROUTES:
        raise HTTPException(status_code=404, detail="Unknown service")

    url = f"{ROUTES[service]}/v1/{service}/{path}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(
                method=request.method,
                url=url,
                headers=request.headers.raw,
                content=await request.body()
            )

            return Response(
                content=response.content,
                status_code=response.status_code,
                headers=dict(response.headers)
            )

        except httpx.RequestError:
            raise HTTPException(status_code=503, detail="Service unavailable")