import math

EPSILON = 1e-5
DELTA = 1e-3
SEGMENTS = 100

def identity():
    """return the mathematical function f such that f(x) = x
    ">>>identity()(3)
    3
    """
    def f(x):
        return x
    return f
x = identity()
print(x(6))

def sin_function():
    """return the mathematical function f such that f(x) = sin(x)
    '>>> sinF()(math.pi/2)
    1.0
    """
    def sin(x):
        return math.sin(x)

    return sin
sin = sin_function()
print(sin(math.pi/2))


g = lambda x: x*3
h = lambda x: x*2
def sum_functions(g, h):
    """return f s.t. f(x) = g(x)+h(x)"""
    def f(x):
        return g(x)+ h(x)
    return f

f  = sum_functions(g, h)
print(f(3))


def sub_functions(g, h):
    """return f s.t. f(x) = g(x)-h(x)"""
    def f(x):
        return h(x)- g(x)
    return f


def mul_functions(g, h):
    """return f s.t. f(x) = g(x)*h(x)"""
    def f(x):
        return g(x)* h(x)
    return f

def div_functions(g, h):
    """return f s.t. f(x) = g(x)/h(x)"""
    def f(x):
        return g(x)/ h(x)
    return f

    # The function solve assumes that f is continuous.
    # solve return None in case of no solution
def solve(f, x0=-10000, x1=10000, epsilon=EPSILON):
    """return the solution to f in the range between x0 and x1"""


    pass

    # inverse assumes that g is continuous and monotonic.
def inverse(g, epsilon=EPSILON):
    """return f s.t. f(g(x)) = x"""
    pass


def compose(g, h):
    """return the f which is the compose of g and h """
    pass


def derivative(g, delta=DELTA):
    """return f s.t. f(x) = g'(x)"""
    pass


def definite_integral(f, x0, x1, num_of_segments=SEGMENTS):
    """
    return a float - the definite_integral of f between x0 and x1
    >>>definite_integral(const_function(3),-2,3)
    15
    """
    pass


def integral_function(f, delta=0.01):
    """return F such that F'(x) = f(x)"""
    pass


def ex11_func_list():
    """return a list of functions as a solution to q.12"""
    pass































