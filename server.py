# A simple starlette server.

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'page': 'home'})


async def posts(request):
    return JSONResponse({'page': 'posts'})


async def projects(request):
    return JSONResponse({'page': 'projects'})


async def about(request):
    return JSONResponse({'page': 'about'})

app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/posts', posts),
    Route('/projects', projects),
    Route('/about', about)
])