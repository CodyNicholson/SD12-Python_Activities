'''
Problem 1: Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.

>>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
{'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4}
'''

def flatten_dict(d):
    result = dict()
    for i in d.keys():
        if type(d[i]) == dict:
            for k,v in d[i].items():
                new_key = i + "." + k
                result[new_key] = v
        else:
            result[i] = d[i]
    return result

print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))
print(flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}))

'''
Problem 2: Write a function unflatten_dict to do reverse of flatten_dict.

>>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
{'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4}
'''



'''
Problem 3: Write a function treemap to map a function over nested list.

>>> treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])
[1, 4, [9, 16, [25]]]
'''

def treemap(func, lst):
  for i in range(len(lst)):
    if type(lst[i]) == list:
      lst[i] = treemap(func,lst[i])
    else:
      lst[i] = func(lst[i])

  return lst
  
print(treemap(lambda i: i*i, [1, 2, [3, 4, [5]]]))