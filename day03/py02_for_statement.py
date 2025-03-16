# py02_for_statement.py

# for문: 프로그래밍의 꽃
# 반복을 처리할 때 사용
# for 변수 in 반복할 값:
#    구문안으로...

# 아래와 출력되는 프로그램을 작성하시오
'''
최대별수 : 4
*
**
***
****
'''

# range() 범위를 생성 클래스
# 마지막수 : max - 1
# range(8) -> range(0, 8)
# range(init, max, add)
print(range(0, 8, 2))

# for i in[0, 1, 2, 3, 4, 5, 6, 7]: # 이 조건이 참인동안 반복...
# for i in range(0, 8, 2):
#     print(i)

# num = int(input('최대별수: '))

# for i in range(1, num + 1):
#     print('*' * i)

# 구구단
# 2단부터 2x9 ~ 9x9
# 2 x 1 = 2, 2 x 2 = 4, 2 x 3 = 6
# 9 x 1 = 9, ... 9 x 9 = 81
# 요사1 - 한 줄에 각 단씩 나오도록
# 요사2 - x * y값이 항상 두줄씩 표현되도록
# 단 시작을 표시
for x in range(2, 9 + 1):
    if x == 5: break
    # if x == 5: continue        # x가 5면 아래 코드 실행하지 않고 다음 x로 넘어감

    print(f'{x}단 시작 ')
    for y in range(1, 9 + 1):

        # if y == 8: break
        print(f'{x} x {y} = {x * y:2d}', end='   ')

    print() # 그냥 한줄 내리기


print('구구단종료\n\n\n\n')

## 반복을 빠져나올때 : break
## 반복문에서 특정 조건을 지나칠 때 : continue
