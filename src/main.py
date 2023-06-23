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

def clear():
  os.system("cls")

def main():
    clear()
    print("Drag each file that you want to merge and separage each file name with a vertical bar which looks like this \"|\".")
    print("To quit without merging pdf files, hold down ctrl and press the letter \"C\"")
    files = input("> ").strip()
    merge_pdfs(files)


if __name__ == "__main__":
    main()
