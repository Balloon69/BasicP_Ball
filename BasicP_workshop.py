monster = 5000
sword  = 150
bow    = 200
spear  = 250

while True:
    print("1 โจมตี")
    print("2 หนี")
    option =int(input("พิมพ์ 1/2 เพื่อเลือก"))
    if option == 1:
        round = int(input("round hit :"))
        for i in range (round):
            print("sword = 150")
            print("bow   = 200")
            print("spear = 250")
            weapon = input("เลือกอาวุธ :")
            if weapon == "sword":
                monster = monster - sword
                print(monster)
            elif weapon == "bow":
                monster = monster - bow
                print(monster)
            elif weapon == "spear":
                monster = monster - spear
                print(monster)
        
                    
            if monster < 0 :
                monster = 20
                print(monster)
            elif monster == 0:
                print("win")
                break
        print("lose")
        break
    elif option == 2:
        break

    
