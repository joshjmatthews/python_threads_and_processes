import time
import requests
from fast_map import fast_map

# a youtube video url
url = 'https://www.youtube.com/watch?v=m4-HM_sCvtQ&ab_channel=Fireship'

# an I/O and cpu bound program that downloads content from a url and calculates numbers squared
def cpuAndIOBoundFunction(i, url=url, requests=requests):
    response = requests.get(url)
    val = i*i
    return (val, response)

if __name__ == '__main__':
    start = time.perf_counter()
    result = [i for i in fast_map(cpuAndIOBoundFunction, range(1000, 1050))]
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds. Length of results = {len(result)}")