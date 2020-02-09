import yaml

yaml_my_class = """
- !MyClass 
    variable: 2
    enemy: 3
- enemy: ['rat']
"""


class MyClass(yaml.YAMLObject):
    yaml_tag = '!MyClass'

    def __init__(self, data):
        self.variable = data['variable']
        self.enemy = data['enemy']

    @staticmethod
    def from_yaml(loader, node):
        data = loader.construct_mapping(node)

        return MyClass(data)

    def __str__(self):
        return f'MyClass = "{self.variable}" and "{self.enemy}"'

    def __repr__(self):
        return str(self)


if __name__ == '__main__':
    yaml.add_representer(MyClass, MyClass.from_yaml)
    yaml_data = yaml.load(yaml_my_class)
    print(yaml_data)
