import sys
import os
import json
from dataclasses import asdict

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from research_ingestion.pipeline import process_pdf


BASE_DIR = os.path.dirname(__file__)

REAL_REPORTS_DIR = os.path.join(BASE_DIR, "real_reports")
TEST_CASES_DIR = os.path.join(BASE_DIR, "test_cases")
OUTPUT_DIR = os.path.join(BASE_DIR, "outputs")
TICKER_MAP_PATH = os.path.join(BASE_DIR, "ticker_map.csv")


def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def process_file(file_path):
    print(f"\nProcessing: {file_path}")

    try:
        doc = process_pdf(file_path, TICKER_MAP_PATH)

        # Save output
        output_name = os.path.basename(file_path) + ".json"
        output_path = os.path.join(OUTPUT_DIR, output_name)

        with open(output_path, "w") as f:
            json.dump(asdict(doc), f, indent=2)

        print(f"✅ Saved: {output_path}")
        print(f"   Entities: {len(doc.entities)}")
        print(f"   Themes: {doc.themes}")

    except Exception as e:
        print(f"❌ Failed: {file_path}")
        print(str(e))


def run_all_tests():
    ensure_output_dir()

    # Process real PDFs
    print("\n=== REAL REPORTS ===")
    for file in os.listdir(REAL_REPORTS_DIR):
        if file.lower().endswith(".pdf"):
            process_file(os.path.join(REAL_REPORTS_DIR, file))

    # Process synthetic test cases (optional future use)
    print("\n=== TEST CASES (TXT) ===")
    for file in os.listdir(TEST_CASES_DIR):
        if file.lower().endswith(".txt"):
            print(f"Skipping (not yet PDF-supported): {file}")


if __name__ == "__main__":
    run_all_tests()