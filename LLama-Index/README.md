
# LlamaIndex Query Engine with Hugging Face and Llama3

This repository demonstrates how to build and query a vector-based search engine using the [LlamaIndex](https://gpt-index.readthedocs.io/) library. The script loads textual data, generates vector embeddings with Hugging Face models, and utilizes a Llama-based model for interactive queries.
<p align= "center">
  <img src = "https://github.com/user-attachments/assets/ec026edc-79a1-400a-b5aa-a488102da0de" style = "width : 600px; height : 300px" >
</p>

---

## **Features**

- Uses **Hugging Face embeddings** (`BAAI/bge-base-en-v1.5`) for semantic vector representation.
- Employs **Llama3** as the language model to process and refine query results.
- Simple text ingestion from a directory structure.
- Interactive querying with high semantic relevance.

---

## **Requirements**

Ensure you have the following Python libraries installed:

```bash
pip install llama-index huggingface_hub
```

---

## **How It Works**

### **1. Load Documents**

The script uses `SimpleDirectoryReader` to load all text documents from the `data` directory.


### **2. Configure Embeddings**

We use the Hugging Face model `BAAI/bge-base-en-v1.5` to generate text embeddings.

### **3. Build the Index**

Documents are processed into a **vector-based search index** using `VectorStoreIndex`.

### **4. Query the Index**

The search index is wrapped into a query engine for natural language queries. Queries are processed and refined using the `llama3` model.

---

## **Setup and Usage**

### **1. Clone the Repository**

```bash
git clone https://github.com/<your-username>/llama-index-query-engine.git
cd llama-index-query-engine
```

### **2. Prepare the Data**

- Place your text files in the `data/` directory.
- Each text file will be indexed for querying.

### **3. Run the Script**

```bash
python main.py
```

### **4. Query Example**

Modify the query in the script or input your own query:

```python
response = query_engine.query("What did the author do growing up?")
print(response)
```

### **5. Output**

The script will print the response inferred from the documents:

```text
Response: "The author engaged in various activities such as ..."
```

---

## **File Structure**

```plaintext
llama-index-query-engine/
|├── data/               # Directory for storing text files.
|├── main.py            # Main script to build and query the index.
|└── README.md          # Documentation.
```

---

## **Customization**

### **Changing the Embedding Model**

You can replace `BAAI/bge-base-en-v1.5` with any other Hugging Face embedding model:

```python
Settings.embed_model = HuggingFaceEmbedding(model_name="your-model-name")
```

### **Switching LLM**

To use a different Llama-based model:

```python
Settings.llm = Ollama(model="your-model-name")
```

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## **Acknowledgments**

- [LlamaIndex Documentation](https://gpt-index.readthedocs.io/)
- [Hugging Face](https://huggingface.co/)
- [Ollama](https://ollama.ai/)
