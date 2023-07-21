
worhr = []
salary = 0

for i in range(7):
    worhr.append(int(input()))
    salary += (worhr[i] * 100)

    if worhr[i] > 8:
        salary += (worhr[i] - 8) * 15

if worhr[0]:
    salary += (worhr[0] * 100) // 2

if worhr[6]:
    salary += (workingHours[6] * 100) // 4

if sum(worhr) > 40:
    salary += (sum(workingHours) - 40) * 25

print(int(salary))