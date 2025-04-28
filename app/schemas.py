# ## define input  o/p model
# from pydantic import BaseModel

# class StoryRequest(BaseModel):
#     text: str


from pydantic import BaseModel

class StoryRequest(BaseModel):
    text: str
    filename: str = None  #optional


