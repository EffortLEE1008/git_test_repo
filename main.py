def adder(num1, num2):
    return num1+num2


if __name__=='__main__':
    u_input = input('Enter tow num: ')
    num1, num2 = [int(c) for c in u_input.split()]
    print(adder(num1,num2))
