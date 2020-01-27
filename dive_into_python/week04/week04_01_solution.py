import os
import uuid
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        self.current_position = 0

        if not os.path.exists(self.path):
            open(self.path, 'w').close()

    def write(self, content):
        with open(self.path, 'w') as f:
            return f.write(content)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __add__(self, obj):
        new_path = os.path.join(
            os.path.dirname(self.path),
            str(uuid.uuid4().hex)
        )
        new_file = type(self)(new_path)
        new_file.write(self.read() + obj.read())

        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path, 'r') as f:
            f.seek(self.current_position)

            line = f.readline()
            if not line:
                self.current_position = 0
                raise StopIteration('EOF')

            self.current_position = f.tell()
            return line


def example_test():
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
