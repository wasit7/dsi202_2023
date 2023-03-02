import strawberry
from strawberry import auto
from typing import List
from . import models
from strawberry.django import mutations

@strawberry.django.filters.filter(models.Author, lookups=True)
class AuthorFilter:
    id: auto
    name: auto
    
@strawberry.django.type(models.Author, filters=AuthorFilter)
class AuthorType:
    id: auto
    name: auto

@strawberry.django.input(models.Author)
class AuthorInput:
    id: auto
    name: auto

@strawberry.django.filters.filter(models.Book, lookups=True)
class BookFilter:
    id: auto
    title: auto
    author: 'AuthorFilter'

@strawberry.django.type(models.Book)
class BookType:
    id: auto
    title: auto
    author: AuthorType

@strawberry.django.input(models.Book)
class BookInput:
    id: auto
    title: auto
    author: auto

@strawberry.django.input(models.Author, partial=True)
class AuthorPartialInput(AuthorInput):
    pass

@strawberry.django.input(models.Book, partial=True)
class BookPartialInput(BookInput):
    pass

@strawberry.type
class Query:
    book: BookType = strawberry.django.field()
    books: List[BookType] = strawberry.django.field()
 
    @strawberry.field
    def myauthors(self) -> List[AuthorType]:
        return models.Author.objects.all()



@strawberry.type
class Mutation:
    createBook: BookType = mutations.create(BookInput)
    createBooks: List[BookType] = mutations.create(BookInput)
    updateBooks: List[BookType] = mutations.update(BookPartialInput)
    deleteBooks: List[BookType] = mutations.delete()

    createAuthor: AuthorType = mutations.create(AuthorInput)
    createAuthors: List[AuthorType] = mutations.create(AuthorInput)
    updateAuthors: List[AuthorType] = mutations.update(AuthorPartialInput)
    deleteAuthors: List[AuthorType] = mutations.delete()
    
    @strawberry.mutation
    def mycreate_book(self, title: str, author_name: str) -> BookType:
        author, created = models.Author.objects.get_or_create(name=author_name)
        book = models.Book.objects.create(title=title, author=author)
        return book

schema = strawberry.Schema(query=Query, mutation=Mutation)

# mutation MyMutation {
#   createAuthors(data: [{name:"create_name1"},{name:"create_name2"}]) {
#     name
#     id
# 	}
# }