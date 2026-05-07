# from universe.providers.local_csv import load_securities_from_csv
# from universe.universe import build_universe
# from datetime import date

# # Load from CSV
# securities = load_securities_from_csv("data/raw/universe_stub.csv")

# # Build universe
# universe = build_universe(securities, as_of_date=date.today())

# # Output results
# print("Total input securities:", len(securities))
# print("Total in universe:", len(universe.securities))

# print("\nTickers in universe:")
# for sec in universe.securities:
#     print(sec.identifier.ticker)


from universe.providers.local_csv import load_securities_from_csv
from universe.universe import build_universe
from datetime import date
import os

filepath = "data/processed/factset_sample_clean.csv"

print("File exists:", os.path.exists(filepath))
print("File path:", filepath)

securities = load_securities_from_csv(filepath)

print("Total input securities:", len(securities))

universe = build_universe(securities, as_of_date=date.today())

print("Total in universe:", len(universe.securities))