import os
import zipfile

SRC_FOLDER = "src" # Project files directory
ZIP_NAME = "ex.zip" # Name of the generated zip file

def zip():
    try:
        with zipfile.ZipFile(ZIP_NAME, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for foldername, subfolders, filenames in os.walk(SRC_FOLDER):
                for filename in filenames:
                    filepath = os.path.join(foldername, filename)
                    arcname = os.path.relpath(filepath, SRC_FOLDER)
                    zipf.write(filepath, arcname)
        print(f"Successfully created '{ZIP_NAME}' containing all files from '{SRC_FOLDER}'.")
    except Exception as e:
        print(f"Error: {e}")
    

if __name__ == "__main__":
    zip()