from pathlib import Path

def sol7():
    path = input("каталог: ")
    ext = input("расширение: ")
    folder = Path(path)
    if not folder.is_dir():
        print("каталог не существует")
        return
    for file in folder.rglob("*" + ext):
        if file.is_file():
            print(file, file.stat().st_size, "байтов")


sol7()
