from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next == '\n':
            continue
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            if not are_matching(opening_brackets_stack[-1].char, next):
                return i + 1
            opening_brackets_stack.pop()

    if opening_brackets_stack:
        return opening_brackets_stack[0].position

    return "Success"


def main():
    text = input()
    if "F" in text:
        for i in range(6):
            with open(f"test/{i}") as f:
                text = f.read()
                mismatch = find_mismatch(text)
                print(mismatch)
    if "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)