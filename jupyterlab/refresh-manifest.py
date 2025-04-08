import yaml
import random
import string
import os
from time import sleep

def generate_random_suffix(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


while(True):
    #with open("/opt/conda/lib/python3.11/site-packages/dask_labextension/DaskCluster.yaml") as f:
    #    manifest = yaml.safe_load(f)

    #random_suffix = generate_random_suffix()
    #manifest["metadata"]["name"] =  "dask-" + os.environ.get("USERNAME") + "-" + random_suffix
    #manifest["spec"]["scheduler"]["service"]["selector"]["dask.org/cluster-name"] = "dask-" + os.environ.get("USERNAME") + "-" + random_suffix
    #manifest["spec"]["scheduler"]["spec"]["containers"][0]["image"] = "ghcr.io/icsc-spoke2-repo/jlab:wp5-alma9-" + os.environ.get("IMAGE_TAG") 
    #manifest["spec"]["worker"]["spec"]["containers"][0]["image"] = "ghcr.io/icsc-spoke2-repo/jlab:wp5-alma9-" + os.environ.get("IMAGE_TAG") 

    #with open("/opt/conda/lib/python3.11/site-packages/dask_labextension/DaskCluster.yaml", "w") as f:
    #    yaml.dump(manifest, f)

    sleep(10)
