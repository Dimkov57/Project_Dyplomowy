from sqlalchemy.orm import Session

from models.book import Book as BookModel
from schemas.book import BookCreate, BookUpdate


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(BookModel).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    return db.query(BookModel).filter(BookModel.id == book_id).first()


def create_book(db: Session, book: BookCreate):
    db_book = BookModel(title=book.title, author=book.author)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def update_book(db: Session, book_id: int, book: BookUpdate):
    db_book = get_book(db, book_id)
    if db_book is None:
        return None

    if book.title is not None:
        db_book.title = book.title
    if book.author is not None:
        db_book.author = book.author

    db.commit()
    db.refresh(db_book)
    return db_book


def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book is None:
        return False

    db.delete(db_book)
    db.commit()
    return True
