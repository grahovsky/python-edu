import requests
import pprint

def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls):
        yield len(resp.content), resp.status_code, resp.url


urls = ('https://ya.ru', 'https://google.com', 'https://vk.com')

for resp_len, status, url, in gen_from_urls(urls):
    print(resp_len, '->', status, '->', url)

urls_res = {url: size for size, _, url in gen_from_urls(urls)}
pprint.pprint(urls_res)
