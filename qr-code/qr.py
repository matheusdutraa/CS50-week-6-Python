import os
import qrcode

img = qrcode.make("https://youtu.be/XCp_X6_1R4w")

img.save("qr.png", "PNG")

os.system("open qr.png")
