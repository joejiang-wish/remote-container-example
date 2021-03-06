import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application(
        [
            (r"/", MainHandler),
        ]
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado_application = tornado.ioloop.IOLoop.current()

    kwargs = dict(tornado_application=tornado_application)

    tornado_application.start()