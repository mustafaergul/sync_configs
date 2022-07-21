import yaml


class File:

    def __init__(self, file_name):
        self.file_name = file_name

    def fetch_file_name(self) -> list:
        with open(self.file_name, "r") as f_stream:
            files = []
            try:
                for key, value in yaml.safe_load(f_stream).items():
                    files.append(value)
            except yaml.YAMLError as exc:
                print(exc)
        return [f for fs in files for f in fs]
