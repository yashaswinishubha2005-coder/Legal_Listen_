
from datasets import load_dataset

dataset = load_dataset(
    "coastalcph/lex_glue",
    "unfair_tos"
)

dataset.save_to_disk("data/lexglue_unfair_tos")

print("Dataset saved successfully!")
print(dataset)
