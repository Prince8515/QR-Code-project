import qrcode

url=input("Enter url want to convert :")
filename=input("Enter file name want to save qr :")
if not(filename.endswith(".png")):
    filename=filename+".png"
img=qrcode.make(url)
img.save(filename)