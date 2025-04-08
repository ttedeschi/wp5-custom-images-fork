import asyncio
import asyncssh
import sys
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

sched_port = int(sys.argv[1])
dash_port = int(sys.argv[2])
name = os.getenv("USERNAME")
token = os.getenv("TOKEN")

async def tunnel_scheduler():
    logger.debug("start tunnel scheduler")
    connection = await asyncssh.connect(
        "jhub.131.154.98.51.myip.cloud.infn.it",
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
        "jhub.131.154.98.51.myip.cloud.infn.it",
        port=31022,
        username=name,
        password=token,
        known_hosts=None,
    )
    forwarder = await connection.forward_remote_port(
        "0.0.0.0", dash_port, "0.0.0.0", dash_port
    )
    await forwarder.wait_closed()

async def main():
    loop = asyncio.get_running_loop()
    loop.create_task(tunnel_scheduler())
    loop.create_task(tunnel_dashboard())
    running = True
    while running:
        await asyncio.sleep(14)
        #logging.debug("Controller is Running...")

if __name__ == "__main__":
    asyncio.run(main())
