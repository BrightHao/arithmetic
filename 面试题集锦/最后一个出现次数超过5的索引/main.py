string = input()

def main(string):
    res = -1
    count = {}
    for i in range(len(string)):
        s = string[i]
        if s in count:
            count[s] += 1
        else:
            count[s] = 1
        if count[s] > 5:
            res = i
    return res

print(main(string))
