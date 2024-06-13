import click
from models.__init__ import SessionLocal
from models.hymns import Hymn, Key, Author

def exit_program():
    print('Goodbye!')
    exit()

def create_hymn(number, title, lyrics, author_name, key_name):
    """Create a new hymn."""
    session = SessionLocal()
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()

    key = session.query(Key).filter_by(name=key_name).first()
    if not key:
        key = Key(name=key_name)
        session.add(key)
        session.commit()

    hymn = Hymn(number=number, title=title, lyrics=lyrics, author_id=author.id, key_id=key.id)
    session.add(hymn)
    session.commit()
    session.close()
    click.echo(f"Hymn '{title}' was added successfully.")

def update_hymn(hymn_id, title, lyrics, author_name, key_name):
    """Update an existing hymn."""
    session = SessionLocal()
    hymn = session.query(Hymn).filter_by(id=hymn_id).first()
    if hymn:
        if title:
            hymn.title = title
        if lyrics:
            hymn.lyrics = lyrics
        if author_name:
            author = session.query(Author).filter_by(name=author_name).first()
            if not author:
                author = Author(name=author_name)
                session.add(author)
                session.commit()
            hymn.author_id = author.id
        if key_name:
            key = session.query(Key).filter_by(name=key_name).first()
            if not key:
                key = Key(name=key_name)
                session.add(key)
                session.commit()
            hymn.key_id = key.id
        session.commit()
        click.echo(f"Hymn '{hymn_id}' updated successfully.")
    else:
        click.echo("Hymn not found.")
    session.close()

def delete_hymn(hymn_id):
    """Delete a hymn."""
    session = SessionLocal()
    hymn = session.query(Hymn).filter_by(id=hymn_id).first()
    if hymn:
        session.delete(hymn)
        session.commit()
        click.echo(f"Hymn {hymn.title} has been deleted successfully.")
    else:
        click.echo('Hymn not found.')
    session.close()

def list_hymns():
    """List all hymns."""
    session = SessionLocal()
    hymns = session.query(Hymn).all()
    if hymns:
        for hymn in hymns:
            click.echo(f"{hymn.id}: {hymn.title} by {hymn.author.name} in {hymn.key.name}")
    else:
        click.echo('There are no hymns yet.')
    session.close()

def view_hymn_lyrics(hymn_id):
    """view lyrics"""
    session = SessionLocal()
    hymn = session.query(Hymn).filter_by(id=hymn_id).first()
    if hymn:
        click.echo(f"These are the lyrics for {hymn.title}: ")
        click.echo(hymn.lyrics)
    else:
        click.echo('Hymn not found')
    session.close()

def hymns_by_key(key_name):
    session = SessionLocal()
    hymns = session.query(Hymn).join(Key).filter(Key.name == key_name).all()
    if hymns:
        click.echo(f"Hymns in key {key_name}:")
        for hymn in hymns:
            click.echo(f"{hymn.id}: {hymn.title}")
    else:
        click.echo(f"No hymns found in key {key_name}.")
    session.close()

def hymns_by_author(author_name):
    session = SessionLocal()
    hymns = session.query(Hymn).join(Author).filter(Author.name == author_name).all()
    if hymns:
        click.echo(f"Hymns by {author_name}:")
        for hymn in hymns:
            click.echo(f"{hymn.id}: {hymn.title}")
    else:
        click.echo(f"No hymns found by {author_name}.")
    session.close()