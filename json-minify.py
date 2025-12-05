import os
import json

def minify_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, separators=(',', ':'))

def find_and_minify_json_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json') or file.endswith('.ahap') or file.endswith('.geojson') or file.endswith('.lottie'):
                file_path = os.path.join(root, file)
                try:
                    minify_json_file(file_path)
                    print(f'Minified: {file_path}')
                except Exception as e:
                    print(f'Failed to minify {file_path}: {e}')

if __name__ == '__main__':
    # Set the directory to your Xcode build products directory
    build_directory = os.environ.get('TARGET_BUILD_DIR', '.')
    find_and_minify_json_files(build_directory)
