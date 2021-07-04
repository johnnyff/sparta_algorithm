input = 20


def find_prime_list_under_number(number):
    result = []
    for i in range(2,number+1):
        cnt = 0
        for j in range(1,i):
            if(i%j==0):
                cnt+=1
        if(cnt==1):
            result.append(i)
    return result


result = find_prime_list_under_number(input)
print(result)

input = "011110"

