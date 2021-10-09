scores = []

members = int(input("enter members number: "))

students_num = 0
temp = 0

for i in range(members):
    students_num += 1
    s = int(input(f"enter the scores of student number{students_num}:"))
    temp = (s+temp)
    scores.append(s)

print("average score :",temp/members)
print("the greatest score is : " , max(scores))
print("the least score is : " , min(scores))


