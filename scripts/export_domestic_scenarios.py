"""Export tidy USD scenarios from the frozen September edition without fetching prices."""
import csv
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AMOUNTS = (1000, 2500, 10000, 50000)


def main():
    data = json.loads((ROOT / 'data.json').read_text())
    providers = {p['id']: p for p in data['providers']}
    rows = []
    for calc in data['calculations']:
        provider = providers[calc['provider']]
        for amount in AMOUNTS:
            fee = calc[f'domestic_fee_cents_{amount}']
            raw_fee = Decimal(str(provider['rate_percent'])) * amount / 100 + provider['fixed_fee_cents']
            if fee != int(raw_fee.quantize(Decimal('1'), rounding=ROUND_HALF_UP)):
                raise ValueError(f"Frozen fee and inputs disagree for {provider['id']} at {amount} cents")
            rows.append({'payment_path': provider['id'], 'observed_on': provider['observed_on'],
                         'sale_cents': amount, 'processing_fee_cents': fee,
                         'after_processing_cents': amount - fee})
    out = ROOT / 'editions/2026-09-14/domestic-card-scenarios.csv'
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=rows[0].keys(), lineterminator='\n')
        writer.writeheader()
        writer.writerows(rows)


if __name__ == '__main__':
    main()
