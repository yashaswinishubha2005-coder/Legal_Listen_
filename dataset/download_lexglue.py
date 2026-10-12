
from datasets import load_dataset

print("Downloading LexGLUE: UNFAIR-ToS...")

dataset = load_dataset(
    "coastalcph/lex_glue",
    "unfair_tos"
)

print("\nDataset downloaded successfully!")
print(dataset)

print("\nFirst training example:")
print(dataset["train"][0])
