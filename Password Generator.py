from string import digits, ascii_uppercase, ascii_lowercase, punctuation
from math import log
from random import SystemRandom as randy

class PwdGen(object):

	pwd = ''
	entropy = 0.0

	def __init__(self, length, strength):

		self.pwd = self.newPwd(length, strength)

	def  __repr__(self):
		return 'Your new password is:    ' + str(self.pwd) + '    it has ' + str(self.entropy) + ' bits of entrophy.' 

	def newPwd(self, length, strength):

		rand = randy()

		alphabet = digits

		if strength > 0:
			alphabet += ascii_uppercase[0:6]
			if strength > 1:
				alphabet += ascii_uppercase[6:26]
				if strength > 2:
					alphabet += ascii_lowercase
					if strength > 3:
						alphabet += punctuation


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

length = int(raw_input('How many characters long would you like your password to be? (int) '))
strength = int(raw_input('Great! Now how strong of a password should I generate for you? (int)(0 - 4, weaker -> stonger) '))

pwd = PwdGen(length,strength)
print pwd