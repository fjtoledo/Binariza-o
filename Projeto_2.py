import cv2
import matplotlib.pyplot as plt

imagem_colorida = cv2.imread(r"C:\Users\ferna\OneDrive\Pictures\Warhammer-40.000-Space-Marine-2.jpg")

imagem_rgb = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2RGB)
imagem_cinza = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

_, imagem_binarizada = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(imagem_rgb)
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(imagem_cinza, cmap="gray")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(imagem_binarizada, cmap="gray")
plt.axis("off")

plt.tight_layout()
plt.show()