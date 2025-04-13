from fastapi import APIRouter
from model.chat import PromptRequest, PromptResponse
from service.openai_service import get_openai_response

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=PromptResponse)
async def chat(req: PromptRequest):
    return await get_openai_response(req.prompt)
