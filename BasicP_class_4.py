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


# students = [{"name": "Thanasorn Dusadeeroj", "age": 19, "ID": 67130500014},
#             {"name": "satit", "age": 15, "ID": 6713050047}]
# for student in students:
#     if student["age"] >= 18:
#         print("เกิน")
#     else:
#         print("ไม่เกิน")




food = [
    {"number": "1", "name_food": "กะเพราหมูกรอบ", "meat": "หมุกรอบ", "price": 600},
    {"number": "2", "name_food": "กะเพราหมู", "meat": "หมู", "price": 550},
    {"number": "3", "name_food": "กะเพราไก่", "meat": "ไก่", "price": 500},
    {"number": "4", "name_food": "กะเพราเนื้อ", "meat": "เนื้อ", "price": 900},
    {"number": "5", "name_food": "กะเพราทะเล", "meat": "กุ้ง+หมึก", "price": 800}
]

# แสดงเมนูอาหารภายในร้าน
def show_manu(m):
    for i in m:
        print(i["number"], "ชื่ออาหาร", i['name_food'], "ราคา", i['price'])

print(show_manu(food))

print("---------------------------------------------------------------------")

# รับคำสั่งอาหาร
manu_food = input("สั่งอาหาร :")
if manu_food == "1":
    egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
    if egg == "1":
        p = 600 + 150
    else:
        p = 600
elif manu_food == "2":
    egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
    if egg == "1":
        p = 550 + 150
    else:
        p = 550
elif manu_food == "3":
    egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
    if egg == "1":
        p = 500 + 150
    else:
        p = 500
elif manu_food == "4":
    egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
    if egg == "1":
        p = 900 + 150
    else:
        p = 900
elif manu_food == "5":
    egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
    if egg == "1":
        p = 800 + 150
    else:
        p = 800
else:
    print("ไม่มีเมนูนี้")
    exit()

print("ราคา:", p, "บาท")

print("---------------------------------------------------------------------")

# รับวิธีกิน
take = input("1กินที่ร้าน, 2กลับบ้าน: ")
if take == "1":
    print("กินร้าน")
else:
    print("กลับบ้าน")

print("---------------------------------------------------------------------")

# วิธีจ่ายเงิน
pay = input("1.สแกน หรือ 2.จ่ายเงินสด: ")
if pay == "2":
    money = int(input("เงิน : "))
    if money >= p:
        cal = money - p
        print("เงินทอน:", cal, "บาท")
    else:
        print("ยอดเงินไม่พอ ขาดอีก", p - money, "บาท")
else:
    print("กรุณาสแกนจ่ายเงินจำนวน", p, "บาท ขอบคุณค่ะ")

