from bs4 import BeautifulSoup
import re
import os


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start
    return files


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = []
    # TODO Добавить нужные страницы в bridge
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]
    bridge = ['Stone_Age', 'Brain', 'Artificial_intelligence', 'Python_(programming_language)']
    # bridge = ['Stone_Age']

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id='bodyContent')

        # TODO посчитать реальные значения
        imgs = len([
            img for img in body.find_all('img') 
            if int(img.get('width', 0)) >= 200
        ])

        # headers = len([
        #     header for header in re.findall(r'<h[123456].+>[ETC]', str(body))
        # ])
        headers = 0
        reg = re.compile('[TCE]')
        for header_type in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            for header in [header for header in body.find_all(header_type)]:
                headers  += 1 if reg.match(header.text) else 0
                
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        linkslen = 0
        max_cnt = 0
        reg = re.compile(r'<a.*?>.*?</a>')
        for ref in soup.body.find_all('a'):
            parent_contents = ref.parent.contents
            current_max = 0
            is_first = True
            for tag in parent_contents:
                if reg.match(str(tag)):
                    current_max += 1
                else:
                    max_cnt = max(current_max, max_cnt)
                    current_max = 0
        linkslen = max_cnt

        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]
        print(f'Images = {imgs}, Headers = {headers}, Linkslen = {linkslen}, Lists = {lists}')

    return out

def find_all_href(start, path):
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # print(dir_path)
    path = os.path.join(path, start)
    reg = re.compile(r'^/wiki/[\w()]+', re.IGNORECASE)
    links = set()
    with open(path, 'r') as fin:
        soup = BeautifulSoup(fin.read(), 'lxml')
        for link in [a.get('href') for a in soup.find_all(name='a')]:
            if reg.match(link or '') and os.path.exists('.' + link):
                print(link)
                links.add(link)
    return links



if __name__ == '__main__':
    result = parse('Stone_Age', 'Python_', './wiki/')