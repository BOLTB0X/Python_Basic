# https://school.programmers.co.kr/learn/courses/30/lessons/181844?language=python3
def solution(arr, delete_list):
    answer = arr
    for ele in delete_list:
        if ele in answer:
            answer.remove(ele)
    return answer