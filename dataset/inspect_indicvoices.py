
from pathlib import Path
import pandas as pd

root = Path("data/indicvoices_kannada")
files = sorted(root.rglob("valid-*.parquet"))

if not files:
    print("No Parquet files found!")
    raise SystemExit(1)

for file in files:
    print(f"\n{'=' * 50}")
    print("FILE:", file.name)

    df = pd.read_parquet(file)

    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())
    print("\nData types:")
    print(df.dtypes.to_string())

    # Print text fields only; avoid dumping audio bytes
    for col in df.columns:
        if col.lower() in ("text", "verbatim", "normalized", "transcript"):
            print(f"\nFirst 3 values in '{col}':")
            print(df[col].head(3).to_string(index=False))

    if "audio" in df.columns:
        print("\nAudio field type:", type(df["audio"].iloc[0]).__name__)
        print("Audio sample:", str(df["audio"].iloc[0])[:200])

