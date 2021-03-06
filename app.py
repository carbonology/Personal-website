import tornado.ioloop
import tornado.web
import tornado.httpserver
import os.path

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('main.html')

class tempHandler(tornado.web.RequestHandler):
	def get(self):
		self.render('underConstruction.html')

settings = dict(
	template_path = os.path.join(os.path.dirname(__file__), "templates"),
	static_path = os.path.join(os.path.dirname(__file__), "static"),
	debug = False
)

handlers = [(r'/', MainHandler),
			(r'/underConstruction', tempHandler)]

def app():
	print('Server Running...')
	print('Press ctrl + c to close')
	application = tornado.web.Application(handlers, **settings)
	http_server = tornado.httpserver.HTTPServer(application)
	port = int(os.environ.get("PORT", 5000))
	http_server.listen(port)
	#application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()

#Start the server at port n
if __name__ == "__main__":
	app()