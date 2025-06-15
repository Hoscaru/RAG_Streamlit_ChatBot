import os
from pathlib import Path
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter



PERSIST_DIR="./server/chroma_store"
UPLOAD_DIR="./server/uploaded_pdfs"
os.makedirs(UPLOAD_DIR,exist_ok=True)


def load_vectorstore(uploaded_files):
    file_paths=[]


    for file in uploaded_files:
        save_path=Path(UPLOAD_DIR)/file.filename
        with open(save_path,"wb") as f:
            f.write(file.file.read())
        file_paths.append(str(save_path))

    docs=[]
    for path in file_paths:
        loader=PyPDFLoader(path)
        docs.extend(loader.load())

    splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    texts=splitter.split_documents(docs)

    embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L12-v2")


    if os.path.exists(PERSIST_DIR) and os.listdir(PERSIST_DIR):
        vectorstore=Chroma(persist_directory=PERSIST_DIR,embedding_function=embeddings)
        vectorstore.add_documents(texts)
        
    else:
        vectorstore=Chroma.from_documents(
            documents=texts,
            embedding=embeddings,
            persist_directory=PERSIST_DIR
        )
        

    return vectorstore