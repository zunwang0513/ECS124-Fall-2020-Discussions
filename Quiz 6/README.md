# Instructions

For this assignment, upload a single python file named `lcs.py`. Your submission won't be graded if it has a different file name.

Your code should open a text file named `rosalind.txt` and read the input from it:

```
with open('rosalind.txt') as input_file:
    # parse input
```

An example input file is provided in this directory.

The script `tester.sh` will run your code on the given input and grade it accordingly. You should make sure your code works with this script. For final grading a larger input file will be used to test your codes.

```
chmod +x tester.sh
./tester.sh /path/to/your/python/file
```

there is dummy file provided that will just print the solution for the example input:

```
./tester.sh dummy.py
```
