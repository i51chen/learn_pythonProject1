if __name__ == '__main__':
    a = False
    b = True
    list1 = [a, b, a]
    list2 = list('123456')
    print(any(list1))
    print(all(list1))
    print(list2)
    output = "".join(list2)
    print(output)

