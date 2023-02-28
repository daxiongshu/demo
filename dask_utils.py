import dask, dask_cudf
from dask.distributed import Client, wait
from dask_cuda import LocalCUDACluster
import subprocess

def get_ip():
    cmd = "hostname --all-ip-addresses"
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    IPADDR = str(output.decode()).split()[0]
    print(IPADDR)
    return IPADDR

def get_cluster():
    ip = get_ip()
    cluster = LocalCUDACluster(ip=ip)
    client = Client(cluster)
    return client
