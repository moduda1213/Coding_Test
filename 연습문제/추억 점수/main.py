def solution(name, yearning, photo):
    result = []
    
    name_scroe = dict(zip(name, yearning))
    
    for people in photo:
        result.append(sum([name_scroe.get(human, 0) for human in people]))
        
    print(result)
    
    return None

if __name__ == "__main__":
    name = ["may", "kein", "kain", "radi"]
    yearning = [5, 10, 1, 3]
    photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]	
    
    solution(name, yearning, photo)