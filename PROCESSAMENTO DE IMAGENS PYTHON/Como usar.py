from imageutils import convert_to_bw, resize_image, blur_image

# Converter imagem para preto e branco
convert_to_bw("entrada.jpg", "saida_pb.jpg")

# Redimensionar imagem para 200x200
resize_image("entrada.jpg", "saida_200x200.jpg", size=(200, 200))

# Aplicar blur com raio 5
blur_image("entrada.jpg", "saida_blur.jpg", radius=5)
