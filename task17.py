ismlar = []

while True:
    ism = input("Ism kiriting (to'xtatish uchun 'stop' deb yozing): ")
    
    if ism.lower() == "stop":
        break
    
    ismlar.append(ism)


print("Kiritilgan ismlar soni:", len(ismlar))