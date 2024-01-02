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


def main():
    string = "((p-->q)&p)-->q"
    stralg = Logic2algbra(string)
    print(stralg)


if __name__ == '__main__':
    main()