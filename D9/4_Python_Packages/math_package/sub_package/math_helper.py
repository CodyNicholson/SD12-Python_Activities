print(__name__)

def list_to(number):
    list = []
    count = 1
    while count < number:
        list.append(count)
        count += 1
    return list