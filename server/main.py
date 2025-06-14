from fastapi import FastAPI, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from modules.load_vectorstore import load_vectorstore
from modules.llm import get_llm_chain
from modules.query_handlers import query_chain
from logger import logger


app = FastAPI(title="RAG Chatbot API")

# allow frontend

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as exc:
        logger.exception(f"Unhandled exception")
        return JSONResponse(
            status_code=500,
            content={"error": str(exc)},
        )

@app.post("/upload_pdfs/")

async def upload_pdfs(files: List[UploadFile] = File(...)):
    try:
        logger.info(f"recieved {len(files)} files")
        logger.info("documents added to chroma")
        return {"message": "Files processed and vector store updated."}
    except Exception as e:
        logger.exception("Error during pdf upload")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)},
        )

@app.post("/ask/")
async def ask_question(question: str = Form(...))
    try:
        logger.info("User query: {question}")
        from langchain.vectorstores import Chroma
        from langchain.embeddings import HuggingFaceBgeEmbeddings
        from modules.load_vectorstore import PERSIST_DIR

        vectorstore = Chroma(
            persist_directory=PERSIST_DIR,
            embedding_function=HuggingFaceBgeEmbeddings(model_name="all-MiniLM-L12-v2"),
        )
        chain = get_llm_chain(vectorstore)
        result = query_chain(chain, question)
        logger.info("query successfull")
    except Exception as e:
        logger.exception("Error processing question")
        return JSONResponse(
            status_code=500,
            content={"error": str(e)},
        )
        

@app.get("/test")
async def test():
    return {"message": "Hello, World!"}