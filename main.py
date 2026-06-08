import json

from parser import parser
from validator import is_valid
from duplicate_detector import detect_duplicates
from ai_analysis import analyse_duplicate

records = []
invalid_records = []

with open("data/data.txt", "r") as f:

    for line in f:

        parsed = parser(line)

        if not is_valid(parsed):

            invalid_records.append(parsed)
            continue

        records.append(parsed)

duplicates = detect_duplicates(records)

results = []

for item in duplicates:

    pair = (
        item["record1"],
        item["record2"]
    )

    analysis = analyse_duplicate(pair)

    results.append({
        "record1": item["record1"],
        "record2": item["record2"],
        "similarity_score": round(
            item["similarity_score"],
            2
        ),
        "analysis": analysis
    })

with open("output/output.json", "w") as f:

    json.dump(results, f, indent=2)

with open("output/invalid_records.json", "w") as f:

    json.dump(invalid_records, f, indent=2)

print("Processing Complete")