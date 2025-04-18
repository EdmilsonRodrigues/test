# Copyright 2023 Canonical Ltd.
# Licensed under the Apache V2, see LICENCE file for details.

"""This example:

1. Connects to current controller.
2. Gets the cloud name in which the controller lives on
3. Disconnects from the controller

"""

import asyncio
import logging

from juju.controller import Controller


async def main():
    controller = Controller()
    # connect to current controller with current user, per Juju CLI
    await controller.connect()

    await controller.get_cloud()

    await controller.disconnect()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    ws_logger = logging.getLogger("websockets.protocol")
    ws_logger.setLevel(logging.INFO)
    asyncio.run(main())
