import string
from math import log
from random import SystemRandom

class PwdGen(object):

	pwd = ''
	entropy = 0.0
	# print 'alphabet: ' + alphabet + 'and length of chars:' + str(len(alphabet))


	def __init__(self, length, strength):

		self.pwd = self.newPwd(length, strength)

	def  __repr__(self):
		return 'Your new password is:    ' + str(self.pwd) + '    it has ' + str(self.entropy) + 'bits of entrophy.' 

	def newPwd(self, length, strength):

		rand = SystemRandom()

		alphabet = string.digits

		if strength > 0:
			alphabet += string.ascii_uppercase[0:6]
			if strength > 1:
				alphabet += string.ascii_uppercase[6:26]
				if strength > 2:
					alphabet += string.ascii_lowercase
					if strength > 3:
						alphabet += string.punctuation


		self.entropy = self.entropyOfPwd(len(alphabet), length)

		return str().join(rand.choice(alphabet) for x in range(length))

	def entropyOfPwd(self,possibleChars,length):
		entropy = length * log(possibleChars, 2)
		return entropy

print
print '************************  PWD GEN  ************************'
print
print 'No funny business, I don\'t handle incorrect input!'
print

length = int(raw_input('How many characters long would you like your password to be? '))
strength = int(raw_input('Great! Now how strong of a password should I generate for you? (0 - 4, weaker -> stonger) '))

pwd = PwdGen(length,strength)
print pwd