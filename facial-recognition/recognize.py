
import face_recognition
import numpy as np
from PIL import Image, ImageDraw

# Carregue uma foto que voce reconheca o rosto
known_image = face_recognition.load_image_file("toby.jpg")
enconding = face_recognition.face_encondings(kown_image)[0]

# Carregue uma foto que voce nao reconheca os rostos
unknown_image = face_recognition.load_image_file("office.jpg")

# Pegue todas as imagens na imagem desconhecida
face_locations = face_recognition.face_locations(unknown_image)
face_encondings = face_recognition.face_encondigs(unknown_image, face_locations)
