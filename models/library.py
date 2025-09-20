from . import db

class Library(db.Model):
    __tablename__ = 'libraries'

    isbn = db.Column(db.String, primary_key=True)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)

    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author
        }