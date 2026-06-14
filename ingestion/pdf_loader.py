from langchain_community.document_loaders import PyPDFLoader
import os

def load_pdf(pdf_path):

    if not os.path.exists(pdf_path):
        raise FileNotFoundError(
            f"PDF not found: {pdf_path}"
        )

    loader = PyPDFLoader(pdf_path)

    return loader.load()