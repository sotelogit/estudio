import qrcode

dato = "https://github.com/sotelogit"
qr = qrcode.make(dato)
qr.save("qr.png")
