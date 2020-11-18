# Instructions

For this assignment, upload a single python file named `lcs.py`. Your submission won't be graded if it has a different file name.

Your code must have two functions defined with the exact names as below:
* the `lcs` function (equivalent to LCSBackTrack from the pseudocode)
* the `backtrack` function (equivalent to OutputLCS from the backtrack)

The program `teser.py` will import these functions from your code and use them to calculate the LCS. The tester will load the strings itself and will call the corresponding functions from your code with them:

```
import lcs # your code
b = lcs.lcs(v, w) # calls the lcs function from your code
l = lcs.backtrack(b, v, len(v), len(w)) # calls the backtrack function from your code
```

Your code will work as long as you have these functions defined with the same parameters as in the pseudocode. As there are multiple LCS strings possible, the tester will check if your output matches the LCS length and if it is a subsequences of both inputs.

Look at the example file `lcs.py` for a sekelton code.

If you have already solved this assignment, only renaming your functions should be enough to make it pass.
