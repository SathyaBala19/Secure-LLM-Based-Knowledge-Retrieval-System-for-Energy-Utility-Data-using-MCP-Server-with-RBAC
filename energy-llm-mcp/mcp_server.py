from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import duckdb
import os

app = FastAPI(title="MCP Server – Energy Utility")

# --- Paths ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "energy_utility.duckdb")

# 🔍 DEBUG: confirm tables
con = duckdb.connect(DB_PATH)
print("📊 Tables in DuckDB:", con.execute("SHOW TABLES").fetchall())
con.close()

# --- RBAC Rules ---
ROLE_POLICIES = {
    "customer_support": ["customers", "billing"],
    "operations": ["meters", "meter_readings"],
    "billing_analyst": ["billing", "meter_readings"],
    "finance": ["billing"],
    "admin": ["customers", "meters", "meter_readings", "billing"]
}

# --- Request Model ---
class QueryRequest(BaseModel):
    role: str
    table: str
    limit: int = 10

# --- API ---
@app.post("/query")
def run_query(req: QueryRequest):

    role = req.role
    table = req.table

    # Validate role
    if role not in ROLE_POLICIES:
        raise HTTPException(status_code=403, detail="Invalid role")

    # Enforce RBAC
    if table not in ROLE_POLICIES[role]:
        raise HTTPException(
            status_code=403,
            detail=f"Role '{role}' is not allowed to access '{table}'"
        )

    # Safe SQL (no user SQL allowed)
    sql = f"SELECT * FROM {table} LIMIT {req.limit}"

    # Execute query
    con = duckdb.connect(DB_PATH)
    result = con.execute(sql).fetchall()
    columns = [c[0] for c in con.description]
    con.close()

    return {
        "role": role,
        "table": table,
        "rows": [dict(zip(columns, row)) for row in result]
    }