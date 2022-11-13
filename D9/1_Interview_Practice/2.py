def sum_of_all_numbers(num):
    if num == 0 or num == 1:
        return num
    else:
        return num + sum_of_all_numbers(num-1)


n = 5

print(sum_of_all_numbers(n))