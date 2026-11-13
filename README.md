# Who actually supplies this brand? Teaching kit 1.1

**Research lead:** Joash Boyton, Acquiry Labs.
**Source edition:** [Who actually supplies this brand? Research edition 1.1](https://www.acquiry.com/labs/who-supplies-this-brand/editions/1.1/) (13 November 2026).

Ten shops appear to use the same supplier. After the evidence is corrected, only three relationships remain supported. Two reproducible scenarios show when that changes which acquisition target a buyer should approach first.

The two ranking scenarios use **fictional** shops and suppliers. The research edition's real-world opening example is Squarespace and Stripe.

## Rule

1. A shop counts for a supplier only with independent evidence.
2. A shared checkout is not independent evidence.
3. Rank by supported shops, then by name A to Z.

## Results

| Scenario | Call list before correction | Call list after correction |
| --- | --- | --- |
| A | Arc (10) > Birch (8) > Cove (6) | Birch (8) > Cove (6) > Dune (4) |
| B | Arc (10) > Birch (8) > Cove (6) | Birch (8) > Cove (6) > Arc (3) |

## Run it

```
python3 kit/verify.py        # recomputes both scenarios; no dependencies
```

Or open `who-supplies-this-brand.ipynb`, which shows both before-and-after rankings and a chart.

## Files

- `kit/retail-input-a.json`, `kit/expected-output-a.json`: Scenario A
- `kit/retail-input-b.json`, `kit/expected-output-b.json`: Scenario B
- `kit/verify.py`: recomputes both scenarios and stops with an error on any mismatch
- `kit/README.md`: kit notes as published in the edition
- `who-supplies-this-brand.ipynb`: executed walkthrough notebook

The kit files are byte-identical to those published with research edition 1.1. Their SHA-256 values are listed in the edition's `SHA256SUMS.txt`.

## Related

- Research edition 1.1: https://www.acquiry.com/labs/who-supplies-this-brand/editions/1.1/
- Companion dataset, *Embedded Payments Provider Map for Software Platforms*, dataset edition 1.1 (versioned separately): https://www.acquiry.com/data/embedded-payments-provider-map/editions/1.1/

## Cite

Acquiry Labs. *Who actually supplies this brand?* Research lead Joash Boyton. Research edition 1.1, 13 November 2026. https://www.acquiry.com/labs/who-supplies-this-brand/editions/1.1/

## Licence

CC BY 4.0, © 2026 Joash Boyton. See `LICENSE`.
