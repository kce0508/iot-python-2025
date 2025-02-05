# py03_while_statement.py

# while 반복문 : for문으로 변경 가능
# while (조건이 참인동안):
#       구문안에서 반복

# 1~10까지의 수를 합산
sum = 0
i = 0

while i <=10:
    sum += i  # sum = sum + 1
    i += 1    # i = i + 1 같은 의미, += -= *= /= ...
    
print(f'합은 {sum}')


sum = 0
for j in range(1, 10 + 1):
    sum += j

print(f'합은 {sum}')
