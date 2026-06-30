Score Calculator - Development Trail
=====================================

Rendition 1 (score_calculator_v1.py)
--------------------------------------
Basic implementation. Prompts the user to enter scores one at a time
and type "done" to finish. Calculates and prints the average.

No error handling - entering anything other than a number or "done"
will crash the program with a ValueError.


Rendition 2 (score_calculator_v2.py)
--------------------------------------
Added error handling using a try/except block. If the user enters
something that is not a number or "done", the program now prints
an error message and continues instead of crashing.


Final Product (score_calculator.py)
--------------------------------------
Added .strip() to the input so that entries with leading or trailing
spaces are handled correctly. A score like " 85 " is now treated the
same as "85".
