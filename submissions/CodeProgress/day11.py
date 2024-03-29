with open('submissions/challenges/sample.txt', 'r') as file:
    names = file.readlines()

names.sort()

print("Sorted names:")
for name in names:
    print(name.strip())

with open('submissions/challenges/sample.txt', 'w') as file:
    for name in names:
        file.write(name.strip() + '\n')  