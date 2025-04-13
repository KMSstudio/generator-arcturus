from fastapi import APIRouter
from model.version import VersionResponse

router = APIRouter(prefix="/version", tags=["Version"])

@router.get("/", response_model=VersionResponse)
async def get_version():
    return VersionResponse(version="0.0.1")
