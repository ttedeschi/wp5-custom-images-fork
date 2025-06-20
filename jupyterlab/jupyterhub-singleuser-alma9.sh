#!/bin/bash

/usr/bin/tini -s /opt/conda/bin/python3.11 -- /usr/local/bin/jupyterhub-singleuser "$@" --debug & python3 /opt/conda/lib/python3.11/site-packages/dask_labextension/refresh-manifest.py & python3 /opt/conda/lib/python3.11/site-packages/dask_labextension/update_daskworkergroups.py