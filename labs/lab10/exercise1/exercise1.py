num_rounds = int(input())
final_score = 0
rounds_processed = 0
for i in range(num_rounds):
    score = int(input("enter score: "))
    if score >= 100:
        total_score = score + ((20 / 100)*score)
        final_score += total_score
    else:
        final_score += score
    rounds_processed += 1

print(f"{final_score:.1f}")
print(rounds_processed)
