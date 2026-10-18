'''
# 최소공배수로 탐색 상한선 설정
# 완전탐색 구현
    알고리즘의 효율성을 판단하는 절대적인 기준은 데이터의 크기입니다.
    이 문제의 제한사항을 수학적으로 뜯어보겠습니다.
    신호등의 개수: 각 신호등의 최대 주기: G + Y + R 우리가 탐색해야 하는 최대 시간(상한선)은 앞서 말씀드린 대로 전체 주기의 **최소공배수(LCM)**입니다. 
    20 이하의 숫자 5개를 골라 만들 수 있는 가장 큰 최소공배수는 언제일까요? 서로소인 가장 큰 수들을 곱했을 때입니다.즉, 19 x 17 x 16 x 13 x 11 = 739,024초가 우리가 탐색해야 할 최악의 경우(Worst Case)입니다.
    파이썬 기준으로 1초에 약 2,000만 번에서 1억 번의 연산을 수행할 수 있습니다. 최대 74만 번 정도의 루프를 도는 것은 0.1초도 걸리지 않는 매우 가벼운 작업입니다.
    오히려 이 문제를 수식으로 우아하게 풀겠다고 구간의 교집합을 구하거나 중국인의 나머지 정리(CRT) 같은 복잡한 수학적 알고리즘을 도입하는 것은, 
    불필요한 예외 처리를 양산하고 구현 시간을 갉아먹는 **전형적인 오버엔지니어링(Over-engineering)**입니다.
'''
from datetime import datetime

def get_gcb(a: int, b: int) -> int:
    """ 
    최대공약수 ==> b가 0이 될 때까지 a와 b의 자리를 교체하며 나머지 연산(유클리드 호제법)
    유클리드 호제법의 핵심 수학적 원리는 **"두 수 A와 B의 최대공약수는 B와 'A를 B로 나눈 나머지'의 최대공약수와 같다"**는 것
    """
    # while b>0:
    #     temp = b
    #     b = a % b
    #     a = b
    # return a
        
    while b > 0:
        a, b = b, a % b
    return a
        
def get_lcm(a: int, b: int) -> int:
    """
    최소공배수
    math.lcm()
    numpy.lcm()
    """
    return (a * b) // get_gcb(a, b) # 최소공배수 공식 : 두 수 곱 // 최대공약수

def isYellow(t: int, g: int, y: int, r: int ) -> bool:
    cycle = g + y + r
    curr = t % cycle
    # 시간 t일 때, 현재 주기의 진행 상태가 g 이상이고 g+y 미만이면 노란불
    return g <= curr < g+y

def solution(signals: list) -> int:
    print(f"starttime: {datetime.now()}")
    
    period = 1
    for g, y, r in signals:
        cycle =g + y + r
        period = get_lcm(period, cycle)
        print(f"period: {period}")
    # java의 잔재
    # for t in range(period):
    #     isCheck = True
    #     for s in signals:
    #         if not isYellow(t, s[0], s[1], s[2]):
    #             isCheck = False
    #             break
        
    #     if isCheck:
    #         answer = t
    #         break
    
    for t in range(period):
        if all(isYellow(t,g,y,r) for g, y, r in signals):
            print(f"endtime: {datetime.now()}")
            return t+1
        
    print(f"endtime: {datetime.now()}")
    return -1
    
if __name__ == "__main__":
    solution([[2, 3, 2], [3, 1, 3], [2, 1, 1]])

