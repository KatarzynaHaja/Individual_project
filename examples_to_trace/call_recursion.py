import numpy

from examples_to_trace import recursion_example


def call_recursion(a,b):
    if a>b:
    	recursion_example.foo(b)
    else:
    	numpy.zeros(2)

