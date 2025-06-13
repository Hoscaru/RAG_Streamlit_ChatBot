from fastapi import FastAPI




app = FastAPI(title="RAG Chatbot API")



@app.get("/test")
async def test():
    return {"message": "Hello, World!"}