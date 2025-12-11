import pandas as pd

data = {
    "right_ascension": [123.2, 123.2, 123.4],
    "Dec": [-23.2, -23.4, -23.1],
    "uber_id": ["gal1", "gal2", "gal3"]
}

df = pd.DataFrame(data)
df.to_parquet("catalogue_4.parquet")