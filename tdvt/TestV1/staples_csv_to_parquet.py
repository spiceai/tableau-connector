import pyarrow.csv as csv
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime

from arrow_utils import print_parquet_schema, read_csv_with_schema, write_table_to_parquet

# CSV input path and Parquet output path
csv_path = "./Staples_utf8_headers.csv"
parquet_path = "staples.parquet"

# Target Staples schema: https://github.com/tableau/connector-plugin-sdk/blob/master/tests/datasets/TestV1/DDL/Staples.sql
arrow_schema = pa.schema([
    ("Item Count", pa.int32()),
    ("Ship Priority", pa.string()),
    ("Order Priority", pa.string()),
    ("Order Status", pa.string()),
    ("Order Quantity", pa.float64()),
    ("Sales Total", pa.float64()),
    ("Discount", pa.float64()),
    ("Tax Rate", pa.float64()),
    ("Ship Mode", pa.string()),
    ("Fill Time", pa.float64()),
    ("Gross Profit", pa.float64()),
    ("Price", pa.decimal128(18, 4)),
    ("Ship Handle Cost", pa.decimal128(18, 4)),
    ("Employee Name", pa.string()),
    ("Employee Dept", pa.string()),
    ("Manager Name", pa.string()),
    ("Employee Yrs Exp", pa.float64()),
    ("Employee Salary", pa.decimal128(18, 4)),
    ("Customer Name", pa.string()),
    ("Customer State", pa.string()),
    ("Call Center Region", pa.string()),
    ("Customer Balance", pa.float64()),
    ("Customer Segment", pa.string()),
    ("Prod Type1", pa.string()),
    ("Prod Type2", pa.string()),
    ("Prod Type3", pa.string()),
    ("Prod Type4", pa.string()),
    ("Product Name", pa.string()),
    ("Product Container", pa.string()),
    ("Ship Promo", pa.string()),
    ("Supplier Name", pa.string()),
    ("Supplier Balance", pa.float64()),
    ("Supplier Region", pa.string()),
    ("Supplier State", pa.string()),
    ("Order ID", pa.string()),
    ("Order Year", pa.int32()),
    ("Order Month", pa.int32()),
    ("Order Day", pa.int32()),
    ("Order Date", pa.timestamp("s")),
    ("Order Quarter", pa.string()),
    ("Product Base Margin", pa.float64()),
    ("Product ID", pa.string()),
    ("Receive Time", pa.float64()),
    ("Received Date", pa.timestamp("s")),
    ("Ship Date", pa.timestamp("s")),
    ("Ship Charge", pa.decimal128(18, 4)),
    ("Total Cycle Time", pa.float64()),
    ("Product In Stock", pa.string()),
    ("PID", pa.int32()),
    ("Market Segment", pa.string())
])

try:
    table = read_csv_with_schema(csv_path, arrow_schema)
    write_table_to_parquet(table, parquet_path)
    print_parquet_schema(parquet_path)
    
except Exception as e:
    print(f"Error during conversion: {e}")

# Keeping Table Arrow schema for future reference / troubleshooting
# Schema in Parquet file:
#   Item Count: int32
#   Ship Priority: string
#   Order Priority: string
#   Order Status: string
#   Order Quantity: double
#   Sales Total: double
#   Discount: double
#   Tax Rate: double
#   Ship Mode: string
#   Fill Time: double
#   Gross Profit: double
#   Price: decimal128(18, 4)
#   Ship Handle Cost: decimal128(18, 4)
#   Employee Name: string
#   Employee Dept: string
#   Manager Name: string
#   Employee Yrs Exp: double
#   Employee Salary: decimal128(18, 4)
#   Customer Name: string
#   Customer State: string
#   Call Center Region: string
#   Customer Balance: double
#   Customer Segment: string
#   Prod Type1: string
#   Prod Type2: string
#   Prod Type3: string
#   Prod Type4: string
#   Product Name: string
#   Product Container: string
#   Ship Promo: string
#   Supplier Name: string
#   Supplier Balance: double
#   Supplier Region: string
#   Supplier State: string
#   Order ID: string
#   Order Year: int32
#   Order Month: int32
#   Order Day: int32
#   Order Date: timestamp[ms]
#   Order Quarter: string
#   Product Base Margin: double
#   Product ID: string
#   Receive Time: double
#   Received Date: timestamp[ms]
#   Ship Date: timestamp[ms]
#   Ship Charge: decimal128(18, 4)
#   Total Cycle Time: double
#   Product In Stock: string
#   PID: int32
#   Market Segment: string

