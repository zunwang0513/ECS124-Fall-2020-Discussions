# Instructions

For this assignment, upload a single python file named `neighbors.py`. Your submission won't be graded if it has a different file name.

Your code must have a function named `main` that will take as input the integer `n`  and the matrix `D` as a list of lists and return the tree `t` as a dictionary of dictionaries, i.e to encode an edge that goes from node 1 to node 4 with the weight of 8 do:

```
# assume t is the tree
t[1][4] = 8.0
```

Note that leaf and node labels should be integers as described in the Rosalind page:

http://rosalind.info/problems/ba7e/

Run the tester as below:

```
python tester.py
```

Your `neighbors.py` file should be in the same directory as the tester for the above to work.
