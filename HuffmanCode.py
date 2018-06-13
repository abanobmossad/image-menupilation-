def cal_tree(freq, alphabet):
    for i in range(len(freq) - 1, 0, -1):
        val = freq[i] + freq[i - 1]
        alpha = [alphabet[i - 1], alphabet[i]]
        x = 0
        freq[i - 1] = val
        freq.sort(reverse=True)
        alphabet.insert(freq.index(val), alpha)
        del freq[i]
        del alphabet[i]
        del alphabet[i]
    return alphabet


def indexRecursive(alist, currentIndex, tuples):
    i = 0
    for item in alist:
        if type(item) != list:
            tuples.append((item, currentIndex + [i]))
        else:
            indexRecursive(alist[i], currentIndex + [i], tuples)
        i += 1


def print_tree():
    alphabet = list("ABCDE")
    freqq = [15, 7, 6, 6, 5]
    li = cal_tree(freqq, alphabet)
    tuplesList = []
    indexRecursive(li[0], [], tuplesList)
    print("Symbol".ljust(10) + "Frequency".ljust(13) + "Huffman Code")
    freqq = [15, 7, 6, 6, 5]
    count = 0
    print(tuplesList)
    for inx, code in tuplesList:
        print(str(inx).ljust(10), str(freqq[count]).ljust(11), str(code))
        count += 1


print_tree()
