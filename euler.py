# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# A bunch of helper functions that are used repeatedly throughout the Euler problems.
# 
# This file will be saved off as a .py file, and functions or classes in here will be importable as euler.py

# <codecell>

#Code to use when generating through "n primes"
def postponed_sieve():                   # postponed sieve, by Will Ness      
    yield 2; yield 3; yield 5; yield 7;  # original code David Eppstein, 
    D = {}                               #            ActiveState Recipe 2002
    ps = (p for p in postponed_sieve())  # a separate Primes Supply:
    p = ps.next() and ps.next()          # (3) a Prime to add to dict
    q = p*p                              # (9) when its sQuare is 
    c = 9                                # the next Candidate
    while True:
        if c not in D:                # not a multiple of any prime seen so far:
            if c < q: yield c         #   a prime, or
            else:   # (c==q):         #   the next prime's square:
                add(D,c + 2*p,2*p)    #     (9+6,6 : 15,21,27,33,...)
                p=ps.next()           #     (5)
                q=p*p                 #     (25)
        else:                         # 'c' is a composite:
            s = D.pop(c)              #   step of increment
            add(D,c + s,s)            #   next multiple, same step
        c += 2                        # next odd candidate

def add(D,x,s):                          # make no multiple keys in Dict
    while x in D: x += s                 # increment by the given step
    D[x] = s 

# <codecell>

# I want to only generate primes when I need to (when the number I'm looking for is greater than the primes I've generated so far)

class Prime:
    sieve = postponed_sieve()
    primes = set()
    max_prime = 0
    
    def is_prime(self, n):
        while n > self.max_prime:
            next_prime = self.sieve.next()
            self.primes.add(next_prime)
            self.max_prime = next_prime
                
        if n in self.primes:
            return True
        else:
            return False
        
    def __str__(self):
        return "Maintaining %s primes in memory" % len(self.primes)
    
    def __len__(self):
        return len(self.primes)

# <codecell>

def triangle():
    n = 1
    while True:
        yield n * (n+1) / 2
        n += 1
        
def square():
    n = 1
    while True:
        yield n**2
        n += 1
        
def pentagonal():
    n = 1
    while True:
        yield n * (3*n - 1) / 2
        n += 1

def hexagonal():
    n = 1
    while True:
        yield n * (2*n - 1)
        n += 1
        
def heptagonal():
    n = 1
    while True:
        yield n * (5*n - 3) / 2
        n += 1
        
def octagonal():
    n = 1
    while True:
        yield n * (3*n - 2)
        n += 1

class Cyclical:
    """ Class to determine if a number is triangular, square, pentagonal, hexagonal, heptagonal or octagonal.
        Contains generators and will generate necessary patterns of numbers to keep the minimum amount of data in memory"""
    #triangle numbers
    triangle_generator = triangle()
    max_triangle = 0
    triangles = set()
    #square numbers
    square_generator = square()
    max_square = 0
    squares = set()
    #pentagonal numbers
    pentagonal_generator = pentagonal()
    max_pentagonal = 0
    pentagonals = set()
    #hexagonal numbers
    hexagonal_generator = hexagonal()
    max_hexagonal = 0
    hexagonals = set()
    #heptagonal numbers    
    heptagonal_generator = heptagonal()
    max_heptagonal = 0
    heptagonals = set()
    #octagonal numbers
    octagonal_generator = octagonal()
    max_octagonal = 0
    octagonals = set()
    
    def is_triangular(self, n):
        while n > self.max_triangle:
            next_number = self.triangle_generator.next()
            self.triangles.add(next_number)
            self.max_triangle = next_number
                
        if n in self.triangles:
            return True
        else:
            return False
        
    def is_square(self, n):
        while n > self.max_square:
            next_number = self.square_generator.next()
            self.squares.add(next_number)
            self.max_square = next_number
                
        if n in self.squares:
            return True
        else:
            return False
        
    def is_pentagonal(self, n):
        while n > self.max_pentagonal:
            next_number = self.pentagonal_generator.next()
            self.pentagonals.add(next_number)
            self.max_pentagonal = next_number
                
        if n in self.pentagonals:
            return True
        else:
            return False
        
    def is_hexagonal(self, n):
        while n > self.max_hexagonal:
            next_number = self.hexagonal_generator.next()
            self.hexagonals.add(next_number)
            self.max_hexagonal = next_number
                
        if n in self.hexagonals:
            return True
        else:
            return False
        
    def is_heptagonal(self, n):
        while n > self.max_heptagonal:
            next_number = self.heptagonal_generator.next()
            self.heptagonals.add(next_number)
            self.max_heptagonal = next_number
                
        if n in self.heptagonals:
            return True
        else:
            return False
        
    def is_octagonal(self, n):
        while n > self.max_octagonal:
            next_number = self.octagonal_generator.next()
            self.octagonals.add(next_number)
            self.max_octagonal = next_number
                
        if n in self.octagonals:
            return True
        else:
            return False

# <codecell>

def find_factors(n):
    import math
    results = set()
    for i in xrange(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            results.add(n / i)
            results.add(i)
    return results

# <codecell>


