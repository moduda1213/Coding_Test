# 순열 == Permutation (중복 O) :  nPr = n! / (n-r)!
## case 1
def permutation_case1(n, r):
    result = 1
    
    for i in range(1,n+1)[:n-r:-1]:
        result *= i
    print(result)
    
permutation_case1(5,3)

## case 2
def permutation_case2(arr, r):
    arr = sorted(arr) # ['A','E','H','D']
    used = [0 for _ in range(len(arr))] # [0, 0, 0, 0]
    
    def generate(chosen, used):
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            if not used[i] and (i == 0 or arr[i-1] != arr[i] or used[i-1]):
                #if arr[i] not in chosen:
                chosen.append(arr[i])
                used[i]=1
                generate(chosen, used)
                used[i]=0
                chosen.pop()
                
    generate([], used)
    
permutation_case2('AACD',2)




# 조합 == Combination (중복 X) : nCr = n! / r!(n-r)!
## case 1
def combinations_case1(n,r):
    result1 = 1
    r = min(r, n-r)
    
    for i in range(0,r):
        result1 *= (n-i)//(1+i)
    print(result1)    
    
combinations_case1(5,3)

def combinations_case2(arr, r):
    arr = sorted(arr)
    print(arr)
    def generate(chosen):
        if len(chosen) == r:
            print(chosen)
            return
        
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        
        for nxt in range(start, len(arr)):
            chosen.append(arr[nxt])
            generate(chosen)
            chosen.pop()
    generate([])
    
combinations_case2('ABCDE', 3)