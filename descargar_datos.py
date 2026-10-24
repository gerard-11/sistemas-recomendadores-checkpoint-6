from pathlib import Path
from urllib.request import urlretrieve


CARPETA_DATOS = Path('data')
BASE_URL = 'https://huggingface.co/datasets/gaygaaa/TheMoviesDataset/resolve/main/'
ARCHIVOS = ['movies_metadata.csv', 'credits.csv', 'keywords.csv']


def descargar_datos():
    CARPETA_DATOS.mkdir(exist_ok=True)

    for archivo in ARCHIVOS:
        destino = CARPETA_DATOS / archivo
        if destino.exists():
            print(f'{archivo} ya existe')
            continue

        print(f'descargando {archivo}...')
        urlretrieve(BASE_URL + archivo, destino)
        print(f'{archivo} guardado en {destino}')


if __name__ == '__main__':
    descargar_datos()
