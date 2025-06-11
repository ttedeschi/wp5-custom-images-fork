from kubernetes import client, config
import requests
import time

config.load_incluster_config()

custom_api = client.CustomObjectsApi()

namespace = "jhub"

updated = []

while True:
    worker_groups = custom_api.list_namespaced_custom_object(
    group="kubernetes.dask.org",
    version="v1",
    namespace=namespace,
    plural="daskworkergroups"
    )
    for item in worker_groups["items"]:
        name_complete = item["metadata"]["name"]
        name = item["metadata"]["name"][:-8] #remove -default
        if name not in updated: 
            try: 
                print(f"Modifying env for: {name}")
                
                containers = item["spec"]["worker"]["spec"]["containers"]
                container = containers[0]
            
                port = int(container["env"][0]["value"].split(":")[-1]) + 2
                ip_url = "http://" + name + "-scheduler.jhub:" + str(port) + "/ip"
                response = requests.get(ip_url, timeout=5)
                data = response.json()     
                ip = data["private_ip"].strip()
            
                container["env"][0]["value"] = container["env"][0]["value"].replace("localhost", ip) 
            
                custom_api.patch_namespaced_custom_object(
                    group="kubernetes.dask.org",
                    version="v1",
                    namespace=namespace,
                    plural="daskworkergroups",
                    name=name_complete,
                    body=item
                )
                
                updated.append(name)
            except:
                pass
                
    time.sleep(1)
