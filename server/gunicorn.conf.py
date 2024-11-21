import multiprocessing

bind='127.0.0.1:3333'
workers = multiprocessing.cpu_count() + 1
user = 'ildar'
timeout = 120