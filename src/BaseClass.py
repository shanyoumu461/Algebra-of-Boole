from LogicDeterime import *

## 符号类，可代表集合/命题前提（结论）等 包含p/~p
class SymBol():
    def __init__(self, arg = None):
        if isinstance(arg, str):
            self.name = arg 
        else: 
            pass 
    def setname(self, name:str):
        self.name = name
    def __str__(self):
        return self.name 
    
class DesymBol(SymBol):
    def __init__(self, arg=None):  
        if isinstance(arg, str):  
            super().__init__(arg)  
        elif isinstance(arg, SymBol):  
            self.name = arg.name  
        else:  
            super().__init__()  
    def __str__(self):
        return "(NOT " + self.name + ")"
    
### 命题类，p-->q，输入的只能是SymBol/DesymBol
class Proposition():
    def __init__(self, sym1=None, sym2=None):  
        if sym1 is not None and sym2 is not None:  
            self.Sym1 = sym1  
            self.Sym2 = sym2  
        else:  
            self.Sym1 = None  
            self.Sym2 = None  
    ### 设置命题前后两者sym1-->sym2的关系
    def setpre(self, sym1:SymBol):
        self.Sym1 = sym1
    def setpost(self, sym2:SymBol):
        self.Sym2 = sym2 
    def __str__(self):
        return str(self.Sym1) + "-->" + str(self.Sym2)
### 关系类 p&q / p|q
class Relation():
    def __init__(self, sym1=None, sym2=None, relation:str = "AND"):  
        if sym1 is not None and sym2 is not None:  
            self.Sym1 = sym1  
            self.Sym2 = sym2
            self.relation = relation
        else:  
            self.Sym1 = None  
            self.Sym2 = None  
            self.relation = relation
    def setSymbol1(self, sym1:SymBol):
        self.Sym1 = sym1
    def setSymbol2(self, sym2:SymBol):
        self.Sym2 = sym2 
    def setRelation(self, relation:str):
        self.relation = relation
    def __str__(self):
        if (self.relation.upper() == "AND"):
            return str(self.Sym1) + " AND " + str(self.Sym2)
        elif (self.relation.upper() == "OR"):
            return str(self.Sym1) + " OR " + str(self.Sym2)
        else:
            print("Non-compliant! Set relation and/or ")

     
class LogicalExperssion():
    def __init__(self) -> None:
        self.condition = []     #### 逻辑表达式的条件
        self.conclusion = []    #### 待判断的结论
        self.realname2symbol = []   ### 将a,b,c...转成逻辑表达式的真实名字 
        self.symbol2realname = {}   ### 将逻辑表达式中的真实名字转成a,b,c...
        pass
    def addcondition(self, condition):      ### condition和conclusion要么是命题，要么是符号
        self.condition.append(condition)
        if (isinstance(condition, SymBol)):
            if (condition.name in self.realname2symbol):
                pass 
            else:
                self.realname2symbol.append(condition.name)
                self.symbol2realname[condition.name] = chr(len(self.realname2symbol) - 1 + ord('a'))
        else:
            if (condition.Sym1.name in self.realname2symbol):
                pass 
            else:
                self.realname2symbol.append(condition.Sym1.name)
                self.symbol2realname[condition.Sym1.name] = chr(len(self.realname2symbol) - 1 + ord('a'))
            
            if (condition.Sym2.name in self.realname2symbol):
                pass 
            else:
                self.realname2symbol.append(condition.Sym2.name)
                self.symbol2realname[condition.Sym2.name] = chr(len(self.realname2symbol) - 1 + ord('a'))
        
    def addconclusion(self, conclusion):
        self.conclusion.append(conclusion)
    def __str__(self):              ### 表达式可视化
        string = "("
        for i in range(len(self.condition)):
            string += "(" + str(self.condition[i]) + ")"
            if (i != len(self.condition) - 1):
                string += " AND "
        string += ")-->("
        for i in range(len(self.conclusion)):
            string += "(" + str(self.conclusion[i]) + ")"
            if (i != len(self.conclusion) - 1):
                string += " AND "
        string += ")"
        return string
    def getlogicExp(self):
        
        string = "("
        for i in range(len(self.condition)):
            if (isinstance(self.condition[i], SymBol)):
                string += "(" + str(self.condition[i]).replace(self.condition[i].name ,self.symbol2realname[self.condition[i].name]).replace("NOT", "~") + ")"
            else:
                string +=  "(" + str(self.condition[i]).replace(self.condition[i].Sym1.name ,self.symbol2realname[self.condition[i].Sym1.name]).\
                    replace("NOT", "~").replace("AND", "&").replace(self.condition[i].Sym2.name ,self.symbol2realname[self.condition[i].Sym2.name]) + ")"
            if (i != len(self.condition) - 1):
                string += " & "
        string += ")-->("
        
        for i in range(len(self.conclusion)):
            if (isinstance(self.conclusion[i], SymBol)):
                string += "(" + str(self.conclusion[i]).replace(self.conclusion[i].name ,self.symbol2realname[self.conclusion[i].name]).replace("NOT", "~") + ")"
            else:
                string +=  "(" + str(self.conclusion[i]).replace(self.conclusion[i].Sym1.name ,self.symbol2realname[self.conclusion[i].Sym1.name]).\
                    replace("NOT", "~").replace("AND", "&").replace(self.conclusion[i].Sym2.name ,self.symbol2realname[self.conclusion[i].Sym2.name]) + ")"
            if (i != len(self.conclusion) - 1):
                string += " & "
        string += ")"
        return string
    def LogicDetermine(self):
        string = self.getlogicExp()
        # print("输入表达式转成逻辑表达式为: ", string)
        logstr = Logic2algbra(string)
        # print("输入的逻辑表达式转成布尔表达式为: ",logstr)
        symstr = Boolstr2symstr(logstr)
        res = BooleReduce(symstr)
        # print("输入的表达式的结果为(1为正确,其他为错误): ", res)
        if (res == "1"):
            return True
        else:
            return False
        
    ###### 将自然语言中的变量转成简单变量
    def GetSymbolTrans(self):
        return self.symbol2realname
        
def main():
    A = SymBol("People")
    B = SymBol("Die")
    C = SymBol("Socrates")

    condition1 = Proposition(A, B)
    condition2 = Proposition(C, A)

    conculusion = Proposition(C, B)
    LogicExp = LogicalExperssion()
    LogicExp.addcondition(condition1)
    LogicExp.addcondition(condition2)
    LogicExp.addconclusion(conculusion)

    print("原始语句为：", LogicExp)
    print("将原始语句转成逻辑表达式为：",LogicExp.getlogicExp())
    print("原始语言与逻辑表达式符号对应关系为: ", LogicExp.GetSymbolTrans())
    print("判断结果为：", LogicExp.LogicDetermine())

if __name__ == '__main__':
    main()