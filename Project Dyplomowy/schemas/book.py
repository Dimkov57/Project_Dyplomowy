from pydantic import BaseModel, ConfigDict, Field


class BookBase(BaseModel):
    title: str = Field(..., min_length=2, max_length=200)
    author: str = Field(..., min_length=2, max_length=150)


class BookCreate(BookBase):
    pass


class BookUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=2, max_length=200)
    author: str | None = Field(default=None, min_length=2, max_length=150)


class Book(BookBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
