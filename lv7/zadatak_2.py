import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans
import math

# ucitaj sliku
img = Image.imread("imgs\\test_1.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

km = KMeans(n_clusters=3, init='random',
            n_init=5, random_state=0)

km.fit(img_array)

labels = km.predict(img_array)
centroids = km.cluster_centers_

diff = img_array[:, None, :] - centroids[None, :, :]

dist = np.sum(diff**2, axis=2)

nearest = np.argmin(dist, axis=1)

img_array_aprox = centroids[nearest]

img_aprox = img_array_aprox.reshape(img.shape)

plt.figure()
plt.title("Rezultantna slika")
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()




img_array_aprox = img_array.copy()

km = KMeans(n_clusters=5, init='random',
            n_init=5, random_state=0)

km.fit(img_array)

labels = km.predict(img_array)
centroids = km.cluster_centers_

diff = img_array[:, None, :] - centroids[None, :, :]

dist = np.sum(diff**2, axis=2)

nearest = np.argmin(dist, axis=1)

img_array_aprox = centroids[nearest]

img_aprox = img_array_aprox.reshape(img.shape)

plt.figure()
plt.title("Rezultantna slika")
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()





img_array_aprox = img_array.copy()

km = KMeans(n_clusters=7, init='random',
            n_init=5, random_state=0)

km.fit(img_array)

labels = km.predict(img_array)
centroids = km.cluster_centers_

diff = img_array[:, None, :] - centroids[None, :, :]

dist = np.sum(diff**2, axis=2)

nearest = np.argmin(dist, axis=1)

img_array_aprox = centroids[nearest]

img_aprox = img_array_aprox.reshape(img.shape)

plt.figure()
plt.title("Rezultantna slika")
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()



# ucitaj sliku
img = Image.imread("imgs\\test_6.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

img_array_aprox = img_array.copy()

km = KMeans(n_clusters=3, init='random',
            n_init=5, random_state=0)

km.fit(img_array)

labels = km.predict(img_array)
centroids = km.cluster_centers_

diff = img_array[:, None, :] - centroids[None, :, :]

dist = np.sum(diff**2, axis=2)

nearest = np.argmin(dist, axis=1)

img_array_aprox = centroids[nearest]

img_aprox = img_array_aprox.reshape(img.shape)

plt.figure()
plt.title("Rezultantna slika")
plt.imshow(img_aprox)
plt.tight_layout()
plt.show()


plt.figure()
plt.title("Ovisnost J")
val = []
for i in range(1, 10):
    km = KMeans(n_clusters=i, init='random',
            n_init=5, random_state=0)
    
    km.fit(img_array)

    val.append(km.inertia_)

plt.plot(val)
plt.show()


# ucitaj sliku
img = Image.imread("imgs\\test_5.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

img_array_aprox = img_array.copy()

km = KMeans(n_clusters=5, init='random',
            n_init=5, random_state=0)

km.fit(img_array)

labels = km.predict(img_array)
centroids = km.cluster_centers_

diff = img_array[:, None, :] - centroids[None, :, :]

dist = np.sum(diff**2, axis=2)

nearest = np.argmin(dist, axis=1)

img_array_aprox = centroids[nearest]

img_aprox = img_array_aprox.reshape(img.shape)

H, W, C = img.shape
img_aprox = img_array_aprox.reshape((H, W, C))
nearest = nearest.reshape((H, W))

centroid_images = []
for k in range(centroids.shape[0]):
    mask = (nearest == k)
    img_k = np.zeros_like(img_aprox)
    img_k[mask] = centroids[k]
    centroid_images.append(img_k)
    plt.figure()
    plt.title(f'Centroid {k}')
    plt.imshow(img_k)
    plt.axis('off')
plt.show()