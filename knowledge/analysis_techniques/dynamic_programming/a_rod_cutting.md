# Rod Cutting

### Problem Formulation
Given a rod of length $n$ inches and a table of prices $p_i$ for $i = 1, 2, ..., n$, where $i$ is the length of the wood, 

e.g.

| Length of Wood $i$ | Price|
| ------------- |:-------------:|
| 1| $p_1$|
| 2| $p_2$|
| 3| $p_3$|
| ...| ...|
| n| $p_n$|


determine the <font color = red>***maximum revenue $r_n$***</font> obtainable by cutting up the rod and selling the pieces. 

### Optimal Substructure
The optimal solution to a large problem is composed of optimal solutions to multiple smaller independent tasks.

In this case, we can decompose the problem in this manner:
$$r_n = \max{\{p_i + r_{n-i}:i\in[1,n]\}}$$

In 
