from universe.providers.stub import load_stub_securities
from universe.universe import build_universe
from datetime import date

securities = load_stub_securities()
universe = build_universe(securities, as_of_date=date.today())

print(len(universe.securities))