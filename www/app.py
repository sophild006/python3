import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web

def index(request):
	return web.Response(body='<html><body><a href="http://www.baidu.com">µÇÂ¼</a></body></html>')

@asyncio.coroutine
def init(loop):
	logging.info('start...')
	app = web.Application(loop=loop)
	logging.info('===')
	app.router.add_route('GET','/',index)
	logging.info('-----')
	srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
	