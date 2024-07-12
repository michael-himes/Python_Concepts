# Process pool template
# https://docs.python.org/3/3library/multiprocessing.html
# https://stackoverflow.com/questions/20776189/concurrent-futures-vs-muliprocessing-in-python-3
from multiprocessing import Pool, Manager

# server process
# A manager object returned by Manager() controls a server process which holds
# Python objects and allows other processes to manipulate them using proxies.
server_process = Manager()
proxy_accessed_list = server_process.list()

def add_to_list(x):
    proxy_accessed_list.append(x)

# Create pool of worker processes
pool = Pool(processes=10)

# Kick off 10 individual processes that 
# append to the list hosted by the server process
# add_to_list(0)
# add_to_list(1)
# etc..
results = pool.map(
    add_to_list, [x for x in range(0,10)]
)
pool.close()
pool.join()

# Results are not in order 
# Would like to explain why the pattern is fitting:
# proxy_accessed_list[0:3] == [0,9,1] 
print(list(proxy_accessed_list))
assert proxy_accessed_list != [x for x in range(0,10)]
# 1st iteration: [1, 9, 5, 0, 3, 2, 4, 6, 8, 7]
# 2nd iteration: [0, 9, 1, 3, 2, 4, 5, 7, 8, 6]
