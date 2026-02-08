import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MCP_URL = "http://127.0.0.1:8000/query"

MODEL = "mistral"

def ask_llm(question):
    prompt = f"""
You are an assistant for an energy utility company.

User question:
"{question}"

Decide which table is needed to answer the question.
Choose ONE from:
- customers
- meters
- meter_readings
- billing

Reply ONLY in JSON like:
{{"table": "<table_name>"}}
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return json.loads(response.json()["response"])


def query_mcp(role, table):
    payload = {
        "role": role,
        "table": table,
        "limit": 5
    }

    response = requests.post(MCP_URL, json=payload)
    return response.json()

def explain_results(question, rows):
    prompt = f"""
You are an energy utility analyst.

User question:
"{question}"

Here is the data returned from the system:
{rows}

Explain the result in simple, clear English.
Do NOT mention SQL or databases.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

if __name__ == "__main__":
    role = "operations"
    question = "Which meters have recent readings?"

    llm_decision = ask_llm(question)
    table = llm_decision["table"]

    print("🧠 LLM selected table:", table)

    mcp_result = query_mcp(role, table)

    explanation = explain_results(question, mcp_result["rows"])

    print("\n📊 Data:")
    print(json.dumps(mcp_result["rows"], indent=2))

    print("\n📝 Explanation:")
    print(explanation)