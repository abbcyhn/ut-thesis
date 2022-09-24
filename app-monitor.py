import time
import psutil as pu
from tcp_latency import measure_latency

def get_latency(host):
	result = measure_latency(host)
	if isinstance(result, list):
		result = sum(result) / len(result)
	latency = round(result, 2)
	return latency

def get_cpu_usage():
	cpu_usage = pu.cpu_percent()
	while cpu_usage == 0 or cpu_usage == 100:
		cpu_usage = pu.cpu_percent()
		time.sleep(1)
	return cpu_usage
	
def get_ram_usage():
	ram_usage = pu.virtual_memory().percent
	return ram_usage

def print_usage(name, usage, newline = False):
	bar_cnt = 20
	percent = (usage / 100.0)
	bar_str = '█' * int(percent * bar_cnt) + '-' * (bar_cnt - int(percent * bar_cnt))
	print(f"{name} Usage: |{bar_str}| {usage:.2f}%")
	if newline: print()		



start = time.monotonic()
cpu_usage = get_cpu_usage()
end = time.monotonic()
runtime = round(end - start, 2)
print_usage(f"RUNTIME: {runtime}. CPU", cpu_usage, newline = True) 


start = time.monotonic()
ram_usage = get_ram_usage()
end = time.monotonic()
runtime = round(end - start, 2)
print_usage(f"RUNTIME: {runtime}. RAM", ram_usage, newline = True)


host = "216.58.210.174"
start = time.monotonic()
latency = get_latency(host)
end = time.monotonic()
runtime = round(end - start, 2)
print(f"RUNTIME = {runtime}. LATENCY of {host} is {latency} ms")
