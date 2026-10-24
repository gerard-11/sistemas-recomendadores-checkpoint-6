# sistemas recomendadores checkpoint 6

notebook en español con tres modelos de recomendación de películas

- recomendador simple con media ponderada de imdb
- recomendador basado en contenido con tf idf y similitud coseno
- recomendador mejorado con actores director géneros palabras clave y equipo

## datos

descarga los archivos con este comando

```bash
python descargar_datos.py
```

el script guarda `movies_metadata.csv` `credits.csv` y `keywords.csv` en la
carpeta `data`

## instalacion

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

abre `recomendadores.ipynb` y ejecuta las celdas en orden
