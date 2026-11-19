---
pretty_name: US online card processing fees and full-refund scenarios
language:
- en
license: cc-by-4.0
tags:
- finance
- ecommerce
- payment-processing
size_categories:
- n<1K
configs:
- config_name: domestic_sale_scenarios
  default: true
  data_files: editions/2026-09-14/domestic-card-scenarios.csv
- config_name: published_price_paths
  data_files: data.csv
- config_name: full_refund_scenarios
  data_files: editions/2026-11-02/recheck-2026-11-02.csv
---

# US online card processing fees — dated inputs and calculations

This is a dated, machine-readable copy of [Payney's US online card fee comparison](https://payney.com/reports/online-card-fees-us-2026-09/). It brings published pricing onto a common basis for a US merchant. It is a transcription and calculation, not a test of real transactions, a merchant survey, or a ranking of payment services.

[Download the $100 processing-fee chart (SVG)](https://payney.com/reports/online-card-fees-us-2026-09/fees.svg) or [get HTML to embed it with the source and licence](https://payney.com/reports/online-card-fees-us-2026-09/#reuse-chart). The chart covers 13 flat-rate price paths observed on September 14, 2026.

The September 14, 2026 edition covers 15 published price paths at 10 providers. Thirteen flat-rate paths have calculated processing costs for $10, $25, $100 and $500 online card sales. Two interchange-plus paths are documented without inventing a single all-in rate. The data also records published international-card and currency-conversion surcharges, refund treatment, dispute fees, observation dates and source URLs. Unpublished terms remain blank rather than estimated.

| File | Contents |
| --- | --- |
| [data.json](data.json) | Inputs, 23 source references, scope, methodology, provider terms and calculations |
| [data.csv](data.csv) | One row per published price path, including the calculated flat-rate scenarios |
| [Domestic sale scenarios (CSV)](editions/2026-09-14/domestic-card-scenarios.csv) | 52 rows, one per payment path and ticket size, with gross amount, processing fee and amount after processing in USD cents |

To use a flat-rate price path in a promotion, enter the percentage and fixed fee in the Excel worksheet alongside your product cost, shipping and ad cost per extra order. It calculates the extra orders needed to preserve the contribution from your usual full-price sales. [Compare a discount with free shipping in Excel](https://payney.com/tools/?utm_source=github&utm_medium=referral&utm_campaign=offer_worksheet#offer-margin-worksheet).

The [report and methodology](https://payney.com/reports/online-card-fees-us-2026-09/#method) explain the assumptions and limitations. Always verify current terms with the provider before making a payment-processing decision: this edition is a snapshot, not a live rate feed. Custom contracts, in-person payments, tax handling and other costs can change the result.

Payney's original calculations and commentary are reusable under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) with attribution; provider prices and third-party material remain subject to their owners' terms. See [LICENSE.md](LICENSE.md). Suggested citation:

> Payney. “Online Card Processing Fees Compared: What a $100 Sale Costs at US Providers.” US edition, September 14, 2026. https://payney.com/reports/online-card-fees-us-2026-09/

## November 2 recheck: processing fees and full refunds

[Run the refund comparison in Google Colab](https://colab.research.google.com/github/stuseek/payney-payment-fees/blob/main/refund-scenarios.ipynb) or [view the notebook on GitHub](refund-scenarios.ipynb). Enter your average ticket, orders and full refunds to compare all six payment paths.

The [November recheck in the original report](https://payney.com/reports/online-card-fees-us-2026-09/#november-recheck) compares six named US domestic online payment paths using rates observed on **November 2, 2026**. It adds reproducible $10 and $100 sale scenarios, including a batch of 100 orders with 10 full refunds. This is a dated pricing calculation; no live payments were tested. It is not a full update of every September price path.

| File | Contents |
| --- | --- |
| [Observed inputs](editions/2026-11-02/recheck-2026-11-02-inputs.json) | Six named paths, observed rates, refund assumptions and provider source URLs |
| [Scenarios and method](editions/2026-11-02/recheck-2026-11-02.json) | Inputs and twelve calculated scenarios in USD cents |
| [Scenario CSV](editions/2026-11-02/recheck-2026-11-02.csv) | One row per payment path and order amount |

For each payment, round percentage × sale amount + fixed fee half up to cents. For the batch, subtract total processing fees and refunded principal from gross receipts. Original fees on refunded payments are already included in total processing fees; do not subtract them twice. The remaining balance is **not profit**. Monthly plans, merchandise, shipping, tax, disputes, international cards, conversion and negotiated pricing are excluded. Shopify requires a paid plan; Square online checkout and its Online API, and PayPal Checkout and standard card payments, are distinct paths.

For the difference between a merchant refund and a cardholder dispute, see [Payney’s chargeback vs refund guide](https://payney.com/blog/chargeback-vs-refund/), updated November 11. The guide is explanatory context, not another dataset edition.

## What does a merchant lose on a disputed $100 card payment?

On the standard US terms Payney checked on September 14, 2026, a merchant who challenged a $100 dispute and lost had $130 unrecovered at Stripe, $115 at Shopify Payments and $100 at Square. Each figure includes the disputed $100. The extra dispute fees were $30, $15 and $0 respectively.

| Payment provider | Accept dispute | Challenge and lose | Challenge and win |
| --- | ---: | ---: | ---: |
| Stripe, manual response | $115 | $130 | $15 |
| Shopify Payments | $115 | $115 | $0 |
| Square | $100 | $100 | $0 |

The table counts unrecovered principal and dispute fees. Original processing charges, merchandise, shipping and staff time are outside these totals. The accompanying CSV covers $25, $100 and $500 disputes in integer US cents. Its separate break-even calculation uses an illustrative $10 in response labor. [Scenario CSV](comparisons/chargebacks-2026-09-14/scenarios.csv) · [Payney report, provider terms and methodology](https://payney.com/reports/chargeback-fees-us-2026-09/?utm_source=github&utm_medium=referral&utm_campaign=chargeback_comparison#order)

Credit Payney for the dispute calculations under CC BY 4.0 and cite the [chargeback report](https://payney.com/reports/chargeback-fees-us-2026-09/). The sale and refund data retain their original observation dates and release files.
