[Credit](https://cs50.harvard.edu/x/2020/psets/6/credit/#credit)
================================================================

Implement a program that determines whether a provided credit card number is valid according to Luhn's algorithm.

```
$ python credit.py
Number: 378282246310005
AMEX

```

[Specification](https://cs50.harvard.edu/x/2020/psets/6/credit/#specification)
------------------------------------------------------------------------------

-   In `credit.py` in `~/pset6/credit/`, write a program that prompts the user for a credit card number and then reports (via `print`) whether it is a valid American Express, MasterCard, or Visa card number, exactly as you did in [Problem Set 1](https://cs50.harvard.edu/x/2020/psets/1/), except that your program this time should be written (a) in Python and (b) in CS50 IDE.
-   So that we can automate some tests of your code, we ask that your program's last line of output be `AMEX\n` or `MASTERCARD\n` or `VISA\n` or `INVALID\n`, nothing more, nothing less.
-   For simplicity, you may assume that the user's input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
-   Best to use `get_int` or `get_string` from CS50's library to get users' input, depending on how you to decide to implement this one.

[Usage](https://cs50.harvard.edu/x/2020/psets/6/credit/#usage)
--------------------------------------------------------------

Your program should behave per the example below.

```
$ python credit.py
Number: 378282246310005
AMEX

```

[Testing](https://cs50.harvard.edu/x/2020/psets/6/credit/#testing)
------------------------------------------------------------------

No `check50` for this problem, but be sure to test your code for each of the following.

-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `378282246310005` and press enter. Your program should output `AMEX`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `371449635398431` and press enter. Your program should output `AMEX`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `5555555555554444` and press enter. Your program should output `MASTERCARD`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `5105105105105100` and press enter. Your program should output `MASTERCARD`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `4111111111111111` and press enter. Your program should output `VISA`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `4012888888881881` and press enter. Your program should output `VISA`.
-   Run your program as `python credit.py`, and wait for a prompt for input. Type in `1234567890` and press enter. Your program should output `INVALID`.

[How to Submit](https://cs50.harvard.edu/x/2020/psets/6/credit/#how-to-submit)
------------------------------------------------------------------------------

Execute the below, logging in with your GitHub username and password when prompted. For security, you'll see asterisks (`*`) instead of the actual characters in your password.

```
submit50 cs50/problems/2020/x/sentimental/credit
```