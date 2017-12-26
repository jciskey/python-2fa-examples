import pyotp

secret_key = raw_input('Secret Key: ')

user_code = raw_input('TOTP Code: ')

totp = pyotp.totp.TOTP(secret_key)

if totp.verify(user_code):
	print 'Code matches'
else:
	print 'Code does not match'
