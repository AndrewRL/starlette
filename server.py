# A simple starlette server.

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from datetime import datetime, timedelta
from db.create_db import get_db
from sqlalchemy import Table, select
from models import Post, Project, Review


templates = Jinja2Templates(directory='static/html')


fake_courses = [{
    'timestamp': datetime.now(),
    'last_updated': datetime.now(),
    'thumbnail': None,
    'name': "Ender's Game",
    'short_summary': "A favorite from my childhood with ideas that have aged well with me.",
    'long_summary': "Nobody has time to type a good long summary while they are laying out a website. " +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website.",
    'review': 'I love this book. It is very great. I think I will continue to like it. I should read the others.',
    'rating': 9,
    'notes': '',
    'margin_notes':[],
    'tags': ['fiction', 'young-adult', 'sci-fi', 'futurism', 'politics'],
    'references': [],
    'affiliate_link': '',
}, {
    'timestamp': datetime.now() - timedelta(days=80),
    'last_updated': datetime.now(),
    'thumbnail': None,
    'name': "Bender's Game",
    'short_summary': "Futurama my llama.",
    'long_summary': "Nobody has time to type a good long summary while they are laying out a website. " +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website.",
    'review': 'Get bent.',
    'rating': 7,
    'notes': '',
    'margin_notes':[],
    'tags': ['fiction', 'young-adult', 'sci-fi', 'futurism', 'humor'],
    'references': [],
    'affiliate_link': '',
}, {
    'timestamp': datetime.now() - timedelta(days=365*2),
    'last_updated': datetime.now(),
    'thumbnail': None,
    'name': "Fender's Game",
    'short_summary': "Demolition derby has never felt so lame.",
    'long_summary': "Nobody has time to type a good long summary while they are laying out a website. " +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website." +
                    "Nobody has time to type a good long summary while they are laying out a website.",
    'review': "I couldn't bear to endure a second more.",
    'rating': 2,
    'notes': '',
    'margin_notes':[],
    'tags': ['non-fiction', 'cars', 'demolition-derby'],
    'references': [],
    'affiliate_link': '',
}]


def get_items(table_name, item_type, limit=100):
    db, metadata = get_db()
    table = Table(table_name, metadata, autoload=True, autoload_with=db)
    sql = select([table])
    items = [item_type(item) for item in db.execute(sql).fetchmany(limit)]
    return items


def get_item(table_name, item_type, item_id):
    db, metadata = get_db()
    posts_table = Table(table_name, metadata, autoload=True, autoload_with=db)
    sql = select([posts_table]).where(posts_table.c.id == item_id)

    post = item_type(db.execute(sql).fetchone())

    if post:
        return post

    raise Exception('Post not found.')


def get_post(post_id):
    db, metadata = get_db()
    posts_table = Table('posts', metadata, autoload=True, autoload_with=db)
    sql = select([posts_table]).where(posts_table.c.id == post_id)

    post = db.execute(sql).fetchone()

    if post:
        return post

    raise Exception('Post not found.')


def get_projects(source, limit=None):
    if limit is None:
        limit = len(source)

    if len(source) < limit:
        limit = len(source)

    return source[:limit]


def get_up_to_n(source, limit=None):
    if limit is None:
        limit = len(source)

    if len(source) < limit:
        limit = len(source)

    return source[:limit]


async def homepage(request):
    # TODO: Send the 10 most recent posts and projects to be rendered in their respective sections
    recent_posts = [post.to_dict() for post in get_items('posts', Post, 5)]
    recent_projects = [project.to_dict() for project in get_items('projects', Project, 5)]
    recent_reviews = [review.to_dict() for review in get_items('reviews', Review, 5)]
    return templates.TemplateResponse('home.html', {'request': request,
                                                    'posts': recent_posts,
                                                    'projects': recent_projects,
                                                    'reviews': recent_reviews})


async def posts(request):
    all_posts = get_items('posts', Post)
    all_posts = [post.to_dict() for post in all_posts]
    return templates.TemplateResponse('posts.html', {'request': request, 'posts': all_posts})


async def post(request):
    post_id = int(request.path_params['post_id'])
    post = get_item('posts', Post, post_id)
    return templates.TemplateResponse('post.html', {'request': request, 'post': post})


async def projects(request):
    all_projects = get_items('projects', Project)
    all_projects = [project.to_dict() for project in all_projects]
    return templates.TemplateResponse('projects.html', {'request': request, 'projects': all_projects})


async def project(request):
    project_id = int(request.path_params['project_id'])
    project = get_item('projects', Project, project_id).to_dict()
    return templates.TemplateResponse('project.html', {'request': request, 'project': project})


async def reviews(request):
    all_reviews = get_items('reviews', Review)
    all_reviews = [review.to_dict() for review in all_reviews]
    print(all_reviews)
    return templates.TemplateResponse('reviews.html', {'request': request, 'reviews': all_reviews})


async def review(request):
    review_id = int(request.path_params['review_id'])
    review = get_item('reviews', Review, review_id).to_dict()
    return templates.TemplateResponse('review.html', {'request': request, 'review': review})


async def about(request):
    return templates.TemplateResponse('base.html', {'request': request})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/posts', posts),
    Route('/post/{post_id}', post),
    Route('/projects', projects),
    Route('/project/{project_id}', project),
    Route('/reviews', reviews),
    Route('/review/{review_id}', review),
    Route('/about', about),
    Mount('/static', app=StaticFiles(directory='static'), name="static")
])