import asyncio
import logging
import os
from time import sleep
import asyncssh

token = os.environ.get("JHUB_TOKEN")
name = os.environ.get("JHUB_USER", "")
sched_port = int(os.environ.get("SCHED_PORT", "42000"))
dash_port = int(os.environ.get("DASH_PORT", "42001"))
controller_port = int(os.environ.get("CONTROLLER_PORT", "42002"))

async def tunnel_scheduler():
    logger.debug("start tunnel scheduler")
    connection = await asyncssh.connect(
        "hub.131.154.98.51.myip.cloud.infn.it",
        port=31022,
        username=name,
        password=token,
        known_hosts=None,
    )
    forwarder = await connection.forward_remote_port(
        "0.0.0.0", sched_port, "0.0.0.0", sched_port
    )
    await forwarder.wait_closed()


async def tunnel_dashboard():
    logger.debug("start tunnel dashboard")
    connection = await asyncssh.connect(
        "hub.131.154.98.51.myip.cloud.infn.it",
        port=31022,
        username=name,
        password=token,
        known_hosts=None,
    )
    forwarder = await connection.forward_remote_port(
        "0.0.0.0", dash_port, "0.0.0.0", dash_port
    )
    await forwarder.wait_closed()


async def tunnel_controller():
    logger.debug("start tunnel controller")
    connection = await asyncssh.connect(
        "hub.131.154.98.51.myip.cloud.infn.it",
        port=31022,
        username=name,
        password=token,
        known_hosts=None,
    )
    forwarder = await connection.forward_remote_port(
        "0.0.0.0", controller_port, "0.0.0.0", controller_port
    )
    await forwarder.wait_closed()



async def main():
    loop = asyncio.get_running_loop()

    loop.create_task(tunnel_scheduler())
    loop.create_task(tunnel_dashboard())
    loop.create_task(tunnel_controller())

    running = True

    #while running:
    #    await asyncio.sleep(14)
    #    logging.debug("Controller is Running...")

if __name__ == "__main__":
    asyncio.run(main())
