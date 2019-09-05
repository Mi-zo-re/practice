a = str(input("请输入一个计算算式,比如(4+8),可以输入多项式，但暂不可以使用括号:"))
b = list(a)
i = 0
n = []
m = []
v = ""
w = ""
p = ""
t = int
f = int
y = int(1)
while i <= len(b)-1:
    if b[i] == " ":
        i += 1
    elif (b[i] == "1" or b[i] == "2" or b[i] == "3" or b[i] == "4" or b[i] == "5" or b[i] == "6" or b[i] == "7" \
            or b[i] == "8" or b[i] == "9"or b[i] == "0") and i < len(b) - 1:
        n.append(b[i])
        i += 1
        while (b[i] != "+" or b[i] != "-") and i < len(b) - 1:
            if b[i] == "1" or b[i] == "2" or b[i] == "3" or b[i] == "4" or b[i] == "5" or b[i] == "6" or b[i] == "7" \
                    or b[i] == "8" or b[i] == "9" or b[i] == "0" :
                n.append(b[i])
                if i < len(b) - 1:
                    i += 1
                if i == len(b)-1:
                    break
            elif b[i] == " ":
                i += 1
            else:
                break
        for mem in n:
            u = str(mem)
            v = v + u
        t = int(v)
        n.clear()
        v = ""
    elif b[i] == "+" or b[i] == "-":
        p = str(b[i])
        i += 1
        while (b[i] != "+" or b[i] != "-") and i <= len(b) - 1:
            if b[i] == "1" or b[i] == "2" or b[i] == "3" or b[i] == "4" or b[i] == "5" or b[i] == "6" or b[i] == "7" \
                    or b[i] == "8" or b[i] == "9"or b[i] == "0":
                m.append(b[i])
                if i < len(b)-1:
                    i += 1
                    if b[i] == "+" or b[i] == "-":
                        break
                elif i == len(b)-1:
                    break
        for mem in m:
            u = str(mem)
            w = w + u
        f = int(w)
        m.clear()
        w = ""
        if p == "+":
            t = t + f
        elif p == "-":
            t = t - f
        print("进行了一次运算")

    else:
        print(t)
        break