Algebra of Boole

All the work referenced to [Boole Reduction: A challenge for programmers | MathFoundations 269 | N J Wildberger (youtube.com)](https://www.youtube.com/watch?v=AJr44JgbKho&list=PLIljB45xT85CnIGIWb7tH1F_S2PyOC8rb&index=19)，The relevant code is in [shanyoumu461/Algebra-of-Boole: Algebra Of Boole (github.com)](https://github.com/shanyoumu461/Algebra-of-Boole/tree/main).

`LogicJudge.py` is used to judge logical expressions. You can use this library to make simple logical judgments. The logical expressions containing specific symbols"-->、|、&、~"：

+ "-->": reasoning,
+ "|": or,
+ "&": and,
+ "~": not.

You can use it in the following ways:

```python
python UI.py
```

![UI1](picture\UI1.png)

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

If you find our work useful to your research, please consider citing:

```shell
@Online{Algebra of Boole,
  accessed = {2025-05-30},
  author   = {shanyoumu},
  title    = {Algebra of Boole},
  url      = {https://github.com/shanyoumu461/Algebra-of-Boole},
}
```
