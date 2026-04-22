from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
1. Data Preprocessing
The dataset was loaded and converted from a comma-separated format into a transactional list.
One-hot encoding was performed to transform the product list into a sparse matrix, where each column represents a product and each row represents a transaction (True if purchased, False otherwise).
2. Association Rule Mining Results 
Model 1: Using a minimum support of 1% and 20% confi dence, we identifi ed common item pairings.● Model 2: Lowering the support to 0.5% allowed us to fi nd rarer but potentially high-value associations, resulting in a larger set of rules.
Model 3: Filtering by a Lift threshold of 2.0 ensured that we only extracted rules where the items have a strong mathematical dependency on each other, rather than just being popular items.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0
)

chunk = splitter.split_text(text)

print(len(chunk))
print(chunk)