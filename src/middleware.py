from fastapi import Request
import logging

class CustomMiddleware:
    def __init__(self):
        logging.basicConfig(filename="api.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

    async def __call__(self, request: Request, call_next):
        response = await call_next(request)
        logging.info(f"method:{request.method} url:{request.url} status_code:{response.status_code}")
        return response