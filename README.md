# US online card processing fees — dated inputs and calculations

This is a dated, machine-readable copy of [Payney's US online card fee comparison](https://payney.com/reports/online-card-fees-us-2026-09/). It brings published pricing onto a common basis for a US merchant. It is a transcription and calculation, not a test of real transactions, a merchant survey, or a ranking of payment services.

[Download the $100 processing-fee chart (SVG)](https://payney.com/reports/online-card-fees-us-2026-09/fees.svg) or [get HTML to embed it with the source and licence](https://payney.com/reports/online-card-fees-us-2026-09/#reuse-chart). The chart covers 13 flat-rate price paths observed on September 14, 2026.

The September 14, 2026 edition covers 15 published price paths at 10 providers. Thirteen flat-rate paths have calculated processing costs for $10, $25, $100 and $500 online card sales. Two interchange-plus paths are documented without inventing a single all-in rate. The data also records published international-card and currency-conversion surcharges, refund treatment, dispute fees, observation dates and source URLs. Unpublished terms remain blank rather than estimated.

| File | Contents |
| --- | --- |
| [data.json](data.json) | Inputs, 23 source references, scope, methodology, provider terms and calculations |
| [data.csv](data.csv) | One row per published price path, including the calculated flat-rate scenarios |

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

The canonical report and downloads live at payney.com. The original September files above remain frozen; the November recheck is a separate edition for reproducible analysis.
