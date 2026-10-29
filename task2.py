"""Lab 1 Task 2: Transparent scholarship rules and a threshold comparison.
All thresholds and probabilities are synthetic examples, not actual policy.
"""
def rule_check(score, documents_complete, attendance, income):
    if not documents_complete:
        return "Hold", "Documents are incomplete"
    if score < 70:
        return "Hold", "Score below 70"
    if attendance < 80:
        return "Hold", "Attendance below 80%"
    if income > 50000:
        return "Hold", "Income above 50000"
    return "Review", "All four conditions passed"

def probability_check(probability):
    return "Review" if probability >= 0.70 else "Hold"

cases = [
    ("Pass", 85, True, 90, 40000, 0.82, "Review"),
    ("Attendance failure", 82, True, 79, 40000, 0.81, "Hold"),
    ("Income failure", 88, True, 90, 51000, 0.88, "Hold"),
    ("Score boundary", 70, True, 80, 50000, 0.70, "Review"),
]
print("Synthetic thresholds: score >=70, documents complete, attendance >=80, income <=50000")
for name, score, docs, attendance, income, probability, expected in cases:
    actual, reason = rule_check(score, docs, attendance, income)
    threshold = probability_check(probability)
    print(f"{name}: inputs=(score={score}, docs={docs}, attendance={attendance}, income={income}, probability={probability})")
    print(f"  expected={expected}; actual={actual}; reason={reason}")
    print(f"  probability threshold={threshold}; disagreement={actual != threshold}")
    assert actual == expected
print("All four core tests passed.")

# Guided comparison on the same inputs (manual section 1.5).
print("\\nGuided original-rule comparison:")
for name, score, docs, prob in [
    ("complete_high",82,True,0.81),
    ("complete_low",68,True,0.74),
    ("incomplete_high",91,False,0.88),
    ("boundary",70,True,0.70),
]:
    rule = "Review" if docs and score >= 70 else "Hold"
    other = probability_check(prob)
    print(f"{name}: symbolic={rule}, threshold={other}, disagreement={rule != other}")
print("Boundary checks: score 69 ->", rule_check(69, True, 80, 50000)[0],
      "; probability 0.69 ->", probability_check(0.69))
