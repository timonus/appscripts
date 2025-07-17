import os
import subprocess
import shutil

# https://chatgpt.com/share/7b04edb2-e0ab-4214-80f6-b25d2cadc123

def convert_to_binary_plist(file_path):
    binary_file_path = f"{file_path}.binary"
    try:
        # Convert plist to binary format and save as a temporary binary file
        subprocess.run(['plutil', '-convert', 'binary1', file_path, '-o', binary_file_path], check=True)
        return binary_file_path
    except subprocess.CalledProcessError as e:
        print(f"Failed to convert {file_path} to binary: {e}")
        return None

def keep_smaller_file(original_file, binary_file):
    original_size = os.path.getsize(original_file)
    binary_size = os.path.getsize(binary_file)

    if binary_size < original_size:
        # Replace the original file with the binary version
        shutil.move(binary_file, original_file)
        savings = original_size - binary_size
        print(f"Kept binary version (smaller): {original_file}, saved {savings}")
        return savings
    else:
        # Remove the binary version and keep the original
        os.remove(binary_file)
        print(f"Kept original version (smaller): {original_file}")
        return 0

def find_and_convert_plist_files(directory):
    overall_savings = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.plist') or file.endswith('.intentdefinition') or file.endswith('.xcprivacy') or file.endswith('.strings') or file == 'CodeResources':
                file_path = os.path.join(root, file)
                binary_file_path = convert_to_binary_plist(file_path)
                if binary_file_path:
                    overall_savings += keep_smaller_file(file_path, binary_file_path)
    print(f"Overall saved: {overall_savings}")


if __name__ == '__main__':
    # Set the directory to your Xcode build products directory
    build_directory = os.environ.get('TARGET_BUILD_DIR', '.')
    find_and_convert_plist_files(build_directory)