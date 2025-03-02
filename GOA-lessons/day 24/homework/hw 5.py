def word(word, repeat):
    new_arr = []
    for i in range(repeat):
        new_arr.append(word)
    print(''.join(new_arr))
l = input('enter word: ')
l1= int(input('enter repeat times: '))
word(l, l1)