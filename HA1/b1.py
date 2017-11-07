def luhn(acc_nbr):
    acc_ints = [int(x) for x in acc_nbr[:-1]]
    checksum = 0
    for index, i in enumerate(acc_ints[::-1]):
        if (index % 2 == 0):
            double = i*2
            digitsum = sum([int(x) for x in list(str(double))])
            checksum += digitsum
        else:
            checksum += i
    return str(checksum * 9)[-1] == str(acc_nbr)[-1]


def find_x(acc_nbr):
    for x in range(10):
        ans = luhn(acc_nbr.replace('X', str(x)))
        if ans:
            return x
    return -1
        

if __name__ == '__main__':
    inputs = [
            "12774212857X4109",
            "586604X108627571",
            "7473X86953606632",
            "4026467X45830632",
            "20X3092648604969",
    ]
    ans = ''
    with open('testin.txt','r') as biginput:
        for line in biginput:
            line = line.strip()
            ans += str(find_x(line))

    print(ans)
    