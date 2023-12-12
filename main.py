import matplotlib.pyplot as plt
import cv2
from sklearn.cluster import KMeans

image = plt.imread("imagens/sable.png")
image = cv2.cvtColor((image*255).astype('uint8'), cv2.COLOR_RGBA2RGB)
X = image.reshape(-1, 3)
print(X.shape)

kmeans = KMeans(n_clusters=5, n_init=10)
kmeans.fit(X)

segmented_img = kmeans.cluster_centers_[kmeans.labels_]
segmented_img = segmented_img.reshape(image.shape)

cv2.imwrite("geradas/sabletest.png", cv2.cvtColor(segmented_img.astype("uint8"), cv2.COLOR_BGR2RGB))