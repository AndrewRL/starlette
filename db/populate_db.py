from faker import Faker
from random import randint
from sqlalchemy import create_engine
import json
import base64
# Create a function which returns a dict of fake project data
faker = Faker()

DB_PATH = '/Users/andrewlaird/PycharmProjects/starlette/psite.db'


def fake_post():
    post = {
        'id': faker.random_int(0, 10000),
        'title': faker.sentence(10),
        'timestamp': faker.date_time_between(start_date="-3y"),
        'length_in_min': faker.random_int(1, 30),
        'short_summary': faker.sentence(20),
        'long_summary': faker.text(250),
        'thumbnail': None,
        'lead_image': 'psite_test_photo.jpg',
        'body': generate_fake_paragraphs(10),
        'margin_notes': [],
        'refs': [],
        'tags': faker.words(3, ['wolf', 'mouse', 'bat', 'sheep', 'cow', 'swine'], unique=True)
    }

    return post


def fake_project():

    project = {
        'id': faker.random_int(0, 1000),
        'name': faker.sentence(4),
        'github': faker.url(),
        'docs': faker.url(),
        'created': faker.date_time_between(start_date="-3y"),
        'updated': faker.date_time_between(start_date="-3y"),
        'thumbnail': 'psite_test_photo.jpg',
        'lead_image': 'psite_test_photo.jpg',
        'short_summary': faker.sentence(20),
        'long_summary': faker.text(250),
        'body': generate_fake_paragraphs(7),
        'margin_notes': [],
        'tags': faker.words(faker.random_int(2, 5)),
        'refs': []
    }

    return project


def fake_review():
    review = {
        'id': faker.random_int(0, 10000),
        'timestamp': faker.date_time_between(start_date="-3y"),
        'name': faker.sentence(5),
        'creator': faker.name(),
        'publication_year': faker.random_int(1900, 2020),
        'summary': faker.sentence(20),
        'body': generate_fake_paragraphs(4),
        'rating': faker.random_int(0, 10),
        'notes': faker.url(),
        'margin_notes': [],
        'tags': faker.words(3),
        'refs': [],
        'link': faker.url()
    }

    return review


def generate_fake_paragraphs(number=5):
    new_paragraphs = []
    for _ in range(number):
        paragraph = ' '.join(faker.sentences(randint(3, 10)))
        new_paragraphs.append(f"<p>{paragraph}</p>")
    new_paragraphs = ''.join(new_paragraphs)
    return new_paragraphs


def populate_posts(posts):
    # Establish db connection
    engine = create_engine(f'sqlite:///{DB_PATH}')
    # Create connection
    conn = engine.connect()
    # Begin transaction
    trans = conn.begin()
    for post in posts:
        # Convert datetime to string
        post['timestamp'] = post['timestamp'].strftime('%Y-%m-%d %H:%M:%S')

        # Serialize lists
        post['margin_notes'] = base64.b64encode(json.dumps(post['margin_notes']).encode('utf-8'))
        post['refs'] = base64.b64encode(json.dumps(post['refs']).encode('utf-8'))
        post['tags'] = base64.b64encode(json.dumps(post['tags']).encode('utf-8'))

        conn.execute('INSERT INTO "posts" (id, '
                     'title, '
                     'timestamp, '
                     'length_in_min, '
                     'short_summary, '
                     'long_summary, '
                     'thumbnail, '
                     'lead_image, '
                     'body, '
                     'margin_notes, '
                     'refs, '
                     'tags)'
                     f'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [post[key] for key in post.keys()])
    trans.commit()
    # Close connection
    conn.close()
    
    
def populate_projects(projects):
    # Establish db connection
    engine = create_engine(f'sqlite:///{DB_PATH}')
    # Create connection
    conn = engine.connect()
    # Begin transaction
    trans = conn.begin()
    for project in projects:
        # Convert datetime to string
        project['created'] = project['created'].strftime('%Y-%m-%d %H:%M:%S')
        project['updated'] = project['updated'].strftime('%Y-%m-%d %H:%M:%S')

        # Serialize lists
        project['margin_notes'] = base64.b64encode(json.dumps(project['margin_notes']).encode('utf-8'))
        project['refs'] = base64.b64encode(json.dumps(project['refs']).encode('utf-8'))
        project['tags'] = base64.b64encode(json.dumps(project['tags']).encode('utf-8'))

        conn.execute('INSERT INTO "projects" (id, '
                     'name, '
                     'github, '
                     'docs, '
                     'created, '
                     'updated, '
                     'thumbnail, '
                     'lead_image, '
                     'short_summary, '
                     'long_summary, '
                     'body, '
                     'margin_notes, '
                     'tags, '
                     'refs)'
                     f'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [project[key] for key in project.keys()])
    trans.commit()
    # Close connection
    conn.close()
    

def populate_reviews(reviews):
    # Establish db connection
    engine = create_engine(f'sqlite:///{DB_PATH}')
    # Create connection
    conn = engine.connect()
    # Begin transaction
    trans = conn.begin()
    for review in reviews:
        # Convert datetime to string
        review['timestamp'] = review['timestamp'].strftime('%Y-%m-%d %H:%M:%S')

        # Serialize lists
        review['margin_notes'] = base64.b64encode(json.dumps(review['margin_notes']).encode('utf-8'))
        review['refs'] = base64.b64encode(json.dumps(review['refs']).encode('utf-8'))
        review['tags'] = base64.b64encode(json.dumps(review['tags']).encode('utf-8'))

        conn.execute('INSERT INTO "reviews" (id, '
                     'timestamp, '
                     'name, '
                     'creator, '
                     'publication_year, '
                     'summary, '
                     'body, '
                     'rating, '
                     'notes, '
                     'margin_notes, '
                     'tags, '
                     'refs, '
                     'link)'
                     f'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', [review[key] for key in review.keys()])
    trans.commit()
    # Close connection
    conn.close()
    

if __name__ == '__main__':
    posts = [fake_post() for _ in range(20)]
    print(f'Adding {len(posts)} posts to db.')
    populate_posts(posts)
    
    projects = [fake_project() for _ in range(20)]
    print(f'Adding {len(projects)} projects to db.')
    populate_projects(projects)

    reviews = [fake_review() for _ in range(20)]
    print(f'Adding {len(reviews)} reviews to db.')
    populate_reviews(reviews)

