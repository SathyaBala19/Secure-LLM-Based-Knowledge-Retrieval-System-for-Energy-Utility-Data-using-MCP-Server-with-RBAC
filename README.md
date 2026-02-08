Secure LLM-Based Knowledge Retrieval System for Energy Utility Data
Using MCP Server with Role-Based Access Control (RBAC)

Abstract
This project presents a secure, offline Large Language Model (LLM) based knowledge retrieval system for energy utility data. The system ensures that the LLM never directly accesses sensitive data. Instead, a Model Control Plane (MCP) server enforces Role-Based Access Control (RBAC) before allowing any database query. The architecture separates intelligence, access control, and data storage to prevent data leakage and align with enterprise security best practices.

Introduction
Large Language Models provide powerful natural language interfaces but introduce security risks when connected directly to enterprise databases. This project addresses those risks by introducing an intermediary MCP server that validates permissions before executing queries. The solution runs fully offline using a local LLM and a local analytical database, making it suitable for secure enterprise and academic environments.

Objectives
The objectives of this project are to enable natural language querying over energy utility datasets, enforce role-based access control before any data access, prevent LLM-based data leakage, operate fully offline without cloud dependencies, and demonstrate enterprise-grade secure AI architecture.

System Architecture
The user submits a natural language question.
The local LLM interprets the question and extracts intent.
The MCP server validates role permissions.
DuckDB executes only authorized queries.
Authorized results are returned.
The LLM generates a plain-English explanation.

Core Components
The local LLM (Ollama with Mistral) interprets natural language queries, identifies the required dataset, and generates human-readable explanations. It does not access the database directly.
The MCP server (FastAPI) acts as a secure access gateway, enforces RBAC policies, and prevents unauthorized database access.
DuckDB stores energy utility datasets and executes only policy-approved queries.

Technologies Used
Python
DuckDB
FastAPI
Ollama
Mistral LLM
Role-Based Access Control (RBAC)

Project Structure
The project includes CSV files for customers, meters, meter readings, and billing data, a DuckDB database file, a data ingestion script, an MCP server implementation, and an LLM client script.

Functional Modules
The Data Ingestion Module loads CSV datasets into DuckDB and creates structured analytical tables.
The MCP Server Module validates user roles and executes only authorized queries.
The LLM Intent Classification Module converts natural language queries into structured intents and selects appropriate datasets.
The Secure Query Execution Module enforces permissions before querying and blocks unauthorized access.
The Explanation Module converts query results into plain-English explanations.

Role-Based Access Control
The Operations role can access meters and meter readings.
The Billing Analyst role can access billing and meter readings.
The Finance role can access billing data in aggregated form only.
The Customer Support role can access customer data and customer-specific billing.
The Admin role has access to all datasets.

Implementation Steps
Install required dependencies.
Load CSV data into DuckDB.
Start the MCP server.
Start the Ollama LLM service.
Run the LLM client to execute queries.

Sample Use Case
User role is Operations.
User query is: Which meters have recent readings?
The LLM interprets the question, the MCP server validates permissions, DuckDB returns authorized data, and the LLM explains the results in plain English.

Key Features
Secure LLM integration.
Policy-controlled data access.
Fully offline execution.
Prevention of LLM data leakage.
Enterprise-ready architecture.

Conclusion
This project demonstrates a secure and scalable approach to integrating Large Language Models with sensitive enterprise data. By separating intelligence, access control, and data storage, the system ensures both usability and strong security guarantees aligned with real-world enterprise AI practices.

Sathya Bala B
Second Year Project
Secure LLM-Based Energy Utility Analytics System
