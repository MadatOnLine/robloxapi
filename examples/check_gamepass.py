import robloxapi, asyncio
client = robloxapi.Client()


async def main():
    ira = await client.get_user_by_id(109503558)
    if await ira.has_gamepass(7430441):
        print('he has it!!!!')

asyncio.run(main())
