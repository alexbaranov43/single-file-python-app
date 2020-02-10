from waitress import serve
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

def static(request):
    print('Incoming request')
    return Response(
      '<body><h1>Hello User! This will always be static text</h1><p>In the address bar type, add "/" to the current address followed by any text you want to see that text appear on screen!</p><br><p>Or you can type "/multiply/" followed by a number, followed by another "/" and then a second number to see those two numbers multipled!<p><br><p>Or you can type "/json/dictionary" to learn more about the developer</p></body>')

@view_config(route_name='multiply')
def multiply(request):
    print('Incoming math request')
    a = request.matchdict['a']
    b = request.matchdict['b']
    math = int(a) * int(b)
    return Response('<body><h1>' + str(math) + '</h1><br><a href="/"><button>home</button></a></body>')

@view_config(route_name='text')
def text(request):
  print('Incoming text request')
  text = request.matchdict['text']
  return Response('<body><p>' + text + '</p><br><a href="/"><button>home</button></a></body>')

@view_config(route_name='dictionary', renderer='json')
def dictionary(request):
  print('Incoming dictionary request')
  my_object = {"name": "Alex Baranov", "Occupation": "Full Stack Developer", "Favorite Food": "Tacos", "Favorite Hobby": "Jiu Jitsu"}
  return my_object

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('static', '/')
        config.add_view(static, route_name='static')
        config.add_route('multiply', '/multiply/{a}/{b}')
        config.add_view(multiply, route_name='multiply')
        config.add_route('text', '/{text}')
        config.add_view(text, route_name='text')
        config.add_route('dictionary', '/json/dictionary')
        config.add_view(dictionary, route_name='dictionary', renderer='json')        
        app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=6543)