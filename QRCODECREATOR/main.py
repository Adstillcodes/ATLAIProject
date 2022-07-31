import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image 
qr1 = input("link you want the QRcode to display eg:www.google.com : ")
qr2 = input("name of the image...please add a .jpg at the end of the name thnx!!: ")
qr = pyqrcode.create(qr1)
qr.png(qr2, scale=8)

#pip install PyQRCode
#pip install pyzbar
