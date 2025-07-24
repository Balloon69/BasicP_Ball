# def pnt_hello(year):
#     print("Hello starterpack #",year)

# pnt_hello("2005")


# def my_sum(num1,num2):
#     return num1 + num2

# total = my_sum(50,20)
# print(total)


# def eat_rice (has_rice,has_spoon):
#     if has_rice == True and has_spoon:
#         return "มีข้าวมีช้อนกินได้"
#     else:
#         return "ไม่มีข้าวไม่มีช้อนไม่กินแล้วว"
    
# print(eat_rice(True,True))


# def cal (num1,num2,cmd):
#     print("cal",num1,cmd,num2)
#     if cmd == "+":
#         return num1 + num2
#     elif cmd == "-":
#         return num1 - num2
    
# print("total",cal(50,10,"+"))

# box = ["cat","dog"]
# box[1] = "tiger"
# print(box[1])
# print(box)

# box_fruit = ["grape","banana","apple","orange","dragonfruit"]

# for i in box_fruit:
#     if i == "apple":
#         print("so yummy")
#     else:
#         print("not found")


# box_fruit = ["grape","banana","apple","orange","dragonfruit"]
# def findfruit (b):
#     for i in b:
#         if i == input("find : "):
#             print("so yummy")
#         else:
#             print("not found")

# print(findfruit)

# student = {"name":"Teerapat","age":18,"ID":68130500034}
# if student["age"] >= 18:
#     print("pass")
# else :
#     print("not pass")


students = [{"name": "Thanasorn Dusadeeroj", "age": 19, "ID": 67130500014},
            {"name": "satit", "age": 15, "ID": 6713050047}]
for student in students:
    if student["age"] >= 18:
        print("เกิน")
    else:
        print("ไม่เกิน")
