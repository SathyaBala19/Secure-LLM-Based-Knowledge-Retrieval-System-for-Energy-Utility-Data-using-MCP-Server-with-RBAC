import os
import duckdb
print("CURRENT WORKING DIRECTORY:", os.getcwd())
import pandas as pd

# Connect to DuckDB (creates file if not exists)
con = duckdb.connect("energy_utility.duckdb")

# Load CSVs into DuckDB tables
con.execute("""
CREATE OR REPLACE TABLE customers AS
SELECT * FROM read_csv_auto('data/customers.csv')
""")

con.execute("""
CREATE OR REPLACE TABLE meters AS
SELECT * FROM read_csv_auto('data/meters.csv')
""")

con.execute("""
CREATE OR REPLACE TABLE meter_readings AS
SELECT * FROM read_csv_auto('data/meter_readings.csv')
""")

con.execute("""
CREATE OR REPLACE TABLE billing AS
SELECT * FROM read_csv_auto('data/billing.csv')
""")

print("✅ Energy utility data loaded into DuckDB successfully")

# Quick validation
print("\nCustomers:")
print(con.execute("SELECT * FROM customers").df())

print("\nMeters:")
print(con.execute("SELECT * FROM meters").df())

print("\nMeter Readings:")
print(con.execute("SELECT * FROM meter_readings").df())

print("\nBilling:")
print(con.execute("SELECT * FROM billing").df())

con.close()