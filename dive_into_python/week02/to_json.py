import functools
import json


def to_json(func):
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)

    return wrapped


@to_json
def get_data():
    return {
        'data': 42
    }


def main():
    print(get_data.__name__)


if __name__ == '__main__':
    main()
