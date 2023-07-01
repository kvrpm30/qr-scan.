import qrcode 
import image


qr = qrcode.QRCode(
    version = 15, 
    box_size = 10, 
    border = 5 
)

data = "https://github.com/kvrpm30"

qr.add_data(data)
qr.make(fit =True)
img = qr.make_image(fill_color = "black", back_color = "white")
img.save("qrcode.png")






