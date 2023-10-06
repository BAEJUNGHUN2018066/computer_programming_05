print("구구단을 출력합니다. \n")
for x in range(2, 10):
    print("-------[" + str(x) + "단] -------")
    for y in range(1, 10):
        print(x, "x", y, "=", x*y)
print("---------------------")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[0], matrix[1], matrix[2])

for row in matrix:
    for element in row:
        print(element)


matrix = [[1,2,3], [4], [5,6,7,8,9]]

total = 0

for row in matrix:
    for element in row:
        total = total +element

results = []
pingpong_list = ["나영", "예진", "원빈", "현빈"]

def create_contents_of_mail(pingpong_list):
    for i in pingpong_list:
        result = ["한국교통대학교 천하제일 탁구대회,", 'i',"님 탁구 대회에 참여해주셔서 감사합니다."
              "행사 일시 : 2023-10-06, 시간 : 10:30 AM, 복장 : 트레이닝복"
              ,"행사 당일에 뵙겠습니다." , 'i','님', '감사합니다']
        return result
    result.append(results)

print(results)
