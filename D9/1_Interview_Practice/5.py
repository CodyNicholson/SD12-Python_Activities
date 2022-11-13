def product_of_list(test_list):
    if len(test_list) == 0:
        return 0
    if len(test_list) ==1:
        return test_list[0]
    else: 
        return test_list[len(test_list)-1]*product_of_list(test_list[:len(test_list)-1])


sample_list = [4, 3, 5]

print(product_of_list(sample_list))