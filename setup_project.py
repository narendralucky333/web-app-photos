import os

# Step 1: Create folders
os.makedirs("static/photos", exist_ok=True)
os.makedirs("templates", exist_ok=True)

# Step 2: Create server.py
with open("server.py", "w") as f:
    f.write("""from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def gallery():
    photos = os.listdir('static/photos')
    photos = [url_for('static', filename=f'photos/{photo}') for photo in photos]
    return render_template('gallery.html', photos=photos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
""")

# Step 3: Create HTML template
with open("templates/gallery.html", "w") as f:
    f.write("""<!DOCTYPE html>
<html>
<head>
    <title>My Photo Gallery</title>
    <style>
        body { font-family: sans-serif; text-align: center; }
        img { height: 200px; margin: 10px; border-radius: 10px; }
    </style>
</head>
<body>
    <h1>📷 My Photo Gallery</h1>
    {% for photo in photos %}
        <img src="{{ photo }}" alt="photo">
    {% endfor %}
</body>
</html>
""")

# Step 4: Create generate_qr.py
with open("generate_qr.py", "w") as f:
    f.write("""import qrcode

url = "http://172.16.1.158:5000"  # Replace with your actual IP if needed
img = qrcode.make(url)
img.save("photo_gallery_qr.png")
print("✅ QR Code generated: photo_gallery_qr.png")
""")

print("✅ Project setup completed. Now add your photos to 'static/photos' folder.")
