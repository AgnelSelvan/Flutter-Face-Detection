import cv2

# Loads the Face Detection Data from XML using Haarcascade Classifier
faceCascade = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

# Gives the coordinate of the Face in image
def giveFacesCoordinates(imagePath):
    # Loads the Image to a variable
    image = cv2.imread(str(imagePath))
    # Convert the Color Image to Black & White Image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detects the list of faces from Image and storing the face cordinates in a variable
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    print("Faces: " + str(faces))
    if faces == ():
        return []
    print(type(faces))
    return faces.tolist()


# Detects the face
def showFace():
    image = cv2.imread("./sample.jpeg")
    for (x, y, w, h) in giveFacesCoordinates("./sample.jpeg"):
        # Draws the rectangle on the image over face
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # Displays the Output Image
    cv2.imshow("Faces found", image)
    cv2.waitKey(0)
