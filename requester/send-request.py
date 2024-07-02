from multiprocessing import Pool

from requests import get

DOMAIN = "ec2-63-32-111-182.eu-west-1.compute.amazonaws.com"

def send_request(url):
    while True:
        response = get(f'http://{DOMAIN}')
        data = response.json()
        print('Request sent')
        print(data)

if __name__ == '__main__':
    with Pool(150) as p:
        p.map(send_request, range(150))