Python 3.4.4 (v3.4.4:737efcadf5a6, Dec 20 2015, 20:20:57) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> word = "pizza"
KeyboardInterrupt
>>> word = "pizza"
>>> print(pizza[0.5])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(pizza[0.5])
NameError: name 'pizza' is not defined
>>> print(pizza[0:5])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(pizza[0:5])
NameError: name 'pizza' is not defined

>>> print(word[0:5])
pizza
>>> print(word[2:5])
zzaprint(word[2:])
SyntaxError: multiple statements found while compiling a single statement
>>> print(word[2:5])
zza
>>> print(word[2:])
zza
>>> 
