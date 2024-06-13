import click
from helpers import (
    exit_program,
    create_hymn,
    update_hymn,
    delete_hymn,
    list_hymns,
    view_hymn_lyrics,
    hymns_by_key,
    hymns_by_author
)

def menu():
    click.echo("Hello please select an option:")
    click.echo("0: Exit the program")
    click.echo("1: Create a hymn")
    click.echo("2: Update a hymn")
    click.echo("3: List hymns")
    click.echo("4: Delete a hymn")
    click.echo("5: View hymn lyrics")
    click.echo("6: Hymns that have the same key")
    click.echo("7: Hymns by author")

def main():
    while True:
        menu()
        choice = click.prompt(">", type=str)
        if choice == "0":
            exit_program()
        elif choice == "1":
            create_hymn_input()
        elif choice == "2":
            update_hymn_input()
        elif choice == "3":
            list_hymns()
        elif choice == "4":
            delete_hymn_input()
        elif choice == "5":
            view_hymn_lyrics_input()
        elif choice == "6":
            hymns_by_key_input()
        elif choice == "7":
            hymns_by_author_input()
        else:
            click.echo("Oops! Invalid choice.")

def create_hymn_input():
    number = click.prompt("Hymn Number:", type=int)
    title = click.prompt("Title:")
    lyrics = click.prompt("Lyrics:")
    author_name = click.prompt("Author Name:")
    key_name = click.prompt("Key Name:")
    create_hymn(number, title, lyrics, author_name, key_name)

def update_hymn_input():
    hymn_id = click.prompt("Hymn ID:", type=int)
    title = click.prompt("New title for the hymn:")
    lyrics = click.prompt("New lyrics for the hymn:")
    author_name = click.prompt("New author for the hymn:")
    key_name = click.prompt("New key for the hymn:")
    update_hymn(hymn_id, title, lyrics, author_name, key_name)

def delete_hymn_input():
    hymn_id = click.prompt("Hymn ID:", type=int)
    delete_hymn(hymn_id)

def view_hymn_lyrics_input():
    identifier = click.prompt("Enter hymn number or title:")
    view_hymn_lyrics(identifier)

def hymns_by_key_input():
    key_name = click.prompt("Enter the key: ")
    hymns_by_key(key_name)

def hymns_by_author_input():
    author_name = click.prompt("Enter the author: ")
    hymns_by_author(author_name)

if __name__ == "__main__":
    main()
