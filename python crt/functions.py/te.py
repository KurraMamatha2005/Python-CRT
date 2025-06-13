# Function to find matches in the sequence
def find_matches(query: str, db: dict) -> list:
    matches = []
    for seq_id, sequence in db.items():
        if query in sequence:
            matches.append(seq_id)
    return matches
db = {
    "seq001": "ATGCGGAATT",
    "seq002": "CGTACGTAGC",
    "seq003": "TTATGCATTA",
    "seq004": "GGAATCCGTA",
    "seq005": "CATGCCGTAGC",
    "seq006": "GGGCGTGCAT",
    "seq007": "AATGCTAGCTA",
    "seq008": "CGCGATGCGC",
    "seq009": "TATATATATA",
    "seq010": "ATGCGGATGCA"
}

query = "ATGCGG"
result = find_matches(query, db)
print("Matched sequences:", result)

