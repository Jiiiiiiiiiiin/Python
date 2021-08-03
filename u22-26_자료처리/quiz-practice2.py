

# 23.6 연습문제: 3차원 리스트 만들기
# 다음 소스 코드를 완성하여 
# 높이 2, 세로 크기 4, 가로 크기 3인 3차원 리스트를 만드세요
# (리스트 표현식 사용)

a = 0
[[[0 for col in range(3)] for row in range(4)] for depth in range(2)]

# Unit 23 심사문제 지뢰찾기
# 표준 입력으로 2차원 리스트의 가로(col)와 세로(row)가 입력되고 
# 그 다음 줄부터 리스트의 요소로 들어갈 문자가 입력됩니다. 
# 이때 2차원 리스트 안에서 *는 지뢰이고 .은 지뢰가 아닙니다. 
# 지뢰가 아닌 요소에는 인접한 지뢰의 개수를 
# 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다)

# 여러 줄을 입력 받으려면 다음과 같이 for 반복문에서 input을 호출한 뒤 
# append로 각 줄을 추가하면 됩니다(list 안에 문자열을 넣으면
#  문자열이 문자 리스트로 변환됩니다).

# matrix = []
# for i in range(row):
#    matrix.append(list(input()))

col, row = map(int, input().split())

matrix = []
for i in range(row):
    matrix.append(list(input()))

for i in matrix:
    for k in i:
        print(k, end=' ')
    print()

for i in range(row):
    for k in range(col):
        if matrix[i][k] == "*":
            print(matrix[i][k], sep='', end='')
        else:
            count = 0
            for x in range(i-1,i+2):
                for y in range(k-1,k+2):
                    if x<0 or y<0 or x>=row or y>=col :
                        continue
                    elif matrix[x][y] == "*":
                        count += 1
            print(count, sep='', end='')
    print()



# 24.4 연습문제: 파일 경로에서 파일명만 가져오기
#다음 소스 코드를 완성하여 파일 경로에서 파일명만 출력되게 만드세요. 
# 단, 경로에서 폴더의 깊이가 달라지더라도 파일명만 출력할 수 있어야 합니다.

path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
x = path.split('\\')
filename=x[-1]


# 24.5 심사문제: 특정 단어 개수 세기
# 표준 입력으로 문자열이 입력됩니다. 
# 입력된 문자열에서 'the'의 개수를 출력하는 프로그램을
# 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다).
# 단, 모든 문자가 소문자인 'the'만 찾으면 되며
# 'them', 'there', 'their' 등은 포함하지 않아야 합니다

a = input().split()
count=0
for words in a:
    if (words.strip(',.')=='the'):
        count+=1
print(count)


# 24.6 심사문제: 높은 가격순으로 출력하기
# 표준 입력으로 물품 가격 여러 개가 문자열 한 줄로 입력되고, 
# 각 가격은 ;(세미콜론)으로 구분되어 있습니다. 입력된 
# 가격을 높은 가격순으로 출력하는 프로그램을 만드세요
# (input에서 안내 문자열은 출력하지 않아야 합니다). 
# 이때 가격은 길이를 9로 만든 뒤 오른쪽으로 정렬하고 
# 천단위로 ,(콤마)를 넣으세요.


prices = list(map(int,input().split(';')))
a = prices.sort(reverse=True)
for i in prices:
    f'{i:,>9d}'


# 25.7 연습문제: 평균 점수 구하기

average = sum(maria.values()) / len(maria)


# 25.8 심사문제: 딕셔너리에서 특정 값 삭제하기

# 표준 입력으로 문자열 여러 개와 숫자 여러 개가 두 줄로 입력되고, 
# 첫 번째 줄은 키, 두 번째 줄은 값으로 하여 딕셔너리를 생성합니다. 
# 다음 코드를 완성하여 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 
# 30인 키-값 쌍을 삭제하도록 만드세요.



keys = input().split()
values = map(int, input().split())
 
x = dict(zip(keys, values))
 
x = {key:value for key, value in x.items() if value != 30}
x = {key:value for key, value in x.items() if key != 'delta'}

print(x)

# 26.8 연습문제: 공배수 구하기
# 다음 소스 코드를 완성하여 1부터 100까지 숫자 중 
# 3과 5의 공배수를 세트 형태로 출력되게 만드세요.

a = {i for i in range(1,101) if i % 3 == 0}
b = {i for i in range(1,101) if i % 5 == 0}

print(a & b)


# 26.9 심사문제: 공약수 구하기
# 표준 입력으로 양의 정수 두 개가 입력됩니다. 
# 다음 소스 코드를 완성하여 두 숫자의 공약수를 
# 세트 형태로 구하도록 만드세요. 
# 단, 최종 결과는 공약수의 합으로 판단합니다.

x, y = map(int,input().split())

a = {i for i in range(1,x+1) if x%i==0}
b = {i for i in range(1,y+1) if y%i==0}

divisor = a & b

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)