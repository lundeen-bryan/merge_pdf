import os
from pypdf import PdfWriter

def merge_pdfs(file_string):
    files = []
    files = windows_to_unix(file_string)
    save_path = os.environ['ONEDRIVE']
    save_path = save_path + "\\Documents\\merged.pdf"
    merger = PdfWriter()
    for file in files:
        with open(file, 'rb') as f:
            merger.append(f)
    with open(save_path, 'wb') as f:
        merger.write(f)
        merger.close()

def windows_to_unix(filepath):
    file_list = []
    filepath = filepath.replace('\'', '')
    filepath = filepath.replace('\"', '')
    filepath = filepath.strip().strip('\'"')
    file_list = list(filepath.split("|"))
    return file_list
