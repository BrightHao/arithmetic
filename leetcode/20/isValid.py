import os
import sys
sys.path.append(os.path.abspath('../struct'))
from stack import Stack

class Solutinon:
    def isValid(self, s):
        st = Stack()
        paren_map = {")": "(", "]": "[", ">": "<", "}": "{"}
        for c in s:
            if c not in paren_map:
                st.append(c)
            elif not st.list or paren_map[c] != st.pop():
                return False
        return not st.list

if __name__ == "__main__":
    s = Solutinon()
    res = s.isValid("[](){[()]}")
    print(res)
