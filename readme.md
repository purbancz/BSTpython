# Binary Search Tree (BST) in Python

[![github](https://img.shields.io/badge/GitHub-purbancz-181717.svg?style=flat&logo=github)](https://github.com/purbancz)
[![x](https://img.shields.io/badge/Twitter-@purbancz-00aced.svg?style=flat&logo=x)](https://twitter.com/purbancz)
[![linkedin](https://img.shields.io/badge/LinkedIn-Piotr_Urbańczyk-00aced.svg?style=flat&logo=linkedin)](https://www.linkedin.com/in/piotr-urba%C5%84czyk-9943ab17a/)
[![website](https://img.shields.io/badge/Website-Piotr_Urbańczyk-5087B2.svg?style=flat&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHg9IjBweCIgeT0iMHB4IiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGQ9Ik0gMTIgMi4wOTk2MDk0IEwgMSAxMiBMIDQgMTIgTCA0IDIxIEwgMTAgMjEgTCAxMCAxNCBMIDE0IDE0IEwgMTQgMjEgTCAyMCAyMSBMIDIwIDEyIEwgMjMgMTIgTCAxMiAyLjA5OTYwOTQgeiIgZmlsbD0iI2ZmZiI+PC9wYXRoPgo8L3N2Zz4=)](https://www.copernicuscenter.edu.pl/en/person/urbanczyk-piotr-2/)

This repository provides a simple implementation of a Binary Search Tree (BST) in Python. It includes a  `Node`  class to
represent individual nodes in the tree, a  `BST`  class for the tree itself, and a  `BstIotIterator`  class for
iterating over the tree in an In-Order Traversal (IOT) manner.

This code was created during the Languages and Libraries of Data Analysis course at the Faculty of Computer Science
of the AGH University of Cracow.

## Usage

    bst = BST()
    bst.insert(10)
    bst.insert(15)
    bst.insert(5)
    print(10 in bst)  # Prints: True
    bst.print_in_order_traversal()  # Prints: 5 10 15
