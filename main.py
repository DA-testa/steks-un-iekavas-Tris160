# python3 Marks Kacens-Adamovics,221RDB461

from collections import namedtuple
import requests
Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_bracekets_stack.append(Bracet(next, i - 1))

        if next in ")]}":
          if not opening_bracets_stack:
          return i + 1
          if not are_matching(opening_bracets_stack[-1].char, next):
          return i + 1

          opening_bracets_stack.pop()
          if opening_bracets_stack:
          return opening_bracets_stack[0].position
          else:
          return "Success"
def main():
    cont = input()
    if "I" in cont:
    text = input()
   mismatch = find_mismatch(text)
   print(mismatch)
    # Printing answer, write your code here
else:
text = input()
mismatch = find_mismatch(text)
print(mismatch)

if __name__ == "__main__":
    main()
