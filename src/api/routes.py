from fastapi import APIRouter, Response, HTTPException
from src.services import make_call, get_call_status

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "AI Voice Agent API is running!"}

@router.get("/call/{phone_number}")
async def run_call(phone_number: str):
    call = make_call(phone_number)
    if call:
        return Response(content=f"Voice call initiated to {phone_number} \n Call SID: {call.sid}")
    else:
        raise HTTPException(status_code=500, detail="Failed to initiate voice call")
    
@router.get("/call/status/{call_sid}")
async def call_status(call_sid: str):
    status = get_call_status(call_sid)
    if status:
        return Response(content=f"Call status: {status}")
    else:
        raise HTTPException(status_code=404, detail="Call not found")
     