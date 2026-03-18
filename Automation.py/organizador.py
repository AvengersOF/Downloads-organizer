import os
import shutil

# encontra automaticamente a pasta Downloads
pasta_downloads = os.path.join(os.path.expanduser("~"), "Downloads")

# tipos de arquivos
tipos = {
    "PDF": [".pdf"],
    "Imagens": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Zip": [".zip", ".rar"],
    "Programas": [".exe", ".msi"]
}

for arquivo in os.listdir(pasta_downloads):

    caminho_arquivo = os.path.join(pasta_downloads, arquivo)

    # verifica se é arquivo (não pasta)
    if os.path.isfile(caminho_arquivo):

        extensao = os.path.splitext(arquivo)[1].lower()

        movido = False

        for pasta, extensoes in tipos.items():

            if extensao in extensoes:

                pasta_destino = os.path.join(pasta_downloads, pasta)

                os.makedirs(pasta_destino, exist_ok=True)

                destino = os.path.join(pasta_destino, arquivo)

                shutil.move(caminho_arquivo, destino)

                print(f"Movido: {arquivo} → {pasta}")

                movido = True
                break

        if not movido:

            pasta_outros = os.path.join(pasta_downloads, "Outros")

            os.makedirs(pasta_outros, exist_ok=True)

            destino = os.path.join(pasta_outros, arquivo)

            shutil.move(caminho_arquivo, destino)

            print(f"Movido: {arquivo} → Outros")