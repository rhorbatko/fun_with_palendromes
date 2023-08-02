def solution(S: str):
    PALINDROME_SIDES = []
    PALINDROME_MIDDLE = []
    # turn string into list of integers
    int_list = [int(char) for char in S]
    # get uniques
    uniques = set(int_list)
    if len(uniques) == 1 and list(uniques)[0] == 0:
        return f"{list(uniques)[0]}"
    else:
        # find number frequency
        freq = [[number, int_list.count(number)] for number in uniques]
        # distribute pairs evenly between center/sides of PALINDROME
        for entry in freq:
            # check if frequency is even
            if entry[1] % 2 == 0:
                for i in range(0, int(entry[1] / 2)):
                    PALINDROME_SIDES.append(entry[0])

            # handle odd frequency
            else:
                # put one in middle to make it even on the ends
                PALINDROME_MIDDLE.append(entry[0])
                # handle just like the even freq loop
                for i in range(0, entry[1] // 2):
                    PALINDROME_SIDES.append(entry[0])

        # organize and stitch the SIDES, MIDDLE lists together
        palindrome_start = sorted(PALINDROME_SIDES, reverse=True)
        palindrome_end = sorted(PALINDROME_SIDES)

        PALINDROME_LIST = palindrome_start + [max(PALINDROME_MIDDLE)] + palindrome_end

        return "".join(str(n) for n in PALINDROME_LIST)
