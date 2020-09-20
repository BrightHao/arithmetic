def permute(string):
    res = list()
    length = len(string)
    def combin(coms, rest):
        if len(coms) == length:
            res.append(coms)
            return
        for i in range(len(rest)):
            combin(coms+rest[i], rest[:i]+rest[i+1:])
    combin("", string)
    return res

word = input()
text = input()
target = input()

ll = permute(word)
for i in ll:
    text = text.replace(i, target)
print(text)
