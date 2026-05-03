import json
import argparse
from src.rag_pipeline import rag_pipeline

def main(input_path, output_path):
    with open(input_path, "r") as f:
        data = json.load(f)

    results = []

    for item in data:
        query = item["query"]

        standards, latency = rag_pipeline(query)

        results.append({
            "id": item["id"],
            "retrieved_standards": standards,
            "latency_seconds": latency
        })

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()
    main(args.input, args.output)