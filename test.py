from turtle import *


def branch(length):
    if length < 1:
        return

    forward(length)
    left(30)
    branch(length/2)
    right(60)
    branch(length/2)
    left(30)
    forward(-length)

branch(200)