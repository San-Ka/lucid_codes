Windows PowerShell
Copyright (C) Microsoft Corporation. All rights reserved.

PS C:\Users\skaur2> python3
python3 : The term 'python3' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ python3
+ ~~~~~~~
    + CategoryInfo          : ObjectNotFound: (python3:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

PS C:\Users\skaur2> python
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 21:26:53) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 2+2
4
>>> 4*3
12
>>> Hello
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Hello' is not defined
>>> "Hello"
'Hello'
>>> 'Hello
  File "<stdin>", line 1
    'Hello
         ^
SyntaxError: EOL while scanning string literal
>>> 'Hello'
'Hello'
>>> #using single line comment
...
>>> """ Hello ther it's multi -line"""
" Hello ther it's multi -line"
>>> 2+@
  File "<stdin>", line 1
    2+@
      ^
SyntaxError: invalid syntax
>>> 2+2
4
>>> 2-0
2
>>> 3*1
3
>>> 4/2
2.0
>>> 1==1
True
>>> 2==1
False
>>> 1!=1
False
>>> 2!=1
True
>>> 20/4
5.0
>>> 3/2
1.5
>>> 10/7
1.4285714285714286
>>> 1>0
True
>>> 3<0
False
>>> 1is1
  File "<stdin>", line 1
    1is1
       ^
SyntaxError: invalid syntax
>>> 1 is 1
True
>>> 2 is 1
False
>>> 1 is not 1
False
>>> 1 is not 2
True
>>> thing_one = 'Alex'
>>> thing_one
'Alex'
>>> thing_two = 'Sandy'
>>> thing_two
'Sandy'
>>> "hello" + "world"
'helloworld'
>>> "hey there" + "  I am running late"
'hey there  I am running late'
>>> "this is a string"[0]
't'
>>> len("can you explain me this")
23
>>> "{} Loves {}." .format
<built-in method format of str object at 0x00EF6E30>
>>> "{} Loves {}." .format "hey" + "there"
  File "<stdin>", line 1
    "{} Loves {}." .format "hey" + "there"
                               ^
SyntaxError: invalid syntax
>>> good_credit = false
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'false' is not defined
>>> good_credit = False
>>> good_credit
False
>>> type(4.60)
<class 'float'>
>>> x= true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> x = true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> X = True
>>> type(x)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'x' is not defined
>>> type(True)
<class 'bool'>
>>> name = "sandy"
>>> age = 42
>>> print( name + "is" + age)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print( name + "is" + str(age))
sandyis42
>>> print( name + "is " + str(age))
sandyis 42
>>> print( name + " is " + str(age))
sandy is 42
>>> name = input("Sandip Kaur")
Sandip Kaur
>>> name = input("Sandip Kaur")
Sandip Kaur Sandy
>>> name
' Sandy'
>>> name = input(" Please Type your name here ")
 Please Type your name here Sandip Kaur
>>> name
'Sandip Kaur'
>>> words = [ "Red", "blue", "yello"]
>>> "sandy" in words
False
>>> "blue" in words
True
>>> len(words)
3
>>> print("My favorite colors are " + words[1] + "!")
My favorite colors are blue!
>>> print("My favorite colors are " + words[3] + "!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> print("My favorite colors are " + words[2] + "!")
My favorite colors are yello!
>>> print("My favorite colors are " + words[0][1][2] + "!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: string index out of range
>>> print("My favorite colors are " + words[0,1,2] + "!")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> print("My favorite colors are " + words[2] + "!")
My favorite colors are yello!
>>> words.append("green")
>>> print(words)
['Red', 'blue', 'yello', 'green']
>>> del words[0]
>>> print(words)
['blue', 'yello', 'green']
>>>