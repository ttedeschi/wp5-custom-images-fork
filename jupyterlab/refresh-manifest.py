import yaml
import random
import string
import os
from time import sleep

def generate_random_suffix(length=5):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))


while(True):
    with open("/opt/conda/lib/python3.11/site-packages/dask_labextension/DaskCluster_template.yaml") as f:
        manifest = yaml.safe_load(f)

    random_suffix = generate_random_suffix()
    manifest["metadata"]["name"] =  "dask-" + os.environ.get("USERNAME") + "-" + random_suffix
    #manifest["spec"]["scheduler"]["service"]["selector"]["dask.org/cluster-name"] = "dask-" + os.environ.get("USERNAME") + "-" + random_suffix

    random_scheduler_port = int(random.uniform(8000, 9998))
    random_dashboard_port = random_scheduler_port + 1 
    random_privateip_port = random_scheduler_port + 2 
    manifest["spec"]["scheduler"]["service"]["ports"][0]['port'] = random_scheduler_port
    manifest["spec"]["scheduler"]["service"]["ports"][0]['targetPort'] = random_scheduler_port
    manifest["spec"]["scheduler"]["service"]["ports"][1]['port'] = random_dashboard_port
    manifest["spec"]["scheduler"]["service"]["ports"][1]['targetPort'] = random_dashboard_port
    manifest["spec"]["scheduler"]["service"]["ports"][2]['port'] = random_privateip_port
    manifest["spec"]["scheduler"]["service"]["ports"][2]['targetPort'] = random_privateip_port
    manifest["spec"]["scheduler"]["spec"]["containers"][0]['args'][2] = manifest["spec"]["scheduler"]["spec"]["containers"][0]['args'][2].replace("8912", str(random_scheduler_port)).replace("8913", str(random_dashboard_port)).replace("8914", str(random_privateip_port))
    manifest["spec"]["worker"]["spec"]["containers"][0]['env'][0]["value"] = manifest["spec"]["worker"]["spec"]["containers"][0]['env'][0]["value"].replace("8912", str(random_scheduler_port))

    #manifest["spec"]["scheduler"]["spec"]["containers"][0]["image"] = "ghcr.io/icsc-spoke2-repo/jlab:wp5-alma9-" + os.environ.get("IMAGE_TAG") 
    #manifest["spec"]["worker"]["spec"]["containers"][0]["image"] = "ghcr.io/icsc-spoke2-repo/jlab:wp5-alma9-" + os.environ.get("IMAGE_TAG") 
    manifest["spec"]["scheduler"]["spec"]["containers"][0]["image"] = "/cvmfs/unpacked.infn.it/harbor.cloud.infn.it/unpacked/jlab:wp5-alma9-highrate-offload-v0.0.3" 
    manifest["spec"]["worker"]["spec"]["containers"][0]["image"] = "/cvmfs/unpacked.infn.it/harbor.cloud.infn.it/unpacked/jlab:wp5-alma9-highrate-offload-v0.0.3" 
    manifest["spec"]["scheduler"]["spec"]['containers'][0]["env"][0]['value'] = os.getenv("JUPYTERHUB_USER")
    manifest["spec"]["scheduler"]["spec"]['containers'][0]["env"][1]['value'] = os.getenv("JUPYTERHUB_API_TOKEN")

    with open("/opt/conda/lib/python3.11/site-packages/dask_labextension/DaskCluster.yaml", "w") as f:
        yaml.dump(manifest, f)

    sleep(10)
