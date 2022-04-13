n = int(input())
positives = list()
negatives = list()

for i in range(n):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)

count_positives = len(positives)
sum_of_negatives = sum(negatives)

print(positives)
print(negatives)
print(f'Count of positives: {count_positives}')
print(f'Sum of negatives: {sum_of_negatives}')
