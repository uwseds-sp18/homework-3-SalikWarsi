import sqlite3
import pandas as pd
query1 = "select video_id, category_id, \"us\" as language from USvideos "
query2 = "UNION select video_id, category_id, \"ca\" as language from CAvideos "
query3 = "UNION select video_id, category_id, \"gb\" as language from GBvideos "
query4 = "UNION select video_id, category_id, \"fr\" as language from FRvideos "
query5 = "UNION select video_id, category_id, \"de\" as language from DEvideos;"
query = query1 + query2 + query3 + query4 + query5
def create_dataframe(dbpath):
    try:
        conn = sqlite3.connect(dbpath)
        df = pd.read_sql_query(query, conn)
    except:
        raise ValueError("SQLite db not correct")
    return df