from typing import List

def read_integers() -> List[int]:
    user = input().split(",")
    ans = []
    for i in user:
        ans.append(int(i))
    return ans
# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
