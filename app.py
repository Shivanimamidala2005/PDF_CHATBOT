from dotenv import load_dotenv
load_dotenv() 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter 
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import InMemoryVectorStore 
from google import genai
import os
import streamlit as st
from time import sleep

llm=ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "messages" not in st.session_state:
    st.session_state.messages = []


def normalize_content(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                if isinstance(item.get("text"), str):
                    parts.append(item["text"])
                elif isinstance(item.get("content"), (str, list, dict)):
                    parts.append(normalize_content(item["content"]))
                elif item.get("type") == "text" and isinstance(item.get("text"), str):
                    parts.append(item["text"])
                else:
                    parts.append(str(item))
            else:
                parts.append(str(item))
        return "".join(parts)
    if hasattr(content, "content"):
        return normalize_content(content.content)
    return str(content)


def normalize_text(text):
    return " ".join(str(text).strip().lower().split())


def document_process(path):
    ##document loading 
    loader = PyPDFLoader(path)
    docs = loader.load()
    ##splitting the document into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    docs = splitter.split_documents(docs)

    ##embedding the document chunks and vector store creation
    embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
    vector_db=InMemoryVectorStore.from_documents(documents=docs, embedding=embeddings)
    st.session_state.vector_db = vector_db
    st.session_state.document_uploaded = True


# answer=llm.invoke(prompt)

# print("Answer:", answer.content)


st.subheader("Document Q&A Chatbot - Ask Anything")
if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False


###document upload and processing 
if not st.session_state.document_uploaded:
    file=st.file_uploader("Upload a PDF document", type="pdf")
    if file:
        with open("uploaded_document.pdf", "wb") as f:
            f.write(file.getvalue())
        with st.spinner("Processing the document..."):
            document_process("./uploaded_document.pdf")
        st.markdown("Document processed successfully! You can now ask questions about the document.")
        sleep(2)
        st.rerun()
if st.session_state.document_uploaded and st.session_state.vector_db:
    for oneMessage in st.session_state.messages:
        role=oneMessage["role"]
        content=normalize_content(oneMessage["content"])
        st.chat_message(role).markdown(content)

    query=st.chat_input("Ask a question about the document")
    if query:
        st.session_state.messages.append({"role": "user", "content": query})
        st.chat_message("user").markdown(query)
        search_query = normalize_text(query)
        documents=st.session_state.vector_db.similarity_search(query=search_query, k=4)
        context=""

        for doc in documents:
            context+=doc.page_content+"\n\n"
        prompt = f"""
        You are a helpful assistant.

        Answer only from the given context.
        If the answer is not available in the context, reply:
        "I couldn't find that information in the document."

        Context:
        {context}

        Question:
        {query}
        """
        result=llm.invoke(prompt)
        assistant_content = normalize_content(result.content)

        st.session_state.messages.append({"role": "assistant", "content": assistant_content})
        st.chat_message("assistant").markdown(assistant_content)
