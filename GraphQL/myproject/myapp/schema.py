import strawberry
from strawberry import auto
from typing import List, Optional
from .models import Author, Book
import strawberry_django 
from strawberry_django import mutations
from strawberry_django.fields.types import DjangoFileType
from strawberry.file_uploads import Upload
from django.contrib.auth import get_user_model
import strawberry_django.auth as auth

@strawberry.django.type(Author)
class AuthorType:
    id: auto
    name: auto
    image: auto
    # books: "List[Book]"

@strawberry.django.input(Author, partial=True)
class AuthorInput:
    id: auto
    name: auto
    image: Upload

@strawberry.django.type(Book)
class BookType:
    id: auto
    title: auto
    author: AuthorType
    cover: auto

@strawberry.django.input(Book, partial=True)
class BookInput:
    id: auto
    title: auto
    author: auto #AuthorInput
    cover: Upload # Optional[DjangoFileType] #= strawberry_django.field(resolver=resolve_picture)

@strawberry.django.type(get_user_model())
class User:
    username: auto
    email: auto

@strawberry.type
class Query:
    authors: List[AuthorType] = strawberry.django.field()
    books: List[BookType] = strawberry.django.field()
    me: User = auth.current_user()


@strawberry.type
class Mutation:
    createAuthor: AuthorType = strawberry.django.mutations.create(AuthorInput)
    createBook: BookType = strawberry.django.mutations.create(BookInput)
    createBooks: List[BookType] = strawberry.django.mutations.create(BookInput)
    #updateBooks: List[BookType] = strawberry.django.mutations.update(BookPartialInput)
    #deleteBooks: List[BookType] = strawberry.django.mutations.delete()

schema = strawberry.Schema(query=Query, mutation=Mutation)


# mutation MyMutation {
#   createBook(data: {author: {set: "9"}, title: "test nine"}) {
#     id
#     author {
#       name
#       id
#     }
#     title
#   }
# }

# query MyQuery {
#   books {
#     author {
#       name
#       id
#     }
#     id
#     title
#   }
# }


# curl 'http://127.0.0.1:8000/myapp/graphql/' \
#   --data-raw '{"query":"query MyQuery {\n  books {\n    id\n    title\n  }\n}","operationName":"MyQuery"}'

# mutation MyMutation($cover: Upload = "dogs.jpg") {
#   createBook(data: {author: {set: "8"}, cover: $cover}) {
#     title
#     cover {
#       height
#       name
#       path
#       url
#       size
#       width
#     }
#   }
# }

# curl --request POST \
#   --url http://127.0.0.1:8000/myapp/graphql/ \
#   --form 'operations={"query":"mutation MyMutation($file: Upload!) {\n  createAuthor(data: {name: \"my great author\", image: $file}) {\n    id\n  }\n}","variables": { "file": null } }' \
#   --form 'map={ "nFile": ["variables.file"] }' \
#   --form nFile=@author.png
