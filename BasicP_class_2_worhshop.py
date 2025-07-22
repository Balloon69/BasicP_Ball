dis = int(input("ระยะทาง :"))
if dis >= 500:
    print("ราคา : 45 บาท")
elif dis >= 301 and dis <= 500:
    print("ราคา : 35 บาท")
elif dis>= 101 and dis<=300:
    print("ราคา : 25 บาท")
elif dis>= 51 and dis<=100:
    print("ราคา : 15 บาท")
elif dis>=5 and dis<=50:
    print("ราคา : 10 บาท")
else:
    print("ส่งฟรี")
    
