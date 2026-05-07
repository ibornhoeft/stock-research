import csv
from datetime import datetime

INPUT = "data/raw/factset_sample_raw.csv"
OUTPUT = "data/processed/factset_sample_clean.csv"


def clean_value(value: str) -> str:
    if value is None:
        return ""

    v = value.strip()

    # Normalize missing values
    if v in {"", "NA", "@NA", "#N/A"}:
        return ""

    return v


def normalize_exchange(value: str) -> str:
    mapping = {
        "NAS": "NASDAQ",
        "NYSE": "NYSE",
        "XNYS": "NYSE",
    }
    return mapping.get(value, value)

def normalize_date(value: str) -> str:
    if not value:
        return ""

    v = value.strip()

    # Handle known missing values
    if v in {"", "NA", "@NA", "#N/A"}:
        return ""

    # Try parsing MM/DD/YYYY (FactSet style)
    try:
        dt = datetime.strptime(v, "%m/%d/%Y")
        return dt.strftime("%Y-%m-%d")
    except Exception:
        pass

    # Try ISO format (already clean)
    try:
        dt = datetime.strptime(v, "%Y-%m-%d")
        return v
    except Exception:
        pass

    # If we cannot parse it, return blank
    return ""

def normalize_security_type(value: str) -> str:
    v = value.strip().upper()

    if v == "SHARE":
        return "COMMON_STOCK"

    # Explicit exclusions
    if v in {"ADR", "UNIT"}:
        return ""

    return ""

def main():
    with open(INPUT, newline="") as infile, open(OUTPUT, "w", newline="") as outfile:
        reader = csv.DictReader(infile)

        fieldnames = [
            "internal_id", "ticker", "exchange", "cusip",
            "valid_from", "valid_to", "security_type", "share_class",
            "sector", "industry", "has_price_history", "has_fundamentals",
        ]

        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            cleaned = {k: clean_value(v) for k, v in row.items()}

            writer.writerow({
                "internal_id": cleaned.get("Entity ID", cleaned.get("Symbol")),
                "ticker": cleaned.get("Symbol"),
                "exchange": normalize_exchange(cleaned.get("Stock Exchange")),
                "cusip": cleaned.get("CUSIP"),
                "valid_from": normalize_date(cleaned.get("Date (FIRST)")),
                "valid_to": "",
                "security_type": normalize_security_type(cleaned.get("Sec Type")), #if  else "COMMON_STOCK",
                "share_class": cleaned.get("Share Class Desc"), #"ORD",
                "sector": cleaned.get("GICS Sector Name"),
                "industry": cleaned.get("GICS Ind Name"),
                "has_price_history": "true",
                "has_fundamentals": "true",
            })


if __name__ == "__main__":
    main()