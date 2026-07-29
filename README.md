# 📄 Document Q&A Chatbot – Ask Anything

An AI-powered chatbot that enables users to upload PDF documents and ask questions in natural language. The application uses **Retrieval-Augmented Generation (RAG)** with **Google Gemini** to retrieve relevant information from the document and generate accurate answers.

---

## 🚀 Features

* 📄 Upload PDF documents
* 💬 Ask questions in natural language
* 🔍 Semantic search using Gemini Embeddings
* 🤖 AI-powered answers using Google Gemini
* ⚡ Fast document retrieval with LangChain
* 🎨 Interactive and user-friendly Streamlit interface
* 🧠 Session-based chat history

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Google Gemini**
* **Google Gemini Embeddings**
* **PyPDF**
* **In-Memory Vector Store**

---

## 📂 Project Structure

```text
pdf_chatbot/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
│── .env
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-chatbot.git
```

### 2. Navigate to the project

```bash
cd pdf-chatbot
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv env
env\Scripts\activate
```

**Linux/macOS**

```bash
python3 -m venv env
source env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

### 6. Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. Upload a PDF document.
2. The document is split into smaller chunks.
3. Gemini Embeddings convert the chunks into vector representations.
4. The vectors are stored in an in-memory vector database.
5. When a question is asked:

   * Relevant chunks are retrieved using semantic similarity.
   * The retrieved context is sent to Gemini.
   * Gemini generates an answer based on the document content.

---

## 📸 Screenshots

You can add screenshots here after deployment.

Example:

```
Home Screen
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/344283e2-a88e-4b47-bc46-afb478a3e7c2" />


Chat Interface
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/50cda0a3-08dd-4903-9fd9-04807c851b8c" />

---

## 🌟 Future Improvements

* Support multiple PDF uploads
* Display source page numbers
* Conversation memory
* Export chat history
* Support for DOCX and TXT files
* Persistent vector database (FAISS or ChromaDB)

---

## 👩‍💻 Author

**Mamidala Shivani**

GitHub:https://github.com/Shivanimamidala2005
LinkedIn: https://www.linkedin.com/in/shivani-mamidala/

---

## 📜 License

This project is intended for learning and educational purposes.
