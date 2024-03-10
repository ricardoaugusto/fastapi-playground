from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from fastapi.websockets import WebSocket

from services.chat import sync_websocket
from services.chat_html import html

router = APIRouter(prefix="/chat", tags=["chat"])

clients = []


@router.get("/")
async def get():
    return HTMLResponse(html)


@router.websocket("/sync")
async def websocket_endpoint(websocket: WebSocket):
    await sync_websocket(clients, websocket)
