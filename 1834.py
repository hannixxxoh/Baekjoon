N = int(input())
number = 0
num_list = []
i = 1

while number < N*N:
    # if i % N != 0:
    number = N * i + i
    if number // N == number % N:
        num_list.append(number)
    i += 1


print(sum(num_list))