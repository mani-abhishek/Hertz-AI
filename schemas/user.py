from pydantic import BaseModel


class User(BaseModel):
    bookName:str
    pageNumber: int
    topicName:str
    chapterName:str
    text1:str