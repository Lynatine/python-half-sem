from pathlib import Path

def sol6(path):
    folder = Path(path)
    files = [p for p in folder.rglob("*") if p.is_file()]
    dirs = [p for p in folder.rglob("*") if p.is_dir()]
    pyfiles = [p for p in files if p.suffix == ".py"]
    size = 0
    for file in files:
        size += file.stat().st_size
    print("колчисество файлов:", len(files))
    print("всегл папок:", len(dirs))
    print("питоновских файлов:")
    for file in pyfiles:
        print(file)
    print("общий размер:", size)


sol6("project")
