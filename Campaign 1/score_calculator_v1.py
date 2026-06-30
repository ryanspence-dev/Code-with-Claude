scores = []

while True:
    entry = input("Enter a score (or 'done' to finish): ")
    if entry.lower() == "done":
        break
    scores.append(float(entry))

if scores:
    average = sum(scores) / len(scores)
    print(f"Average score: {average:.2f}")
else:
    print("No scores entered.")
