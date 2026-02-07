# 11-mashq
try:
    x = float(input())
    print(x)
except:
    print("Float emas")

# 12-mashq
try:
    l = [10, 20, 30]
    print(l[1] / l[5])
except:
    print("Xato indeks")

# 13-mashq
try:
    f = open("/root/test.txt", "w")
except:
    print("Ruxsat yo‘q")

# 14-mashq
try:
    a = int(input())
    b = int(input())
    c = int(input())
    print(a / b + c)
except:
    print("Xatolik bor")

# 15-mashq
try:
    s = input()
    n = int(s)
    print(100 / n)
except:
    print("Xato kiritildi")
