import qrcode
import qrcode.constants

qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data("https://yasith-rashan-website.vercel.app/")

img=qr.make_image()
img.save("qrcode.jpg")
