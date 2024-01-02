Algebra of Boole

You can use this library to make simple logical judgments：Use logical expressions containing specific symbols"-->、|、&、~"：

+ "-->": reasoning,
+ "|": or,
+ "&": and,
+ "~": not.

You can use it in the following ways:

```python
python UI.py
```

![1704180996771](image/README/1704180996771.png)

 `BaseClass.py` is for object-oriented

+ `SymBol/DesymBol: ` a class or the negation of a class, representing `p or ~p`；
+ `Proposition:` proposition class, representing `p-->q`;
+ `Relation:` relationship class, representing `p|q or p&q`；
+ `LogicalExperssion:` Logical expression class.

You can use it in the following ways:

```python
python BaseClass.py
```

Then there will be the following results:

```python
The original statement is:  ((People-->Die) AND (Socrates-->People))-->((Socrates-->Die))
Convert the original statement into a logical expression: ((a-->b) & (c-->a))-->((c-->b))
The corresponding relationship between original language and logical expression symbols is: {'People': 'a', 'Die': 'b', 'Socrates': 'c'}
The judgment result is: True
```
