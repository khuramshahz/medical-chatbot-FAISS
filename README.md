🏥 Medical Chatbot – FAISS-based Question Answering

This project is an AI-powered Medical Chatbot that uses **FAISS for similarity search** and **semantic search on custom medical data**. It includes notebooks for embedding generation and a FastAPI backend to serve responses.

📁 Project Structure

medical-chatbot/
├── app/
│   ├── main.py               # Main FastAPI server
│   ├── model/
│   │   ├── index.faiss       # FAISS index (copy from notebook)
│   │   └── qa_answers.json   # Corresponding answers (copy from notebook)
├── embeddings/
│   └── generate_embeddings.ipynb  # Notebook to create FAISS index
├── requirements.txt
├── .gitattributes            # Git LFS configuration
└── README.md

🚀 How to Run the Project
Clone the Repository
git clone https://github.com/khuramshahz/medical-chatbot_FAISS.git
cd medical-chatbot_FAISS

Install Required Packages

Create and activate a virtual environment (optional but recommended):
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

Install dependencies:

pip install -r requirements.txt
> If you haven't installed Git LFS before, run:
git lfs install

3. **Run the Notebook to Generate Embeddings**

Open the notebook:
cd embeddings
Open `generate_embeddings.ipynb` in Jupyter:
Run all cells to generate:
index.faiss
qa_answers.json

4. Move Files to `model/` Folder
After generating the files, move them like this
cp index.faiss ../app/model/
cp qa_answers.json ../app/model/
Or manually copy them from the notebook output directory into:
medical-chatbot_FAISS/app/model/

5. Run the Chatbot Backend
Go back to the main directory and run the API:
cd ../app
python main.py


You should see:
Uvicorn running on http://127.0.0.1:8000

Now visit `http://127.0.0.1:8000` to test your chatbot, or use the `/docs` path to interact with the API via Swagger UI.

💡 Notes
Large files (like `index.faiss`) are tracked using Git LFS.
You can extend this chatbot with a frontend, voice interface, or more advanced NLP models.
