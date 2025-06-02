from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def gallery():
    # Define photos with captions and ads
    photos_info = [
        {"filename": "img1.jpg", "caption": "Beautiful Pair", "ad": "The girl behind me at any situations!"},
        {"filename": "img2.jpg", "caption": "Marriage Moments", "ad": "The girl with Golden Heart."},
        # add more photos with info
    ]
    
    # Generate URLs for images
    for photo in photos_info:
        photo['url'] = url_for('static', filename=f'photos/{photo["filename"]}')
        
    return render_template('gallery.html', photos=photos_info)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
