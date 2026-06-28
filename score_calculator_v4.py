scores = []

print("=" * 40)
print("       SCORE CALCULATOR")
print("=" * 40)
print("Enter scores one at a time (0 - 100).")
print("Type 'done' when finished.")
print("-" * 40)

while True:
    entry = input("\n> Enter score: ").strip()

    if entry.lower() == "done":
        break

    if entry == "":
        print("  ! No input detected. Please enter a number or 'done'.")
        continue

    try:
        score = float(entry)
    except ValueError:
        print("  ! Invalid input. Numbers only please.")
        continue

    if score < 0 or score > 100:
        print("  ! Score must be between 0 and 100.")
        continue

    scores.append(score)
    print(f"  + Score {score:.2f} added. ({len(scores)} score(s) so far)")

print("\n" + "=" * 40)

if scores:
    average = sum(scores) / len(scores)
    print(f"  Scores entered : {', '.join(str(s) for s in scores)}")
    print(f"  Total scores   : {len(scores)}")
    print(f"  Average score  : {average:.2f}")
else:
    print("  No scores were entered.")

print("=" * 40)
