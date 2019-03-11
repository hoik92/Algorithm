p = 19893827938274839
result = True
for i in range(2, p):
    if p % i == 0:
        result = False
        print(i)
        # break
print(result)