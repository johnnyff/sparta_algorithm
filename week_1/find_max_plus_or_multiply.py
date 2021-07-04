#Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 "X"혹은 "+"연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램
# 단, 모든 연산은 왼쪽에서 순서대로 이루어진다.

input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    result = 0
    for num in array:
        if (num<=1 or result<=1):
            result+=num
        else:
            result*=num
    return result


result = find_max_plus_or_multiply(input)
print(result)