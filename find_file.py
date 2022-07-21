import os
from file import File
from directory import Directory


def find_file(names, paths) -> str:
    result = []
    for dirpath, dirname, filename in os.walk(paths):
        for name in names:
            if name in filename:
                result.append(os.path.join(dirpath, name))
    print(result[:2])


dir = Directory("directories.yml")
file = File("filenames.yml")

# Running syncing the config files
find_file(file.fetch_file_name(), dir.fetch_dir())
