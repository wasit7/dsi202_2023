// Get a reference to the form and the book list
const bookForm = document.querySelector('#book-form');
const bookList = document.querySelector('#book-list');

// Listen for the form submission event
bookForm.addEventListener('change', (event) => {
  event.preventDefault();

  // Get the selected author ID from the form
  const authorId = document.querySelector('#author').value;

  // Send an AJAX request to the server to get the list of books by author
  fetch(`/book_app/api/authors/${authorId}/`)
    .then(response => response.json())
    .then(author => {
      // Clear the previous book list
      bookList.innerHTML = '';

      // Add each book to the book list
      author.books.forEach(book => {
        const li = document.createElement('li');
        li.textContent = book.title;
        bookList.appendChild(li);
      });
    });
});