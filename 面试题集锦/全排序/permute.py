#coding=utf-8

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

if __name__ == "__main__":
    string = input("输入字符：")
    print(permute(string))
