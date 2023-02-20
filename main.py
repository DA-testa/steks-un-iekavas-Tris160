# python3 Marks Kacens-Adamovics,221RDB461

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            if not opening_brackets_stack:
                return i + 1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else:
        return "Success"

def main():
    cont = input()
    if "F" in cont:
        with open(cont, "r") as f:
            text = f.read()
        text = input()
    # Printing answer, write your code here
    else:
        cont = input()
    mismatch = find_mismatch(cont)
    print(mismatch)

if __name__ == "__main__":
    main()
