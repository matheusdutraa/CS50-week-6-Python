from PIL import Image
import face_recognition

# Carrega o arquivo jpg em um numpy array
image = face_recognition.load_image_file("office.jpg")

# Encontra todos rotos na imagem usando o padrao HOG-based model.
# Esse metodo não é muito eficaz
face_locations = face_recognition.face_locations(image)

for face_location in face_locations:

    # Mostra a localização de cada rosto da imagem
    top, right, bottom, left = face_location

    # Voce pode acessar o propio rosto assim
    face_image = image[top:bottom, left:right]
    pill_image = Image.fromarray(face_image)
    pill_image.show()
