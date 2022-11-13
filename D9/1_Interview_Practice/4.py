def capitalize_strings(test_list):
    if len(test_list) == 0:
        return ""
    else:       
        return (f"{test_list[0].upper()} {capitalize_strings(test_list[1:])}")


# sample_list = []
sample_list = ['pandas', 'monkeys', 'koalas', 'kangaroos']
print(capitalize_strings(sample_list))