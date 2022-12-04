[Hello](https://cs50.harvard.edu/x/2020/psets/6/hello/#hello)
=============================================================

Implement a program that prints out a simple greeting to the user, per the below.

```
$ python hello.py
What is your name?
David
hello, David

```

[Specification](https://cs50.harvard.edu/x/2020/psets/6/hello/#specification)
-----------------------------------------------------------------------------

Write, in a file called `hello.py` in `~/pset6/hello`, a program that prompts a user for their name, and then prints `hello, so-and-so`, where `so-and-so` is their provided name, exactly as you did in [Problem Set 1](https://cs50.harvard.edu/x/2020/psets/1/), except that your program this time should be written (a) in Python and (b) in CS50 IDE.

[Usage](https://cs50.harvard.edu/x/2020/psets/6/hello/#usage)
-------------------------------------------------------------

Your program should behave per the example below.

```
$ python hello.py
What is your name?
Emma
hello, Emma

```

[Testing](https://cs50.harvard.edu/x/2020/psets/6/hello/#testing)
-----------------------------------------------------------------

No `check50` for this problem, but be sure to test your code for each of the following.

-   Run your program as `python hello.py`, and wait for a prompt for input. Type in `Emma` and press enter. Your program should output `hello, Emma`.
-   Run your program as `python hello.py`, and wait for a prompt for input. Type in `Rodrigo` and press enter. Your program should output `hello, Rodrigo`.

[How to Submit](https://cs50.harvard.edu/x/2020/psets/6/hello/#how-to-submit)
-----------------------------------------------------------------------------

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 cs50/problems/2020/x/sentimental/hello
```