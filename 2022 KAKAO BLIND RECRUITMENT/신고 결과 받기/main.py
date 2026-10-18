from collections import Counter

def solution(id_list, report, k):
    
    # # 신고 한번 당 한명 
    # # 중복 가능 but a가 b를 두번 신고해도 한번으로 처리 x
    # # 신고 2번 되면 정지
    # # 신고했던 사람에게 정지메시지 전송
    
    '''case 1
    테스트 1 〉	통과 (0.03ms, 11.2MB)
    테스트 2 〉	통과 (0.04ms, 11.3MB)
    테스트 3 〉	통과 (136.67ms, 42.5MB)
    테스트 4 〉	통과 (0.05ms, 11.3MB)
    테스트 5 〉	통과 (0.05ms, 11.3MB)
    테스트 6 〉	통과 (0.64ms, 11.4MB)
    테스트 7 〉	통과 (1.26ms, 11.7MB)
    테스트 8 〉	통과 (2.20ms, 12.1MB)
    테스트 9 〉	통과 (49.85ms, 26.3MB)
    테스트 10 〉통과 (39.81ms, 26MB)
    테스트 11 〉통과 (109.58ms, 42.4MB)
    테스트 12 〉통과 (1.27ms, 11.5MB)
    테스트 13 〉통과 (1.00ms, 11.5MB)
    테스트 14 〉통과 (84.42ms, 23.4MB)
    테스트 15 〉통과 (83.17ms, 37.3MB)
    테스트 16 〉통과 (0.21ms, 11.4MB)
    테스트 17 〉통과 (0.77ms, 11.3MB)
    테스트 18 〉통과 (1.53ms, 11.5MB)
    테스트 19 〉통과 (1.75ms, 11.5MB)
    테스트 20 〉통과 (81.75ms, 23.3MB)
    테스트 21 〉통과 (111.87ms, 37.3MB)
    테스트 22 〉통과 (0.03ms, 11.3MB)
    테스트 23 〉통과 (0.03ms, 11.1MB)
    테스트 24 〉통과 (0.03ms, 11.3MB)
    '''
    
    # answer = [0] * len(id_list)
    
    # reporter_list = {user: set() for user in id_list}
    
    # for record in report:
    #     reporter, reported = record.split(" ")
    #     print(reporter, reported)
    #     reporter_list.setdefault(reporter, set()).add(reported)
    
    
    # print(reporter_list)
    
    
    # reported_count = Counter(
    #     user
    #     for users in reporter_list.values()
    #     for user in users
    # )
    
    # print(reported_count)
    # for idx, reported_list in enumerate(reporter_list.values()):
    #     for reported, count in reported_count.items():
    #         if count >= k and reported in reported_list: 
    #             answer[idx] += 1
    
    # return answer

    '''case 2
    테스트 1 〉	통과 (0.04ms, 11.2MB)
    테스트 2 〉	통과 (0.04ms, 11.3MB)
    테스트 3 〉	통과 (97.99ms, 42.4MB)
    테스트 4 〉	통과 (0.05ms, 11.4MB)
    테스트 5 〉	통과 (0.05ms, 11.4MB)
    테스트 6 〉	통과 (0.60ms, 11.8MB)
    테스트 7 〉	통과 (1.14ms, 11.8MB)
    테스트 8 〉	통과 (2.81ms, 12.3MB)
    테스트 9 〉	통과 (38.30ms, 26.2MB)
    테스트 10 〉통과 (37.42ms, 26.4MB)
    테스트 11 〉통과 (93.17ms, 42.4MB)
    테스트 12 〉통과 (0.20ms, 11.3MB)
    테스트 13 〉통과 (0.20ms, 11.3MB)
    테스트 14 〉통과 (32.61ms, 23.5MB)
    테스트 15 〉통과 (63.43ms, 37.7MB)
    테스트 16 〉통과 (0.15ms, 11.3MB)
    테스트 17 〉통과 (0.21ms, 11.5MB)
    테스트 18 〉통과 (0.28ms, 11.5MB)
    테스트 19 〉통과 (0.46ms, 11.5MB)
    테스트 20 〉통과 (32.67ms, 23.7MB)
    테스트 21 〉통과 (62.01ms, 37.7MB)
    테스트 22 〉통과 (0.02ms, 11.4MB)
    테스트 23 〉통과 (0.03ms, 11.4MB)
    테스트 24 〉통과 (0.02ms, 11.2MB)
    '''
    
    # answer = []
        
    # reporter_list = {user: set() for user in id_list}
    
    # for record in report:
    #     reporter, reported = record.split()
    #     reporter_list[reporter].add(reported)
    # print(reporter_list)
    
    # reported_count = Counter(
    #     reported
    #     for reported_users in reporter_list.values()
    #     for reported in reported_users
    # )
    # print(reported_count)
    # print(type(reported_count))
    
    # answer = [
    #     sum(reported_count[reported] >= k for reported in reporter_list[reporter])
    #     for reporter in id_list
    # ]
    
    # return answer

    '''
    case 3
    테스트 1 〉	통과 (0.03ms, 11.3MB)
    테스트 2 〉	통과 (0.04ms, 11.5MB)
    테스트 3 〉	통과 (142.80ms, 65MB)
    테스트 4 〉	통과 (0.05ms, 11.3MB)
    테스트 5 〉	통과 (0.05ms, 11.3MB)
    테스트 6 〉	통과 (0.68ms, 11.9MB)
    테스트 7 〉	통과 (1.44ms, 12.1MB)
    테스트 8 〉	통과 (2.29ms, 12.7MB)
    테스트 9 〉	통과 (67.08ms, 37.2MB)
    테스트 10 〉통과 (55.21ms, 37.1MB)
    테스트 11 〉통과 (136.42ms, 64.7MB)
    테스트 12 〉통과 (0.16ms, 11.5MB)
    테스트 13 〉통과 (0.16ms, 11.5MB)
    테스트 14 〉통과 (53.82ms, 30.9MB)
    테스트 15 〉통과 (90.09ms, 45.3MB)
    테스트 16 〉통과 (0.12ms, 11.3MB)
    테스트 17 〉통과 (0.17ms, 11.3MB)
    테스트 18 〉통과 (0.26ms, 11.4MB)
    테스트 19 〉통과 (0.50ms, 11.7MB)
    테스트 20 〉통과 (52.21ms, 30.8MB)
    테스트 21 〉통과 (94.75ms, 45.4MB)
    테스트 22 〉통과 (0.03ms, 11.4MB)
    테스트 23 〉통과 (0.03ms, 11.5MB)
    테스트 24 〉통과 (0.03ms, 11.4MB)
    '''
    answer = []
    
    unique_reports = {tuple(record.split()) for record in report}
    print(unique_reports)
    
    reported_count = Counter(
        reported for reporter, reported in unique_reports
    )
    print(reported_count)
    
    suspended = {
        user for user, count in reported_count.items()
        if count >= k
    }
    print(suspended)
    
    notice_count = Counter(
        reporter
        for reporter, reported in unique_reports
        if reported in suspended
    )
    print(notice_count)
    answer = [notice_count[user] for user in id_list]
    
    return answer
    

if __name__ == "__main__":
    id_list = ["muzi", "frodo", "apeach", "neo"]
    report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    # id_list = ["con", "ryan"]
    # report = ["ryan con", "ryan con", "ryan con", "ryan con"]
    k = 2
    print(solution(id_list, report, k))
    pass