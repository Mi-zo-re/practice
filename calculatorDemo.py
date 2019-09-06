# l = str(input("请输入一个计算算式,比如(4+8),可以输入多项式:"))
l1 = ""

num = ('1', '2', '3', '4', '5', '6', '7', '8', '9')

op = ('+', '-', '*', '/', '(', ')')
# 存放数字堆栈
num_list = list()

# 存放运算堆栈
option_list = list()

# 检测一个数
def get_number(i):
    is_int = True
    num_buffer = ''
    while i<len(l1):# 作为最后一个数字的跳出条件
        if l1[i] in num:
            num_buffer += l1[i]
        elif l1[i] == '.' and is_int==True:
            is_int = False
            num_buffer += l1[i]
        elif l1[i] == '.' and is_int == False:
            return False # 遇到两个小数点时报错
        else:
            break # 不是数字的时候跳出循环
        i+=1
    if is_int:
        num_list.append(int(num_buffer))
    else:
        num_list.append(float(num_buffer))
    return i

# 获得运算符号
def get_option(i):
    while i < len(l1) and l1[i] in op:
        if l1[i] == ')': # 遇到右括号时处理括号
            handle_bracket()
        elif l1[i] == '(' or len(option_list) == 0 or option_list[len(option_list)-1] == '(':# 三种默认符号直接入栈的情况
            option_list.append(l1[i])
        else:# 对栈顶符号和当前符号进行优先级比较，栈顶优先级不小于当前符号时持续运算
            while get_priority(option_list[len(option_list)-1])>=get_priority(l1[i]):
                do_calculate()
                if len(option_list) == 0:
                    break
            option_list.append(l1[i])
        i+=1
    return i

# 判断运算符号优先级
def get_priority(a):
    if a in ('+', '-'):
        return 1
    elif a in ('*', '/'):
        return 2

# 定义运算规则
def do_calculate():
    # print(num_list)
    # print(option_list)
    # 弹出两个操作数
    a = num_list.pop()
    b = num_list.pop()
    # 弹出一个运算符号
    option = option_list.pop()
    if option == '+':
        num_list.append(a+b)
    elif option == '-':
        num_list.append(b-a)
    elif option == '*':
        num_list.append(a*b)
    elif option == '/':
        num_list.append(b/a)

# 处理括号
def handle_bracket():
    # 直到符号栈栈顶元素为左括号之前一直进行运算
    while option_list[len(option_list)-1] != '(':
        do_calculate()
    # 弹出栈顶的左括号
    option_list.pop()

# 分析字符串
def analyse_str():
    i = 0
    while i<len(l1):
        if l1[i] in num:
            i = get_number(i)
        elif l1[i] in op:
            i = get_option(i)
    # 做完剩下的全部运算
    while len(option_list) > 0:
        do_calculate()
    print(f"{l1}={num_list[0]}")

if __name__ == "__main__":
    l = str(input("请输入一个计算算式,比如\"1+2*(3+4)-5\",可以输入多项式:"))
    l1 = l.replace(" ","")# 除去所有空格
    analyse_str()