#열번 찍어 안넘어가는 나무 없다
'''
treehit = 0
while treehit <10 :
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다" % treehit)
    if treehit == 10 :
        print("나무 넘어갑니다")
'''

'''
prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number : """
number = 0
while number != 4:
    print(prompt)
    number = int(input())
'''

# 커피 자판기 판매 중지
'''
coffee = 10
money = 300
while money :
    print(" 돈을 받았으니 커피를 줍니다")
    coffee = coffee - 1
    print("남은 커피의 양은 %d 개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 종료합니다")
        break
'''

#자판기 실제 작동과정
'''
coffee = 10
while True  :
    money = int(input("돈을 넣어주세요: "))
    if money ==300:
        print("커피을 줍니다")
        coffee = coffee -1 
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다" %(money-300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다")
        print("남은 커피의 양은 %d개 입니다" % coffee)
    if coffee == 0 :
        print("커피가 다 떨어졌습니다. 판매를 중지합니다")
        break
'''

#continue
'''
a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0 : continue
    print(a)
'''

#3의 배수를 뺀 나머지
'''
a = 0
while a<10:
    a = a + 1
    if a %3 == 0 :continue
    print(a)
'''

# 무한루프
'''
while True :
    print("Ctrl + C를 눌러야 while문을 빠져나갈 수 있습니다.")
'''

