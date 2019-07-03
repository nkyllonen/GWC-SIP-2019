import math

def summation(start, stop):
    sum = 0
    for x in range(start, stop):
        sum += x
    return sum

if __name__ == '__main__':
    output = summation(0,10)
    print("Summation = " , output)
