def checkNum( num, num_sum):
    if num_sum == num:
        return True
    if num_sum < num:
        return False
    for i in range(1,len(str(num))+1):
        num_one = num_sum % (10 ** i)
        if num_one > num:
            continue
        num_two = int(num_sum / (10 ** i))
        if num_one + num_two == num:
            return True
        if checkNum(num - num_one, num_two):
            return True
    return False

if __name__ == '__main__':
    out = 0
    for i in range(1, 11):
        if checkNum(i, i * i):
            out = out + i * i
    print(out)