from strawberry_django_plus import gql
import strawberry
from .models import Author, Book

@gql.django.type(Author)
class AuthorType(gql.Node):
    id: gql.auto
    name: gql.auto

@gql.django.input(Author)
class AuthorInput:
    id: gql.auto
    name: gql.auto


@gql.django.partial(Author)
class AuthorInputPartial(gql.NodeInput):
    id: gql.auto
    name: gql.auto

@gql.django.type(Book)
class BookType(gql.Node):
    id: gql.auto
    title: gql.auto
    author: 'AuthorType'
    cover: gql.auto


@gql.django.input(Book)
class BookInput:
    id: gql.auto
    title: gql.auto
    author: 'AuthorInput'
    cover: gql.auto
    


@gql.django.partial(Book)
class BookInputPartial(gql.NodeInput):
    id: gql.auto
    title: gql.auto

@gql.type
class Query:
    author: AuthorType = gql.django.field()
    book: BookType = gql.django.field()

@gql.type
class Mutation:
    create_author: AuthorType = gql.django.create_mutation(AuthorInput)
    update_author: AuthorType = gql.django.update_mutation(AuthorInputPartial)
    delete_author: AuthorType = gql.django.delete_mutation(gql.NodeInput)

    create_book: BookType = gql.django.create_mutation(BookInput)
    update_book: BookType = gql.django.update_mutation(BookInputPartial)
    delete_book: BookType = gql.django.delete_mutation(gql.NodeInput)

schema = gql.Schema(query=Query, mutation=Mutation)