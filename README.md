# Collatz Conjecture plotter
This  code calculates and visulizes amount of Collatz operations applied from 1 to a user provided integer. 
------------
### What are Collatz operations?
Collatz operations are formed by these 2 simple operations:
- `3n + 1` if n is odd.
- `n/2` if n is even.

### What is Collatz Conjecture?
Collatz Conjecture is a theory which asserts that all positive integers undergoing Collatz conjecture repetaedly will eventually lead us to the integer 1. By 2020, all integers from 1 to 2<sup>68</sup> have been tried and none of them found to be disproving.<sup>[[1]](https://link.springer.com/article/10.1007/s11227-020-03368-x)</sup>

### Definition
[![definition](https://raw.githubusercontent.com/BoraDere/Collatz-Conjecture-plotter/main/2023-02-02%2012_08_24-%7B_displaystyle%20f(n)%3D%7B_begin%7Bcases%7D%7B_frac%20%7Bn%7D%7B2%7D%7D%26%7B_text%7Bif%20%7D%7Dn_equiv%200%7B_pm...png "definition")](https://raw.githubusercontent.com/BoraDere/Collatz-Conjecture-plotter/main/2023-02-02%2012_08_24-%7B_displaystyle%20f(n)%3D%7B_begin%7Bcases%7D%7B_frac%20%7Bn%7D%7B2%7D%7D%26%7B_text%7Bif%20%7D%7Dn_equiv%200%7B_pm...png "definition")
------------
### Requirements
`matplotlib` is required to run this code. To install, run `pip install matplotlib` via terminal.

------------
For testing purposes 100.000.000 is given as input. The goal was to achieve [this](https://en.wikipedia.org/wiki/Collatz_conjecture#/media/File:Collatz_Conjecture_100M.jpg "this") graph and calculate how much time would it take on my computer (it took ~3200 seconds, which is about 53 minutes). Time testing is purely optional and can be deactivated with ease. Result:

[![https://raw.githubusercontent.com/BoraDere/Collatz-Conjecture-plotter/main/2023-02-09%2020_04_03-Figure%201.png](https://raw.githubusercontent.com/BoraDere/Collatz-Conjecture-plotter/main/2023-02-09%2020_04_03-Figure%201.png "https://raw.githubusercontent.com/BoraDere/Collatz-Conjecture-plotter/main/2023-02-09%2020_04_03-Figure%201.png")](https://raw.githubusercontent.com/BoraDere/Collatz-Conjecture-plotter/main/2023-02-09%2020_04_03-Figure%201.png "https://raw.githubusercontent.com/BoraDere/Collatz-Conjecture-plotter/main/2023-02-09%2020_04_03-Figure%201.png")
