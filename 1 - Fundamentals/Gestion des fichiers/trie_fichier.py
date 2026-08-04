# Script pour trier le repertoire de Telechargement en fonction des extensions des fichiers

from pathlib import Path

dirs = {
    ".png" : "Images",
    ".jpg" : "Images",
    ".jpeg" : "Images",
    ".gif" : "Images",
    ".svg" : "Images",
    ".tiff" : "Images",
    ".doc" : "Documents",
    ".txt" : "Documents",
    ".pptx" : "Documents",
    ".ppt" : "Documents",
    ".xls" : "Documents",
    ".xlsx" : "Documents",
    ".docx" : "Documents",
    ".pdf": "Documents",
    ".mp3" : "Audio",
    ".wav" : "Audio",
    ".mov" : "Video",
    ".mp4" : "Video",
    ".zip" : "Archives",
    ".rar" : "Archives",
    ".zip" : "Archives",
    ".exe" : "Programmes",
    ".apk" : "Programmes"
 }

SOURCE_FILE = Path(__file__).resolve()  # resolve permet de résoudre les liens symboliques
dir_a_trier = Path.home() / "Documents"


files = [f for f in dir_a_trier.iterdir() if f.is_file()]
print(SOURCE_FILE)

for f in files:
    output_dir = dir_a_trier / dirs.get(f.suffix,"Autres")
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)

