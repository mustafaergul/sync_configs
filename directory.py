import yaml


class Directory:
    def __init__(self, dir_name):
        self.dir_name = dir_name

    def fetch_dir(self) -> str:
        with open(self.dir_name, "r") as d_stream:
            dirs = []
            try:
                for key, value in yaml.safe_load(d_stream).items():
                    dirs.append(value)
            except yaml.YAMLError as exc:
                print(exc)
        return ' '.join([d for ds in dirs for d in ds])
