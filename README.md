PwdGen
======

Lightweight password generator capable of generating passwords of a user specified length and entropy. Entropy options are 3.32, 4.0, 5.17, 5.95 or 6.55 bits per character and can be specified by passing (0 - 4) to the generators strength parameter.


This project utilizes SystemRandom() from Python's random library as its cryptographically secure pseudo-random number generator. More information on this class method can be found here:

http://docs.python.org/2/library/random.html#random.SystemRandom