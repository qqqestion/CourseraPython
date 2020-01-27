import os.path
import tempfile


class File:
    file_count = 0

    def __init__(self, path_to_file):
        if not os.path.exists(path_to_file):
            with open(path_to_file, 'w'):
                pass
        self.filename_path = path_to_file
        self.file_count += 1

    def read(self):
        with open(self.filename_path, 'r') as file:
            return file.read()

    def write(self, line):
        with open(self.filename_path, 'w') as file:
            file.write(line)
        return len(line)

    def __add__(self, other):
        new_file = File(
            os.path.join(
                tempfile.gettempdir(),
                'python_week04_01_inst_' + str(self.file_count))
        )
        with open(str(new_file), 'w') as fout:
            for line in self:
                fout.write(line)
            for line in other:
                fout.write(line)
        return new_file

    def __str__(self):
        return os.path.abspath(self.filename_path)

    def __iter__(self):
        self.open_file = open(self.filename_path, 'r')
        self.count = 0
        return self

    def __next__(self):
        line = self.open_file.readline()
        if line != '':
            return line
        else:
            self.open_file.close()
            raise StopIteration


def example_test():
    print(tempfile.gettempdir())
    path = 'files/some_file_new'
    file = File(path)
    print(file.read())
    file1 = File(path + '_1')
    file2 = File(path + '_2')
    file1.write('line 1\n')
    file2.write('line 2\n')
    new_file = file1 + file2
    for line in new_file:
        print(ascii(line))

    os.remove(str(file))
    os.remove(str(file1))
    os.remove(str(file2))
    os.remove(str(new_file))


def main():
    example_test()


if __name__ == '__main__':
    main()
