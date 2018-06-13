def tree(text, count):
    text =list(text)
    left = text[0:2]
    right = text[2:]
    all_tree = [left, right]

    count.append(all_tree)

    if len(right) == 2:
        return count

    else:
        return tree(right, count)


def indexRecursive(alist, currentIndex, tuples):
    i = 0
    for item in alist:
        if type(item) != list:
            if not i > 1:
                tuples.append((item, currentIndex + [i]))
        else:
            indexRecursive(alist[i], currentIndex + [i], tuples)
        i += 1


def pr_tree(c):
    for i in c:
        tuplesList = []
        indexRecursive(i, [], tuplesList)
        return tuplesList


def shannon(text):
    cc = tree(text, [])

    one_arry = []
    for i in range(len(cc), 0, -1):
        try:
            cc[i - 1][1] = cc[i]
            del cc[i]
            one_arry = cc
        except IndexError:
            pass

    return one_arry


def gui(text):
    one = pr_tree(shannon(text))
    for inx, code in one:
        print(str(inx).ljust(10), str(code))

gui("ABCDE")

