from fastapi import FastAPI, Request
import uvicorn

from tasks import process_message_and_respond

app = FastAPI()


@app.post("/api/v0/telegram/webhook")
async def telegram_webhook(request: Request):
    update = await request.json()
    if "message" in update and "text" in update["message"]:
        chat_id = update["message"]["chat"]["id"]
        message_text = update["message"]["text"]
        message = {"chat_id": chat_id, "message_text": message_text}
        process_message_and_respond.delay(chat_id, message)
        return {"status": "Message received and queued for processing"}
    return {"status": "No message content found"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, reload=True)
