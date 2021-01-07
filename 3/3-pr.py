"""
n명중 두명을 뽑아 짝지어 짝을 지을 수 있는 모든 조합을 출력하는 알고리즘을 작성하십시오.
예를 들어 리스트 ["Tom", "Jerry", "Mike"]이라면 
Tom - Jerry
Tom - Mike
Jerry - Mike
3가지를 출력함
"""
# i , j 로 같지 않을 경우를 변수 b에 add 하는 ?


def mate(a):
    n = len(a)
    result = set()
    for i in range(0, n-1):
        for j in range(i+1, n):
            if a[i] != a[j]:
                result.add(a[i] + "-" + a[j])
    return result


name = ["ab", "bc", "cd"]
print(mate(name))
