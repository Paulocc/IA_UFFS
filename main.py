import matplotlib.pyplot as plt
import pandas as pd
import cv2, os, glob
from sklearn.cluster import KMeans

def get_image_size(image):
    return os.path.getsize(image) / 1024  #Tamanho em KB

def get_unique_colors(image):
    unique_colors = len(set(tuple(pixel) for row in image for pixel in row))
    return unique_colors

#diretórios utilizados nas funções
input_directory = "images/"
output_directory = "generated/"
info_directory = "info/"

#Lista de arquivos de imagem no diretório de entrada
image_files = glob.glob(os.path.join(input_directory, "*.png"))

#valores do cluster
#n_clusters_values = [2, 3, 4, 5, 6, 7, 8]
n_clusters_values = [2,3,5]

data = []

for n_clusters in n_clusters_values:
    for image_file in image_files:

        original_image = plt.imread(image_file)
        original_image = cv2.cvtColor((original_image * 255).astype('uint8'), cv2.COLOR_RGBA2RGB)

        X = original_image.reshape(-1, 3)
        print(X.shape)

        kmeans = KMeans(n_clusters=n_clusters, n_init=10)
        kmeans.fit(X)

        #Reconstrução da Imagem Segmentada
        segmented_img = kmeans.cluster_centers_[kmeans.labels_]
        segmented_img = segmented_img.reshape(original_image.shape)

        # Salvar a Imagem Segmentada
        output_file = os.path.join(output_directory, f"{os.path.basename(image_file).replace('.png', '')}_n{n_clusters}_CLUSTERS.png")
        cv2.imwrite(output_file, cv2.cvtColor(segmented_img.astype("uint8"), cv2.COLOR_BGR2RGB))

        #Obtendo as informações da imagem original
        original_resolution = original_image.shape[:2]
        original_size_kb = get_image_size(image_file)
        original_unique_colors = get_unique_colors(original_image)

        #Obtendo as informações aa imagem gerada
        generated_size_kb = get_image_size(output_file)
        generated_unique_colors = get_unique_colors(segmented_img)

        #salvando as informações em uma lista
        data.append({
            "Imagem": os.path.basename(image_file),
            "n_clusters": n_clusters,
            "Resolucao_original": f"{original_resolution[0]} x {original_resolution[1]}",
            "Tamanho_KB_original": original_size_kb,
            "Cores_unicas_original": original_unique_colors,
            "Tamanho_KB_gerada": generated_size_kb,
            "Cores_unicas_gerada": generated_unique_colors
        })

        #Salvando as informações em um .txt
        output_info_file = os.path.join(info_directory, f"info_{os.path.basename(image_file).replace('.png', '')}_n{n_clusters}_CLUSTERS.txt")
        with open(output_info_file, "w") as f:
            f.write(f"Resolucao: {original_resolution[0]} x {original_resolution[1]}\n")
            f.write(f"Tamanho em KB (Original): {original_size_kb:.2f} KB\n")
            f.write(f"Cores unicas (Original): {original_unique_colors}\n")
            f.write(f"Tamanho em KB (Gerada): {generated_size_kb:.2f} KB\n")
            f.write(f"Cores unicas (Gerada): {generated_unique_colors}\n")

#Criando DataFrame do pandas e organizando pelo nome dos arquivos
df = pd.DataFrame(data)
df = df.sort_values(by=['Imagem', 'n_clusters'])

#salvando em uma planilha
df.to_csv("Informacoes_imagens.csv", index=False)