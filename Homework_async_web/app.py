from aiohttp import web

async def create_app():
    app=web.Application()
    return app

if __name__ == '__main__':
    create_app()