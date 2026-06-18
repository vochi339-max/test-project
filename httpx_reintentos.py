from typing import Any, Dict, Optional, Tuple
from fastapi import File
from httpx._client import AsyncClient


async def post(
    *,
    url: str,
    files: Optional[Dict[str, File]] = None,
    json: Optional[Dict[str, Any]] = None,
    data: Optional[Dict[str, str]] = None,
    params: Optional[Dict[str, str]] = None,
    timeout: int = 10000
) -> Tuple[bool, Any]:
    try:
        async with AsyncClient() as client:
            response = await client.post(url, files=files, json=json, data=data, timeout=timeout)
            response = response.json() if response.status_code == 200 else None
            if not response:
                return False, None
            return True, response
    except Exception as e:
        print(e)
        return False, None

