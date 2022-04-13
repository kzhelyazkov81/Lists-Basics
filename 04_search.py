n = int(input())
word = input()
string = []
filtered = []

for i in range(n):
    current_string = input()
    string.append(current_string)
    if word in current_string:
        filtered.append(current_string)

print(string)
print(filtered)
