import hashlib
import os

# Created by Jordan Leich or Rampage

def calculate_md5(filename):
    md5_hash = hashlib.md5()
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()

def normalize_path(path):
    return path.replace("\\", "/")

def scan_directory(directory):
    output = ""
    try:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                md5_hash_value = calculate_md5(file_path)
                normalized_file_path = normalize_path(file_path)
                normalized_relative_path = normalize_path(os.path.relpath(normalized_file_path, directory))
                output += f"'{normalized_relative_path}': '{md5_hash_value}',\n"
    except Exception as e:
        print("An error occurred during directory scanning:")
        print(e)
        return None
    return output

output_file_name = "Vanilla XML2 File Hashes.txt"

while True:
    directory_path = input("Enter the path of your vanilla XML2 directory: ")
    if os.path.exists(directory_path):
        break
    print("Invalid directory path. Please try again.")

output_dir = input("Enter the path of where you want the output results to go: ")
output_file_path = os.path.join(output_dir, output_file_name)

try:
    print("Scanning, please wait...")
    output_data = scan_directory(directory_path)

    if output_data is None:
        raise Exception("Directory scanning failed.")

    with open(output_file_path, "w") as output_file:
        output_file.write(output_data)

    print(f"Output written to '{output_file_path}'")
except Exception as e:
    print("An error occurred:")
    print(e)

input("Press enter to end.")