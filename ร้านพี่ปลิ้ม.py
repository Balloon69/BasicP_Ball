# #ร้านพี่ปลิ้มมึงลองยัง กะเพราพี่ปลิ้ม
# food = [
#     {"number":"1","name_food":"กะเพราหมูกรอบ","meat":"หมุกรอบ","price":600},
#     {"number":"2","name_food":"กะเพราหมู","meat":"หมู","price":550},
#     {"number":"3","name_food":"กะเพราไก่","meat":"ไก่","price":500},
#     {"number":"4","name_food":"กะเพราเนื้อ","meat":"เนื้อ","price":900},
#     {"number":"5","name_food":"กะเพราทะเล","meat":"กุ้ง+หมึก","price":800}
# ]

# #แสดงเมนููอาหารภายในร้าน
# def show_manu(m):
#     for i in  m:
#         print(i["number"],"ชื่ออาหาร",i['name_food'],"ราคา",i['price'])
# print(show_manu(food))

# print("---------------------------------------------------------------------")
# # def restaurant (oder):
# manu_food = input("สั่งอาหาร :")
# if  manu_food == "1":
#     egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
#     if egg == "1":
#         p = 600 + 150
#         print("ราคา :",p)
#     else:
#         print("600")
# elif  manu_food == "2":
#     egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
#     if egg == "1":
#         p = 550 + 150
#         print("ราคา :",p)
#     else:
#         print("550")
# elif  manu_food == "3":
#     egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
#     if egg == "1":
#         p = 500 + 150
#         print("ราคา :",p)
#     else:
#         print("500")
# elif  manu_food == "4":
#     egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
#     if egg == "1":
#         p = 900 + 150
#         print("ราคา :",p)
#     else:
#         print("900")
# elif  manu_food == "5":
#     egg = input("เพิ่มไข่ดาวไหม(1.เพิ่ม/2.ไม่เพิ่ม) :")
#     if egg == "1":
#         p = 800 + 150
#         print("ราคา :",p)
#     else:
#         print("800")

# take = input("1กินที่ร้าน,2กลับบ้าน")
# if take == 1:
#     print("กินร้าน")
# else:
#     print("กลับบ้าน")
        
# pay = input("1.สแกน หรือ 2.จ่ายเงินสด: ")
# if pay == "2":
#     money = int(input("เงิน : "))
#     if money >= p:
#         cal = money - p
#         print("เงินทอน:", cal, "บาท")
#     else:
#         print("ยอดเงินไม่พอ ขาดอีก", p - money, "บาท")
# else:
#     print("กรุณาสแกนจ่ายเงินจำนวน", p, "บาท ขอบคุณค่ะ")
    
print ("ร้านพี่ปลิ้มมึงลองยัง กะเพราพี่ปลิ้ม")


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

# วิธีกิน
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




    
        

    

    





