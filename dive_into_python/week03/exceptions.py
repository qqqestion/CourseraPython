import json
import os.path
import traceback
import requests
import sys


def main():
    # catch all error
    """
    try:
        input()
    except: # catch all error
        print('Error')

    # can catch valueerror and keyboardinterrupt
    try:
        raw = input('enter number: ')
        number = int(raw)
        print(number)
    except ValueError:
        print('invalid value!')
    except KeyboardInterrupt:
        print('exit')

    # if error handling is the same with some errors
    try:
        raw = input('enter number: ')
        number = int(raw)
        print(number)
    except (ValueError, KeyboardInterrupt):
        print('error occurred')

    database = {
        'red': ['fox', 'flower'],
        'green': ['peace', 'M', 'Python']
    }
    try:
        color = input('enter the color: ')
        number = input('enter index: ')
        label = database[color][int(number)]
        print(f'you choose: {label}')
    # except(IndexError, KeyError): -> LookupError is the base class and
    # IndexError and KeyError are subclasses
    except LookupError:
        print('object not found')

    # block finally
    f = open('files/file.txt')
    try:
        for line in f:
            print(line.rstrip('\n'))
    except OSError:
        print('error')
    # it happens anyway
    finally:
        f.close()

    # access to exception obj
    try:
        with open('files/that_not_exist.txt') as f:
            content = f.read()
    except OSError as err:
        print(err.errno, err.strerror, sep='\n')

    # attribute args
    filename = 'files/that_not_exist.txt'
    try:
        if not os.path.exists(filename):
            raise ValueError('no such file:', filename)
    except ValueError as err:
        message, desired_filename = err.args[0], err.args[1]
        print(message, desired_filename)

    # access to traceback
    try:
        with open('files/that_not_exist.txt') as f:
            content = f.read()
    except OSError as err:
        trace = traceback.print_exc()
        print(trace)

    # raise error up
    try:
        raw = input('enter the number: ')
        if not raw.isdigit():
            raise ValueError('bad number', raw)
    except ValueError as err:
        print('invalid value: ', err)
        raise

    # exception through raise from Exception
    # ValueError call TypeError
    # ValueError
    # 'The above exception was the direct cause of the following exception:'
    # TypeError
    try:
        raw = input('enter the number: ')
        if not raw.isdigit():
            raise ValueError('bad number', raw)
    except ValueError as err:
        print('invalid value: ', err)
        raise TypeError('error') from err

    # it's bad to catch AssertationError with try/except
    try:
        assert False
    except:
        print('not do this!')
    """

    #
    url = sys.argv[1]
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.Timeout:
        print(f'TimeoutError: url "{url}"')
    except requests.HTTPError as err:
        print(f'URLError url "{url}": code {err.response.status_code}')
    except requests.RequestException:
        print(f'Downloading error url: {url}')
    else:
        print(response.content)


if __name__ == '__main__':
    main()
