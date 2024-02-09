# 백준 1331

## Solution 1 
def draw_star(n):
    if n == 1:
        return ['*']
    
    stars = draw_star(n-1)
    pattern = []
    
    # 첫 번째 행
    pattern.append('*' * (4 * (n-1) + 1))
    
    # 재귀적으로 형성된 패턴을 중간에 삽입
    for star in stars:
        pattern.append('* ' + star + ' *')
    
    # 중앙에 있는 별들
    for star in stars:
        pattern.append('* ' + ' '.join(star) + ' *')
    
    # 마지막 행
    pattern.append('*' * (4 * (n-1) + 1))
    
    return pattern

# 입력 받기
N = int(input().strip())

# 별 찍기
star_pattern = draw_star(N)

# 출력하기
for pattern in star_pattern:
    print(pattern)
