"""Reproduce both rankings in the fictional retail teaching case (kit 1.1). Python 3, no dependencies."""
import json
from pathlib import Path

folder = Path(__file__).resolve().parent

def run(letter):
    case = json.loads((folder / f"retail-input-{letter}.json").read_text())
    expected = json.loads((folder / f"expected-output-{letter}.json").read_text())
    shops = {row["id"] for row in case["shops"]}
    visible = {row["id"] for row in case["shops"] if row["shared_checkout"]}
    supported = {row["id"] for row in case["shops"] if row["independent_platform_record"]}

    def ranking(arc_count):
        counts = {**case["other_supplier_counts"], "Arc": arc_count}
        return sorted(counts, key=lambda s: (-counts[s], s)), counts

    before, _ = ranking(len(visible | supported))
    after, counts = ranking(len(supported))
    result = {"before": before[:3], "after": after[:3],
              "arc_supported": len(supported), "arc_unresolved": len(shops - supported)}
    if "third_place_after" in expected:
        result["third_place_after"] = {"supplier": after[2], "supported_shops": counts[after[2]]}
    if result != expected:
        raise SystemExit(f"Scenario {letter.upper()} mismatch: {result}")
    return result

if __name__ == "__main__":
    for letter in ("a", "b"):
        print(f"Scenario {letter.upper()}:", json.dumps(run(letter)))
    print("Both scenarios match the expected output.")
