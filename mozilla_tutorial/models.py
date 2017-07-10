from django.db import models
import uuid

from django.urls import reverse


class Genre(models.Model):
    """
    Model representing a book genre.
    (e.g: Science Fiction, Non Fiction)
    """
    name = models.CharField(max_length=100, help_text='Enter a book genre (e.g. Science Fiction, Non Fiction ..etc).')

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=200, help_text='Enter a book title (e.g. Harry Potter, Doctor Maisy ..etc).')
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.CharField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField(
        max_length=13,
        help_text='Enter 13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN Number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self):
        return self.title

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book
    (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4(),
        help_text='Unique ID for this particular book across whole library')
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=100)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('d', 'Maintenance'),
        ('o', 'On lone'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        """
        String for representing the Model object.
        :return:
            String: "id:(book_title)"
            e.g. "1234567890(HarryPotter)"
        """
        return '%s(%s)' % (self.id, self.book.title)

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Book availability')


class Author(models.Model):
    """
    Models representing an author
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        :return:
            String: "/author/(id)"
            e.g.: "/author/1234567890"
        """
        return reverse("author_detail", args=str(self.id))

    def __str__(self):
        """
        String for representing the Model object.
        :return: String "(first_name), (last_name)", e.g.: "Michel, jacson"
        """
        return '%s, %s' % (self.first_name, self.last_name)
