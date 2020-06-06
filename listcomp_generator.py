import requests

urls = ('https://ya.ru', 'https://google.com', 'https://vk.com')

# listcomp waits for all of its data
for resp in [requests.get(url) for url in urls]:
    print(len(resp.content), '->', resp.status_code, '->', resp.url)

# the generator releases data as soon as it becomes available 
for resp in (requests.get(url) for url in urls):
    print(len(resp.content), '->', resp.status_code, '->', resp.url)
