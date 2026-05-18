from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {
        "message": "Customer Support API Running"
    }

@app.post("/chat")
def chat(query: str):

    return {
        "response": f"Received query: {query}"
    }
