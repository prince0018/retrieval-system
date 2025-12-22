from fastapi import FastAPI
from src.index_api import router as index_router
from fastapi import FastAPI
from src.index_api import router as index_router
from src.pdf_ingest_api import router as pdf_router
from src.document_api import router as document_router





app = FastAPI(title="Index Management API")
app.include_router(index_router, prefix="/indices")
app.include_router(pdf_router)
app.include_router(document_router)
app.include_router(index_router, prefix="/indices")
#checking..