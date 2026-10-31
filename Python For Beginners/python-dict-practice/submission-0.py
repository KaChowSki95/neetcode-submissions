from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    ans = {}
    for i in word:
        if i in ans:
            ans[i] += 1
        else:
            ans[i] = 1
    return ans


# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
