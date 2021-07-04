# Q. 0과 1로만 이루어진 문자열이 주어졌을떄, 이 문자열에 있는 모든 숫자를 전부 같게 만드려고 한다. 할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
# 주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오

input = "011110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    cnt_0 = 0
    cnt_1 = 0
    if (string[0]=="0"):
        cnt_1 +=1
    if (string[0]=="1"):
        cnt_0 +=1

    for i in range(len(string)-1):
        if(string[i]!=string[i+1]):
            if (string[i]=="0"):
                cnt_0+=1
            else :
                cnt_1 +=1

    return min(cnt_0,cnt_1)


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

