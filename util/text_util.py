from sentence_transformers import SentenceTransformer

# Load the model once at the module level
print("Loading MiniLM model...")
model = SentenceTransformer('all-MiniLM-L6-v2')

def encode_text(text: str):
    try:
        embedding = model.encode(text, convert_to_tensor=True)
        return embedding.tolist()
    except Exception as e:
        print(f"Error encoding text: {e}")
        raise