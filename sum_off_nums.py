def solution(number):

    multiples = 0
    for num in range(number):
        if num % 3 == 0 and num != 0:
            multiples += num
            continue
        if num % 5 == 0 and num != 0:
            multiples += num
            continue

    print(multiples)
    return multiples

solution(93)


def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)
