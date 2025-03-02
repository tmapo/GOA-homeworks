def replace_better(string, element, element2):
    arr =  string.split(element)
    arr.append(element2)
    l = arr.pop(1)
    arr.append(l)
    print(''.join(arr))
replace_better('hello', 'e', 'e')