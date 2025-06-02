import qrcode

url = "http://172.16.1.158:5000"  # Replace with your IP if different
img = qrcode.make(url)
img.save("photo_gallery_qr.png")
print("✅ QR Code generated: photo_gallery_qr.png")
