from pathlib import Path

folder_path = Path("Code_Testing")

for file_path in folder_path.iterdir():
    if file_path.is_file():
        if "CRITICAL" in file_path.read_text():
            new_name = folder_path / f"URGENT_{file_path.name}"
            file_path.rename(new_name)
            print(f"Successfully changed {file_path.name} name!")



