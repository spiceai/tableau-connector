import pyarrow.csv as csv
import pyarrow as pa
import pyarrow.parquet as pq
from datetime import datetime

from arrow_utils import print_parquet_schema, read_csv_with_schema, write_table_to_parquet

# CSV input path and Parquet output path
csv_path = "./Calcs_headers.csv"
parquet_path = "calcs.parquet"

# Target Calcs schema: https://github.com/tableau/connector-plugin-sdk/blob/master/tests/datasets/TestV1/DDL/Calcs.sql
arrow_schema = pa.schema([
    ("key", pa.string()),
    ("num0", pa.float64()),
    ("num1", pa.float64()),
    ("num2", pa.float64()),
    ("num3", pa.float64()),
    ("num4", pa.float64()),
    ("str0", pa.string()),
    ("str1", pa.string()),
    ("str2", pa.string()),
    ("str3", pa.string()),
    ("int0", pa.int32()),
    ("int1", pa.int32()),
    ("int2", pa.int32()),
    ("int3", pa.int32()),
    ("bool0", pa.bool_()),
    ("bool1", pa.bool_()),
    ("bool2", pa.bool_()),
    ("bool3", pa.bool_()),
    ("date0", pa.date32()),
    ("date1", pa.date32()),
    ("date2", pa.date32()),
    ("date3", pa.date32()),
    ("time0", pa.timestamp("s")),
    ("time1", pa.time64("us")),
    ("datetime0", pa.timestamp("s")),
    ("datetime1", pa.string()),
    ("zzz", pa.string())
])

try:
    table = read_csv_with_schema(csv_path, arrow_schema)
    write_table_to_parquet(table, parquet_path)
    print_parquet_schema(parquet_path)
    
except Exception as e:
    print(f"Error during conversion: {e}")

# Keeping Table Arrow schema for future reference / troubleshooting
# Schema in Parquet file:
#   key: string
#   num0: double
#   num1: double
#   num2: double
#   num3: double
#   num4: double
#   str0: string
#   str1: string
#   str2: string
#   str3: string
#   int0: int32
#   int1: int32
#   int2: int32
#   int3: int32
#   bool0: bool
#   bool1: bool
#   bool2: bool
#   bool3: bool
#   date0: date32[day]
#   date1: date32[day]
#   date2: date32[day]
#   date3: date32[day]
#   time0: timestamp[ms]
#   time1: time64[us]
#   datetime0: timestamp[ms]
#   datetime1: string
#   zzz: string
