# Who actually supplies this brand? Teaching kit 1.1

Squarespace and Stripe are the real-world opening example in the research edition. This kit's two ranking scenarios use fictional shops and suppliers.

- `retail-input-a.json`, `expected-output-a.json`: Scenario A. The correction changes the third call: Dune enters the shortlist and Arc drops out.
- `retail-input-b.json`, `expected-output-b.json`: Scenario B. Same correction, Dune has 2 shops. Arc falls from first to third on three supported shops. The same three suppliers remain on the shortlist, in a different order.
- `verify.py`: recomputes both and stops with an error on any mismatch.

Run: `python3 verify.py`

Rule: a shop counts for a supplier only with independent evidence; the shared checkout is not independent evidence; rank by supported shops, then name A to Z.
Research lead: Joash Boyton. Acquiry Labs. Kit 1.1 accompanies research edition 1.1; dataset edition 1.1 is versioned separately.
