import pyotp
import qrcode

# Generate the secret key that will be used
secret_key = pyotp.random_base32()
print 'Secret key: {}'.format(secret_key)

# Generate an OTP provisioning URI for importing into FreeOTP (or another authenticator)
user_name = 'fake@null.net'
issuer_name = 'ACME Corp'

provisioning_uri = pyotp.totp.TOTP(secret_key).provisioning_uri(user_name, issuer_name=issuer_name)

# Generate, save, and display a QR Code for import into an authenticator app
qr_img_path = 'test-qr.png'
print 'QR code saved to file: {}'.format(qr_img_path)
img = qrcode.make(provisioning_uri)

img.save(qr_img_path)

img.show()

