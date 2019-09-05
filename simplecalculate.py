# 定义变量的时候变量名要能告诉别人变量是干嘛用的，或者在变量后面加注释
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
number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
while i <= len(b)-1:
    if b[i] == " ":
        i += 1
    #elif (b[i] == "1" or b[i] == "2" or b[i] == "3" or b[i] == "4" or b[i] == "5" or b[i] == "6" or b[i] == "7" \
    #       or b[i] == "8" or b[i] == "9"or b[i] == "0") and i < len(b) - 1:
    elif (b[i] in number) and (i < len(b)-1): # 可以缩短代码并且增加代码的复用能力
        n.append(b[i])
        i += 1
        while (b[i] != "+" or b[i] != "-") and i < len(b) - 1:
            # if b[i] == "1" or b[i] == "2" or b[i] == "3" or b[i] == "4" or b[i] == "5" or b[i] == "6" or b[i] == "7" \
                    # or b[i] == "8" or b[i] == "9" or b[i] == "0" :
            if b[i] in number:
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
            # if b[i] == "1" or b[i] == "2" or b[i] == "3" or b[i] == "4" or b[i] == "5" or b[i] == "6" or b[i] == "7" \
            #         or b[i] == "8" or b[i] == "9"or b[i] == "0":
            if b[i] in number:
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