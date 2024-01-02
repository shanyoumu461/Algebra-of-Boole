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
def BooleReduce(string : str) -> str:
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

def Boolstr2symstr(string : str) -> str:  ## 将boolean表达式转成sympy的表达式
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


### 从符号的右边开始找到第一个整体的逻辑表达式, string[i]非空
########## 返回逻辑表达式的最右端位置和整个表达式子
def findrightsymbol(string : str, i : int):
    if string[i] == '(':
        j = i+1
        flag = 1
        while (j < len(string) and flag != 0):
            if (string[j] == ')'):
                flag -= 1
                if flag == 0:
                    break
            elif (string[j] == '('):
                flag += 1
            j += 1
        return j, string[i: j+1]
    else:
        j = i
        while (j < len(string) and string[j] != ' ' and string[j] != '~' and string[j] != '&' and string[j] != '|' and string[j] != ')' and string[j] != '(' and string[j] != '-'):
            j += 1
        return j-1, string[i: j]

def findleftsymbol(string : str, i : int):
    if string[i] == ')':
        j = i-1
        flag = 1
        while (j >= 0 and flag != 0):
            if (string[j] == '('):
                flag -= 1
                if flag == 0:
                    break
            elif (string[j] == ')'):
                flag += 1
            j -= 1
        return j, string[j : i+1]
    else:
        j = i
        while (j >= 0 and string[j] != ' ' and string[j] != '~' and string[j] != '&' and string[j] != '|' and string[j] != ')' and string[j] != '(' and string[j] != '-'):
            j -= 1
        return j+1, string[j+1: i+1]

########### 返回字符串中逻辑符号的位置    
def findlogicsymbol(string : str):
    i = 0
    while(i < len(string)):
        if (string[i] == '&' or string[i] == '~' or string[i] == '|' or string[i] == '-'):
            break
        i += 1
    return i

### 将逻辑表达式转成Boolean Algebra
def Logic2algbra(string : str) -> str:
    stringtemp = string
    i = findlogicsymbol(stringtemp)
    while (i != len(stringtemp)):
        # print(i, stringtemp)
        if (stringtemp[i] == '&'):
            idxi = i+1
            idxj = i-1
            while(idxi < len(stringtemp) and stringtemp[idxi] == ' '):
                idxi += 1
            while(idxj >= 0 and stringtemp[idxj] == ' '):
                idxj -= 1
            rightj, strj = findrightsymbol(stringtemp, idxi)
            lefti, stri = findleftsymbol(stringtemp, idxj)
            strand = stri + strj
            string1 = stringtemp
            stringtemp = string1[0:lefti] + strand + string1[rightj+1:]

        elif (stringtemp[i] == '|'):
            idxi = i+1
            idxj = i-1
            while(idxi < len(stringtemp) and stringtemp[idxi] == ' '):
                idxi += 1
            while(idxj >= 0 and stringtemp[idxj] == ' '):
                idxj -= 1
            rightj, strj = findrightsymbol(stringtemp, idxi)
            lefti, stri = findleftsymbol(stringtemp, idxj)
            stror = "(" + stri + " + " + strj + " + "+ stri + strj + ")"
            string1 = stringtemp
            stringtemp = string1[0:lefti] + stror + string1[rightj+1:]
        elif (stringtemp[i] == '~'):
            idxi = i+1
            while(idxi < len(stringtemp) and stringtemp[idxi] == ' '):
                idxi += 1
            rightj, strj = findrightsymbol(stringtemp, idxi)
            strnot = "(1 + " + strj + ")"
            string1 = stringtemp
            stringtemp = string1[0:i] + strnot + string1[rightj+1:]
        else:
            idxi = i+3
            idxj = i-1
            while(idxi < len(stringtemp) and stringtemp[idxi] == ' '):
                idxi += 1
            while(idxj >= 0 and stringtemp[idxj] == ' '):
                idxj -= 1
            rightj, strj = findrightsymbol(stringtemp, idxi)
            lefti, stri = findleftsymbol(stringtemp, idxj)
            stror = "(1 + " + stri + " + " + stri + strj + ")"
            string1 = stringtemp
            stringtemp = string1[0:lefti] + stror + string1[rightj+1:] 
        i = findlogicsymbol(stringtemp)
    return stringtemp


def LogicDetermine():
    string = input("请输入仅包含&、|、~、()、-->的逻辑表达式: ")
    print("输入的逻辑表达式为: ", string)
    logstr = Logic2algbra(string)
    print("输入的逻辑表达式转成布尔表达式为: ",logstr)
    symstr = Boolstr2symstr(logstr)
    res = BooleReduce(symstr)
    print("输入的表达式的结果为(1为正确,其他为错误): ", res)

if __name__ == '__main__':
    LogicDetermine()