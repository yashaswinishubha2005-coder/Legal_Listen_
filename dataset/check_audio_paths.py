
from pathlib import Path
import pandas as pd

root = Path("data/indicvoices_kannada")
files = sorted(root.rglob("valid-*.parquet"))

for file in files:
    df = pd.read_parquet(file)

    print(f"\nFILE: {file.name}")
    print("Rows:", len(df))
    print("Duration statistics:")
    print(df["duration"].describe().round(2).to_string())

    audio = df["audio_filepath"].dropna().iloc[0]

    print("\nAudio reference type:", type(audio).__name__)

    if isinstance(audio, dict):
        print("Audio keys:", list(audio.keys()))
        print("Audio path:", audio.get("path"))
        data = audio.get("bytes")
        print("Embedded bytes present:", data is not None)
        if data is not None:
            print("Embedded byte count:", len(data))
    else:
        print("Audio reference:", str(audio)[:200])

    print("Missing transcripts:", df["text"].isna().sum())
