from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text

DB_PATH = '/Users/andrewlaird/PycharmProjects/starlette/psite.db'


def create_posts_table():
    engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)
    meta = MetaData()

    posts = Table(
        'posts', meta,
        Column('id', Integer, primary_key=True),
        Column('title', Text),
        Column('timestamp', Text),
        Column('length_in_min', Integer),
        Column('short_summary', Text),
        Column('long_summary', Text),
        Column('thumbnail', Text),
        Column('lead_image', Text),
        Column('body', Text),
        Column('margin_notes', Text),
        Column('refs', Text),
        Column('tags', Text)
    )

    meta.create_all(engine)


def create_projects_table():
    engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)
    meta = MetaData()

    projects = Table(
        'projects', meta,
        Column('id', Integer, primary_key=True),
        Column('name', Text),
        Column('github', Text),
        Column('docs', Text),
        Column('created', Text),
        Column('updated', Text),
        Column('thumbnail', Text),
        Column('lead_image', Text),
        Column('short_summary', Text),
        Column('long_summary', Text),
        Column('body', Text),
        Column('margin_notes', Text),
        Column('tags', Text),
        Column('refs', Text)
    )

    meta.create_all(engine)


def create_reviews_table():
    engine = create_engine(f'sqlite:///{DB_PATH}', echo=True)
    meta = MetaData()

    reviews = Table(
        'reviews', meta,
        Column('id', Integer, primary_key=True),
        Column('timestamp', Text),
        Column('name', Text),
        Column('creator', Text),
        Column('publication_year', Integer),
        Column('summary', Text),
        Column('body', Text),
        Column('rating', Integer),
        Column('notes', Text),
        Column('margin_notes', Text),
        Column('tags', Text),
        Column('refs', Text),
        Column('link', Text)
    )

    meta.create_all(engine)


def get_db():
    engine = create_engine('sqlite:///psite.db')
    metadata = MetaData(bind=engine)
    conn = engine.connect()
    return conn, metadata


if __name__ == '__main__':
    create_posts_table()
    create_projects_table()
    create_reviews_table()
