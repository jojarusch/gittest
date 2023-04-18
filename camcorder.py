import cv2

# Webcam-Stream öffnen
cap = cv2.VideoCapture(0)

# Überprüfen, ob die Webcam erfolgreich geöffnet wurde
if not cap.isOpened():
    print("Fehler: Webcam konnte nicht geöffnet werden!")
    exit()

# Webcam-Parameter festlegen
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Bild von der Webcam aufnehmen
ret, frame = cap.read()

if ret:
    # Bild in Graustufen umwandeln
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Bild als JPG speichern
    cv2.imwrite("webcam_image.jpg", gray_frame)

    print("Bild erfolgreich als webcam_image.jpg gespeichert!")

# Webcam-Stream und Fenster schließen
cap.release()
cv2.destroyAllWindows()