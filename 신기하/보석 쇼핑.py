'''
정확성  테스트
테스트 1 〉	통과 (0.02ms, 10.3MB)
테스트 2 〉	통과 (0.11ms, 10.1MB)
테스트 3 〉	통과 (0.39ms, 10.1MB)
테스트 4 〉	통과 (0.19ms, 10.2MB)
테스트 5 〉	통과 (0.12ms, 10.1MB)
테스트 6 〉	통과 (0.01ms, 10.2MB)
테스트 7 〉	통과 (0.02ms, 10.1MB)
테스트 8 〉	통과 (2.90ms, 10.3MB)
테스트 9 〉	통과 (2.83ms, 10.1MB)
테스트 10 〉	통과 (0.40ms, 10.2MB)
테스트 11 〉	통과 (1.26ms, 10.3MB)
테스트 12 〉	통과 (4.64ms, 10.1MB)
테스트 13 〉	통과 (6.81ms, 10.2MB)
테스트 14 〉	통과 (8.30ms, 10.4MB)
테스트 15 〉	통과 (13.84ms, 10.4MB)
효율성  테스트
테스트 1 〉	통과 (29.82ms, 10.5MB)
테스트 2 〉	통과 (86.49ms, 10.7MB)
테스트 3 〉	통과 (100.19ms, 10.9MB)
테스트 4 〉	통과 (38.09ms, 12.2MB)
테스트 5 〉	통과 (596.52ms, 12MB)
테스트 6 〉	통과 (93.86ms, 11.9MB)
테스트 7 〉	통과 (894.42ms, 12.7MB)
테스트 8 〉	실패 (시간 초과)
테스트 9 〉	통과 (317.52ms, 13.4MB)
테스트 10 〉	통과 (887.83ms, 13.9MB)
테스트 11 〉	실패 (시간 초과)
테스트 12 〉	실패 (시간 초과)
테스트 13 〉	실패 (시간 초과)
테스트 14 〉	실패 (시간 초과)
테스트 15 〉	실패 (시간 초과)
채점 결과
정확성: 33.3
효율성: 40.0
합계: 73.3 / 100.0
'''

def solution(gems):
    answer = []
    gems_set = set()
    gems_dict = {}
    min_gem = ''
    
    # 보석의 종류 구하기
    for gem in gems:
        gems_set.add(gem)
    
    gems_nums = len(gems_set) # 보석 종류 개수
    min_len = 100000 # 가장 작은 구간을 찾기 위한 설정
    
    for i in range(len(gems)):
        # 보석의 gem, index를 key, value로 걸어 딕셔너리 생성
        if gems[i] in gems_dict:
            gems_dict[gems[i]] = i
        else:
            gems_dict[gems[i]] = i
        
        if len(gems_dict) == gems_nums: # 딕셔너리 길이가 보석 개수와 같다면 보석이 구간 안에 전부 존재
            if min_gem != gems[i]: # 최소 인덱스의 보석이 현재 보석과 달라야 최신화가 가능하기 때문에 조건 설정
                min_gem = min(gems_dict.keys()) # 최소 인덱스의 보석 최신화
                min_idx = min(gems_dict.values()) # 최소 인덱스 뽑기
                max_idx = max(gems_dict.values()) # 최대 인덱스 뽑기
                gap = max_idx - min_idx # 구간의 길이
                
                if gap < min_len: # 구간의 길이가 최소 길이보다 작다면 최신화
                    min_len = gap
                    answer = [min_idx + 1, max_idx + 1]
                    
            else:
                continue
                
    return answer