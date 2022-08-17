import sys
from pathlib import Path
import asyncio

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
MP3_AUDIO = []
OGG_AUDIO = []
WAV_AUDIO = []
AMR_AUDIO = []
AVI_VIDEO = []
MP4_VIDEO = []
MOV_VIDEO = []
MKV_VIDEO = []
DOC_FILES = []
DOCX_FILES = []
TXT_FILES = []
PDF_FILES = []
XLSX_FILES = []
PPT_FILES = []
PPTX_FILES = []
SOME = []
ARCHIVES = []

REGISTER_EXTENSIONS = {
    'JPEG': JPEG_IMAGES,
    'PNG': PNG_IMAGES,
    'JPG': JPG_IMAGES,
    'SVG': SVG_IMAGES,
    'MP3': MP3_AUDIO,
    'OGG': OGG_AUDIO,
    'WAV': WAV_AUDIO,
    'AMR': AMR_AUDIO,
    'AVI': AVI_VIDEO,
    'MP4': MP4_VIDEO,
    'MOV': MOV_VIDEO,
    'MKV': MKV_VIDEO,
    'DOC': DOC_FILES,
    'DOCX': DOCX_FILES,
    'TXT': TXT_FILES,
    'PDF': PDF_FILES,
    'XLSX': XLSX_FILES,
    'PPT': PPT_FILES,
    'PPTX': PPTX_FILES,
    'ZIP': ARCHIVES,
    'GZ': ARCHIVES,
    'TAR': ARCHIVES
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extention(filename: str) -> str:
    # Превращаем расширение файла в название фала
    return Path(filename).suffix[1:].upper()


async def scan(folder: Path) -> None:
    for item in folder.iterdir():
        # Усли єто папка то добавляем ее в список Фолдерс
        if item.is_dir():
            # проверяем чтобі папка не біла той в которую мі скидіваем уже файлі
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'some'):
                FOLDERS.append(item)
                #  сканируем эту вложенную папку - рекурсия
                await scan(item)
            # Перейти к след елементу
            continue

        # Работа с файлом
        ext = get_extention(item.name)  # взять расширение
        fullname = folder / item.name  # взять полній путь файла
        if not ext:  # если у файла нет расширения добавить к неизвестнім
            SOME.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]  # взять список куда положить полній путь к файлу
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                # Если мы не регистрировали расширение в REGISTER_EXTENSIONS то добавить в Other
                UNKNOWN.add(ext)
                SOME.append(fullname)


if __name__ == '__main__':
    folder_for_scan = sys.argv[1]
    print(f'Start in folder {folder_for_scan}')

    scan(Path(folder_for_scan))
    print(f'Images jpeg: {JPEG_IMAGES}')
    print(f'Images jpg: {JPG_IMAGES}')
    print(f'Images svg: {SVG_IMAGES}')
    print(f'Audio mp3: {MP3_AUDIO}')
    print(f'Archives: {ARCHIVES}')

    print(f'Types of files in folder: {EXTENSIONS}')
    print(f'Unknown files of types: {UNKNOWN}')

    print(FOLDERS[::-1])
