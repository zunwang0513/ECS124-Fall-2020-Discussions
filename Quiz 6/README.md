# Instructions

For this assignment, upload a single python file named `lcs.py`. Your submission won't be graded if it has a different file name.

Your code must have a function named `main` that will tkae as input the two input strings and return the LCS. The tester will load the strings itself and will call this function from your code with them:

```
import lcs # your code
lcs = lcs.main(v, w)
```

Your code will work as long as you have the `main` function defined. As there are multiple LCS strings possible, the tester will check if your output matches the LCS length and if it is a subsequences of both inputs.

Look at the example file `lcs.py` for a sekelton code.

You can run the tester as below:

```
python tester.py
```

Your `lcs.py` file should be in the same directory as the tester.
