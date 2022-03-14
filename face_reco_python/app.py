# Imports
import json
import werkzeug
from flask import Flask, request, jsonify

# Importing only giveFacesCoordinates from main.py
from main import giveFacesCoordinates

# Flask
app = Flask(__name__)

# Routes for API

# /face_detection POST Route detects the face using giveFacesCoordinates function in main.py and returns the list of faces coordinate
# in the body of the request we need to pass the image.
@app.route("/face_detection", methods=["POST"])
def index():
    # Image
    imagefile = request.files["image"]
    # Getting file name of the image using werkzeug library
    filename = werkzeug.utils.secure_filename(imagefile.filename)
    print("\nReceived image File name : " + imagefile.filename)
    # Saving the image in images Directory
    imagefile.save("images/" + filename)
    # Passing the imagePath in this giveFacesCoordinates function and getting the list of faces coordinate
    faces = giveFacesCoordinates("./images/" + filename)
    # Returns faces Cordinate in the json Format
    return json.dumps({"faces": faces})


# Running the app
app.run()
