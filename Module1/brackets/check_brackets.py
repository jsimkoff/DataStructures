# python2

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    ob_index = []

    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            ob_index.append(i)

        if next in ")]}":
            if not opening_brackets_stack:
                # print("empty stack")
                return False, i+1
            top = opening_brackets_stack.pop()
            if not are_matching(top, next):
                # print("not matching")
                return False, i+1
            else:
                ob_index.pop()


    if not opening_brackets_stack:
        return True, None
    else:
        # print("finished for loop - non empty stack")
        return False, ob_index[0]+1




def main():
    text = raw_input()
    mismatch, i = find_mismatch((text))
    if mismatch == 1:
        print("Success")
    if mismatch == 0:
        print(i)
    # Printing answer, write your code here



if __name__ == "__main__":
    main()
