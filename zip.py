import os
import zipfile

SRC_FOLDER = "src"  # Project files directory
ZIP_NAME = "ex.zip"  # Name of the generated zip file
EXCLUDE_FILES = []


def zip():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        zip_filepath = os.path.join(current_dir, ZIP_NAME)

        with zipfile.ZipFile(zip_filepath, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for foldername, subfolders, filenames in os.walk(SRC_FOLDER):
                if "__pycache__" in foldername:
                    continue
                for filename in filenames:
                    if filename in EXCLUDE_FILES:
                        continue
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.relpath(filepath, SRC_FOLDER)
                    zipf.write(filepath, arcname)
        print(f"Successfully created '{ZIP_NAME}' in '{current_dir}' containing all files from '{SRC_FOLDER}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    zip()