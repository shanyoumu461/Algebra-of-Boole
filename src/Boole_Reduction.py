#################
######### 这个文件为将boolean 表达式化简成多项式
import sympy as sp

## 将单个的表达式化简，例如（A**2*B**3 -->AB）
def reducesymbol(string: str):
    idx = 0
    result = ""
    length = len(string)
    while(idx < length and string[idx] == ' '):
        idx += 1
    if(string[idx] >= '1' and string[idx] <= '9'):   ###前面有系数
        while(idx < length and string[idx] >= '0' and string[idx] <= '9'):
            idx += 1
        if (int(string[idx-1])- 0 ) % 2 == 0:
            return "0"
        while (idx < length and string[idx] == ' '):
            idx += 1
    if (idx == length):                    ### 这一段只是数字
        return "1"
    while(idx < length):
        while(idx < length and (string[idx] == '*' or (string[idx] >= '0' and string[idx] <= '9'))):   ### 去掉数字
            idx += 1
        if (idx == length):
            return result
        tempchar = string[idx]
        if (tempchar == ' '):
            idx += 1
            continue
        result += tempchar
        idx += 1
    return result

################# 将sympy表达式化简
def BooleReduce(string : str):
    varset = set()
    for s in string:
        if(s != ' ' and s != '+' and s != '*' and s != '(' and s != ')'):
            varset.add(s)
    sp.var(varset)
    parts = str(sp.expand(string)).split("+")
    res = set()    ####### 保存最后结果
    for partstr in parts:
        tempstr = reducesymbol(partstr)
        if (tempstr == "0"):
            continue
        if (tempstr in res):
            res.remove(tempstr)
            continue
        res.add(tempstr)
    resultlist = list(res)
    resultlist.sort()
    result = ""
    for val in resultlist:
        result += val 
        result += " + "
    return result[:-3]

def Boolstr2symstr(string : str):  ## 将boolean表达式转成sympy的表达式
    def issymbol(c):
        return c!=' ' and c!='+' and c!='(' and c!=')'
    result = ""
    idx = 0
    length = len(string)
    while(idx < length):
        if (issymbol(string[idx])):
            result += string[idx]
            if idx < length -1 and (issymbol(string[idx+1]) or string[idx+1] == '('):    
                result += "*"
        elif string[idx] == ')':
            result += string[idx]
            if idx < length -1 and (issymbol(string[idx+1]) or string[idx+1] == '('):    
                result += "*"
        else:
            result += string[idx]
        idx += 1
    return result


def main():
    string = "(1 + (((1 + p + pq))p) + (((1 + p + pq))p)q)"
    symstr = Boolstr2symstr(string)
    print(f"化简前表达式为: ", string)
    print(f"sympy表达式为: ", symstr)
    print(f"化简后表达式为: ", BooleReduce(symstr))


if __name__ == '__main__':
    main()