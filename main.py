if __name__ == '__main__':
    unparsed_number = input()
    power = 0
    parsed_number = 0

    for i in range(len(unparsed_number) - 1, -1, -1):
        unparsed_digit = unparsed_number[i]
        unicode = ord(unparsed_digit)

        parsed_number += pow(10, power) * (unicode - ord('0'))
        power += 1

    print(parsed_number)

