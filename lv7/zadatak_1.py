import matplotlib.pyplot as plt
import numpy as np
from scipy.cluster.hierarchy import dendrogram
from sklearn.datasets import make_blobs, make_circles, make_moons
from sklearn.cluster import KMeans, AgglomerativeClustering

from sklearn.cluster import KMeans

def generate_data(n_samples, flagc):
    # 3 grupe
    if flagc == 1:
        random_state = 365
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
    
    # 3 grupe
    elif flagc == 2:
        random_state = 148
        X,y = make_blobs(n_samples=n_samples, random_state=random_state)
        transformation = [[0.60834549, -0.63667341], [-0.40887718, 0.85253229]]
        X = np.dot(X, transformation)

    # 4 grupe 
    elif flagc == 3:
        random_state = 148
        X, y = make_blobs(n_samples=n_samples,
                        centers = 4,
                        cluster_std=np.array([1.0, 2.5, 0.5, 3.0]),
                        random_state=random_state)
    # 2 grupe
    elif flagc == 4:
        X, y = make_circles(n_samples=n_samples, factor=.5, noise=.05)
    
    # 2 grupe  
    elif flagc == 5:
        X, y = make_moons(n_samples=n_samples, noise=.05)
    
    else:
        X = []
        
    return X

# generiranje podatkovnih primjera
X = generate_data(500, 1)

#KMeans
km = KMeans(n_clusters=3, init='random',
            n_init=5, random_state=0)

km.fit(X)

labels = km.predict(X)

mapping = {0: "red", 1: "green", 2: "blue"}
colors = [mapping[l] for l in labels]

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1], c=colors)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')

centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='purple', marker='X')

plt.show()



plt.figure()
plt.title("Ovisnost J")
val = []
for i in range(1, 10):
    km = KMeans(n_clusters=i, init='random',
            n_init=5, random_state=0)
    
    km.fit(X)

    val.append(km.inertia_)

plt.plot(val)
plt.show()



km = KMeans(n_clusters=5, init='random',
            n_init=5, random_state=0)

km.fit(X)

labels = km.predict(X)

mapping = {0: "red", 1: "green", 2: "blue", 3: "black", 4: "grey"}
colors = [mapping[l] for l in labels]

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1], c=colors)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')

centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='purple', marker='X')

plt.show()

# generiranje podatkovnih primjera
X = generate_data(500, 2)

#KMeans
km = KMeans(n_clusters=3, init='random',
            n_init=5, random_state=0)

km.fit(X)

labels = km.predict(X)

mapping = {0: "red", 1: "green", 2: "blue"}
colors = [mapping[l] for l in labels]

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1], c=colors)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')

centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='purple', marker='X')

plt.show()

# generiranje podatkovnih primjera
X = generate_data(500, 3)

#KMeans
km = KMeans(n_clusters=3, init='random',
            n_init=5, random_state=0)

km.fit(X)

labels = km.predict(X)

mapping = {0: "red", 1: "green", 2: "blue"}
colors = [mapping[l] for l in labels]

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1], c=colors)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')

centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='purple', marker='X')

plt.show()

# generiranje podatkovnih primjera
X = generate_data(500, 4)

#KMeans
km = KMeans(n_clusters=2, init='random',
            n_init=5, random_state=0)

km.fit(X)

labels = km.predict(X)

mapping = {0: "red", 1: "green", 2: "blue"}
colors = [mapping[l] for l in labels]

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1], c=colors)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')

centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='purple', marker='X')

plt.show()

# generiranje podatkovnih primjera
X = generate_data(500, 5)

#KMeans
km = KMeans(n_clusters=2, init='random',
            n_init=5, random_state=0)

km.fit(X)

labels = km.predict(X)

mapping = {0: "red", 1: "green", 2: "blue"}
colors = [mapping[l] for l in labels]

# prikazi primjere u obliku dijagrama rasprsenja
plt.figure()
plt.scatter(X[:,0],X[:,1], c=colors)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')

centers = km.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='purple', marker='X')

plt.show()