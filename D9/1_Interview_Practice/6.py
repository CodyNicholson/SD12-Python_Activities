def nonrepeating_integers(test_list):

    # insert elements of list into dictionary (hash table)
    elements = {}
    for i in range(len(test_list)):
        if test_list[i] not in elements:
            elements[test_list[i]]=0
        elements[test_list[i]]+=1
    
    # traverse through elements in dictionary
    for j in elements:
        if (elements[j] == 1):
            print(j)

test_list = [1, 5, 1, 6, 8, 5]
nonrepeating_integers(test_list)