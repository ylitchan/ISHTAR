import asyncio
import logging

from aiotdlib import Client

API_ID = 27117571
API_HASH = "49646a563c5f7ca80deddd57f0d47c2a"
PHONE_NUMBER = "+8617880356481"


async def main():
    client = Client(
        api_id=API_ID,
        api_hash=API_HASH,
        phone_number=PHONE_NUMBER,
        library_path=r'D:\allProjects\pyDemo\tgDemo\td\tdlib\lib\tdjson.lib'
    )

    async with client:
        me = await client.api.get_me()
        logging.info(f"Successfully logged in as {me.json()}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())