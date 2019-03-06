# prime_number = [2, 3, 5, 7]
# print(2, end=' ')
# for i in range(3, 1000001):
#     is_prime_number = True
#     if i % 2 and i % 3 and i % 5 and i % 7:
#         for j in prime_number:
#             if i % j == 0:
#                 is_prime_number = False
#                 break
#         if is_prime_number:
#             prime_number.append(i)
#             print(i, end=' ')

prime = [2]
print(2, end=' ')
for i in range(3, 1000001):
    is_prime = True
    squ_i = int(i**0.5) + 1
    for j in prime:
        if squ_i < j:
            break
        elif i % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(i)
        print(i, end=' ')