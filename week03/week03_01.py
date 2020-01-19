import os.path


class FileReader:
    def __init__(self, path_to_file):
        self.path = path_to_file

    def read(self):
        try:
            with open(self.path, 'r') as fin:
                return fin.read()
        except FileNotFoundError:
            return ''


def main():
    pass


if __name__ == '__main__':
    main()
