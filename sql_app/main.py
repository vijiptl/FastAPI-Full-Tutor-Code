# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def get_item(item_id: int):
#     return {"item_id": item_id}

# from enum import Enum
# from fastapi import FastAPI

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     lenet = "lenet"
#     resnet = "resnet"

# app = FastAPI()

# @app.get("/model/{model_name}")
# async def get_models(model_name: ModelName):
#     if model_name is ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep learning FWT!"}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}
#     return {"model_name": model_name, "message": "Have some residuals"}

# Creating a programme with Enum values into the path parameter

# from fastapi import FastAPI
# from enum import Enum

# class ModelName(str, Enum):
#     x1 = "alexnet"
#     x2 = "lenet"
#     x3 = "resnet"

# app = FastAPI()
# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name is ModelName.x1:
#         return {"model_name": model_name, "message": "Deep learning FWT!"}
#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN is same images"}
    
#     return {"model_name": model_name, "message": "Have same pages"}

# Create a programme for a Query parameter along path.

# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/items/{item_id}")
# async def get_item(item_id: str, q: str | None = None):
#     if q:
#         return {"item_id": item_id, "q": q}
#     return {"item_id": item_id}

# Create a programmme for multiple Path and Query parameter

# from fastapi import FastAPI

# app = FastAPI()
# @app.get("/items/{item_id}/users/{user_id}")
# async def read_item_user(item_id: str, user_id: int, q: str | None = None, short: bool= False):
#     item = {"item_id": item_id, "owner_id": user_id}
#     if q:
#         item.update({"q": q})
#     if not short:
#         item.update({"description": "Hi all I wish all the best for the day"})
#     return item

# Create a API with Request Body, Path and Query Parameters

# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# app = FastAPI()
# @app.post("/items/{item_id}")
# async def update_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result

#Create a API with more validation for Query parameter

# from fastapi import FastAPI, Query
# from typing import Annotated

# app = FastAPI()
# @app.get("/items")
# async def read_item(q: Annotated[str | None, Query(max_length=50)] = None):
#     result = {"items": [{"items_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         result.update({"q": q})
#     return result


# from fastapi import FastAPI, Query
# from typing import Annotated

# app = FastAPI()

# @app.get("/items")
# async def read_item(q: Annotated[list[str] | None, Query()] = None):
#     query_item = {"q": q}
#     return query_item

#Create a Query additional validations

# from fastapi import FastAPI, Query
# from typing import Annotated

# app = FastAPI()

# @app.get("/items")
# async def read_item(q: Annotated[str | None, Query(
#     alias="item-query",
#     title="Query string",
#     description="Query string for the items to search in DB",
#     min_length=3,
#     max_length=50,
#     pattern="^fixedquery$",
#     deprecated=True
# ),
# ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q":q})
#     return results
    
#Create a API with Mix of Path and Query

# from fastapi import FastAPI, Path, Query
# from typing import Annotated

# app = FastAPI()

# @app.get("/items/{item_id}")
# async def read_item(item_id: Annotated[int, Path(title="The ID of the item to get")], q: Annotated[str | None, Query(alias="item-query")] = None,):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# Create a API with Body, Path, Query parameters

# from fastapi import FastAPI, Path, Query
# from typing import Annotated
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name : str
#     description : str | None = None
#     price : float
#     tax : float | None = None

# class User(BaseModel):
#     usrename : str
#     full_name: str | None = None

# @app.post("/items/{item_id}")
# async def update_item(item_id: Annotated[int, Path(title = "The ID to get", ge = 0, le = 1000)], 
#                       q:str | None = None, item: Item | None = None, user: User | None = None):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

# Multiple Body parameters

# from fastapi import FastAPI, Path, Query
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None

# @app.put("/items/{item_id}/")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item": item, "user": user}
#     return results

# Singular value body parameter

# from typing import Annotated
# from pydantic import BaseModel
# from fastapi import FastAPI, Body

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None

# class User(BaseModel):
#     username: str

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User, importance: Annotated[int, Body()]):
#     results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
#     return results

# Embed Single value of Body parameter

# from fastapi import FastAPI, Body
# from typing import Annotated
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results

# Adding more validation and Metadata

# from fastapi import FastAPI, Body
# from typing import Annotated
# from pydantic import BaseModel, Field

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = Field(default = None, title = "The description of item", max_length = 300)
#     price: float = Field(gt = 0, description = "The price must be greater than zero")
#     tax: float

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
#     results = {"item_id": item_id, "item": item}
#     return results

# Create a Nested Body parameter

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()

# class Image(BaseModel):
#     url: HttpUrl
#     name: str | None = None

# class Item(BaseModel):
#     name: str
#     descritpion: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str]  = set()
#     image: list[Image] | None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

#Deeply Nested Body Parameter

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()

# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     images: list[Image] | None = None

# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     items: list[Item]

# @app.post("/offer/")
# async def create_offer(offer: Offer):
#     return offer

# Adding type within functions parameters

# from fastapi import FastAPI
# from pydantic import BaseModel, HttpUrl

# app = FastAPI()

# class Image(BaseModel):
#     url: HttpUrl
#     name: str

# @app.post("/images/multiples")
# async def create_multi_images(images: list[Image]):
#     for image in images:
#         image.url
#     return image

# Adding extra JSON example data with model_config model

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

#     model_config = {
#         "json_schema_extra": {
#             "eample": [
#                 {
#                     "name": "Foo",
#                     "description": "A very nice item",
#                     "price": 42.8,
#                     "tax": 4.2
#                 }
#             ]
#         }
#     }
# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# Adding extra schema example using Fiels than addition lines

# from fastapi import FastAPI
# from pydantic import BaseModel, Field

# app = FastAPI()

# class Item(BaseModel):
#     name: str = Field(examples = ["Foo"])
#     description: str | None = Field(default = None, examples = ["A very nice item"])
#     price: float = Field(examples = [42.8])
#     tax: float | None = Field(default = None, examples = [4.2])

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

#Adding examples like extra schema using Body model

# from fastapi import FastAPI, Body
# from typing import Annotated
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Annotated[Item, Body(examples = [{"name": "Foo", "description": "A very nice item",
#                                                                             "price": 42.8, "tax": 4.2}])]):
#     results = {"item_id": item_id, "item": item}
#     return results

# Extra Data Types

# from datetime import datetime, time, timedelta
# from typing import Annotated
# from uuid import UUID
# from fastapi import Body, FastAPI # type: ignore

# app = FastAPI()


# @app.put("/items/{item_id}")
# async def read_items(
#     item_id: UUID,
#     start_datetime: Annotated[datetime, Body()],
#     end_datetime: Annotated[datetime, Body()],
#     process_after: Annotated[timedelta, Body()],
#     repeat_at: Annotated[time | None, Body()] = None,
# ):
#     start_process = start_datetime + process_after
#     duration = end_datetime - start_process
#     return {
#         "item_id": item_id,
#         "start_datetime": start_datetime,
#         "end_datetime": end_datetime,
#         "process_after": process_after,
#         "repeat_at": repeat_at,
#         "start_process": start_process,
#         "duration": duration,
#     }

# Cookie Parameter

# from typing import Annotated
# from fastapi import Cookie, FastAPI

# app = FastAPI()
# @app.get("/items/")
# async def read_items(ads_id: Annotated[str | None, Cookie()] = None):
#     return {"ads_id": ads_id}

# Header Parameter

# from typing import Annotated
# from fastapi import FastAPI, Header

# app = FastAPI()
# @app.get("/items/")
# async def read_items(user_agent: Annotated[str | None, Header(convert_underscores = True)] = None):
#     return {"user_agent": user_agent}

# from fastapi import FastAPI, Header
# from typing import Annotated

# app = FastAPI()
# @app.get("/items/")
# async def read_items(x_token: Annotated[list[str] | None, Header()] = None):
#     return {"X-token": x_token}

# Response Model - Return Type(->)

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None

# @app.post("/items/")
# async def read_items(item: Item) -> Item:
#     return item

# @app.get("/items")
# async def read_items() -> list[Item]:
#     return [
#         Item(name = "Foo", price = 42.8),
#         Item(name = "Bar", price = 28.6)
#     ]

# Again using response_model type parameter for Decorator

# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import Any

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: list[str] = []

# @app.post("/items/", response_model=Item)
# async def create_item(item: Item) -> Any:
#     return item

# @app.get("/items/", response_model=list[Item])
# async def read_item() -> Any:
#     return [
#         {"name": "Foo", "price": 42.0},
#         {"name": "Baz", "price": 32.8}
#     ]

# Getting same Input as Output sample

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()
# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# @app.post("/user/")
# async def create_user(user: UserIn) -> UserIn:
#     return user

# Hidding or Flittering Output Data from Input Data

# from fastapi import FastAPI
# from typing import Any
# from pydantic import BaseModel, EmailStr

# app = FastAPI()
# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None

# class UserOut(BaseModel):
#     name: str
#     email: EmailStr
#     full_name: str | None = None
# @app.post("/user/", response_model=UserOut)
# async def create_user(user: UserIn) -> Any:
#     return user

# Adding more Filtters and Annotations to output data

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class BaseUser(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str
# class UserIn(BaseUser):
#     password: str
# @app.post("/user/")
# async def create_user(user: UserIn) -> BaseUser:
#     return user

# Other Return Types __annotations__

# from fastapi import FastAPI, Response
# from fastapi.responses import JSONResponse, RedirectResponse

# app = FastAPI()

# @app.get("/portal/")
# async def get_portal(teleport: bool = True) -> Response:
#     if teleport:
#         return RedirectResponse(url = "https://www.youtube.com/watch?v=Z6U3tVjHcUI")
#     return JSONResponse(content={"message": "Here's your interdimensional portal."})

# Other Return Types

# from fastapi import FastAPI
# from fastapi.responses import RedirectResponse, JSONResponse

# app = FastAPI()

# @app.get("/teleport")
# async def get_portal() -> RedirectResponse:
#     return RedirectResponse(url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Response model encoding parameters

# from fastapi import FastAPI, Response
# from pydantic import BaseModel

# app = FastAPI()
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float = 10.4
#     tags: list[str] = []

# items = {
#     "foo": {"name": "Foo", "price": 50.6},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 23.90, "tax": 2},
#     "baz": {"name": "Baz", "description": "The baztenders", "price": 42.9, "tax": 4, "tags": []}
# }

# @app.get("/items/{items_id}", response_model=Item, response_model_exclude_unset=True)
# async def read_item(item_id: str):
#     return items[item_id]

# Include and Exclude response model path operation decorator parameters

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     descriptiom: str | None = None
#     price: float
#     tax: float = 10.6

# items = {
#     "foo": {"name": "Foo", "price": 42.0},
#     "bar": {"name": "Bar", "description": "The bartenders", "price": 89, "tax": 2.6},
#     "baz": {"name": "Baz", "description": "The baztenders", "price": 22.8, "tax": 4.7} 
# }

# @app.get("/items/{item_id}/name", response_model=Item, response_model_include={"name", "description"})
# async def read_item(item_id: str):
#     return items[item_id]

# @app.get("/items/{item_id}/public", response_model=Item, response_model_exclude={"tax"})
# async def read_item(item_id: str):
#     return items[item_id]

# Multiple Models in one API

# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class UserIn(BaseModel):
#     username: str
#     password: str
#     email: EmailStr
#     full_name: str | None = None
# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
# class UserInDB(BaseModel):
#     username: str
#     hashed_password: str
#     email: EmailStr
#     full_name: str | None = None

# def fake_password(raw_password: str):
#     return "supersecret" + raw_password
# def fake_user_save(user_in: UserIn):
#     hashed_password = fake_password(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password = hashed_password)
#     print("User Saved! ..not really.")
#     return user_in_db
# @app.post("/user/", response_model = UserOut)
# async def create_user(user_in: UserIn):
#     user_save =fake_user_save(user_in)
#     return user_save

# Multiple Model Reducing Duplications
 
# from fastapi import FastAPI
# from pydantic import BaseModel, EmailStr

# app = FastAPI()

# class UserBase(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: str | None = None
# class UserIn(UserBase):
#     password: str
# class UserOut(UserBase): 
#     pass
# class UserInDB(UserBase):
#     hashed_password: str

# def fake_password(raw_password: str):
#     return "supersecret" + raw_password
# def fake_user_save(user_in: UserIn):
#     hashed_password = fake_password(user_in.password)
#     user_in_db = UserInDB(**user_in.dict(), hashed_password = hashed_password)
#     print("User Saved! ..not really.")
#     return user_in_db
# @app.post("/user/", response_model = UserOut)
# async def create_user(user_in: UserIn):
#     user_saved = fake_user_save(user_in)
#     return user_saved

# Union or anyoff of two types in Response

# from typing import Union

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class BaseItem(BaseModel):
#     description: str
#     type: str
# class CarItem(BaseItem):
#     type: str = "car"
# class PlaneItem(BaseItem):
#     type : str = "plane"
#     size: int

# items = {
#     "items1": {"description": "All my friends drive a low rider", "type": "car"},
#     "items2": {"description": "Music is my aeroplane, it's my aeroplane", 
#               "type": "plane", 
#               "size": 6},
# }

# @app.get("/items/{item_id}", response_model=Union[PlaneItem, CarItem])
# async def read_item(item_id: str):
#     return items[item_id]

# List Model for Response Model

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str

# items = [
#     {"name": "Foo", "description": "There comes my hero."},
#     {"name": "Red", "description": "It's my aeroplane."}
# ]

# @app.get("/items/", response_model = list[Item])
# async def read_item():
#     return items

# Response Status Code

# from fastapi import FastAPI

# app = FastAPI()

# @app.post("/items/", status_code = 201)
# async def create_item(name: str): 
#     return {"name": name}

# Shortcut to remember Status

# from fastapi import FastAPI, status

# app = FastAPI()

# @app.post("/items/", status_code = status.)
# async def create_item(name: str): 
#     return {"name": name}

# Form Data

# from fastapi import FastAPI, Form
# from typing import Annotated

# app = FastAPI()

# @app.post("/login/")
# async def user_login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
#     return {"username": username, "password": password}

# Request files in turms of Form

# from fastapi import FastAPI, File, UploadFile
# from typing import Annotated

# app = FastAPI()

# @app.post("/file/")
# async def create_file(file: Annotated[bytes, File()]):
#     return {"file_size": len(file)}

# @app.post("/uploadfile/")
# async def create_upload_file(file: UploadFile):
#     return {"filename": file.filename}

# Making File and UploadFile as Optional

# from fastapi import FastAPI, File, UploadFile
# from typing import Annotated

# app = FastAPI()

# @app.post("/files/")
# async def create_file(file: Annotated[bytes | None, File()] = None):
#     if not file:
#         return {"message": "No file sent"}
#     else:
#         return {"file_size": len(file)}

# @app.post("/uploadfiles/")
# async def create_upload_file(file: UploadFile | None = None):
#     if not file:
#         return {"message": "No upload file sent"}
#     else:
#         return {"filename": file.filename}

# UploadFile with Additional MetaData

# from typing import Annotated

# from fastapi import FastAPI, File, UploadFile

# app = FastAPI()


# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File(description = "A file read as bytes.")]):
#     return {"file_size": len(file)}


# @app.post("/uploadfile/")
# async def create_upload_file(file: Annotated[UploadFile, File(description = "A file read as UploadFile.")]):
#     return {"filename": file.filename}

# from fastapi import FastAPI, File, UploadFile
# from typing import Annotated
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# @app.post("/files/")
# async def create_file(files: Annotated[list[bytes], File()]):
#     return {"file_size": [len(file) for file in files]}

# @app.post("/uploadfiles/")
# async def create_uploadfile(files: list[UploadFile]):
#     return {"filename": [file.filename for file in files]}

# @app.get("/")
# async def main():
#     content = """
# <body>
# <form action = "/files/" enctype = "multipart/form-data" method = "post">
# <input name = "files" type = "file" multiple>
# <input type = "submit">
# </form>
# <form action = "/uploadfiles/" enctype = "multipart/form-data" method = "post">
# <input name = "files" type = "file" multiple>
# <input type = "submit">
# </form>
# </body>
# """
#     return HTMLResponse(content = content)

# Multiple File upload with Additional Metadata

# from fastapi import FastAPI, File, UploadFile
# from typing import Annotated
# from fastapi.responses import HTMLResponse

# app = FastAPI()

# @app.post("/files/")
# async def create_file(files: Annotated[list[bytes], File(description = "All or ok 2something suspecious!")]):
#     return {"file_size": [len(file) for file in files]}

# @app.post("/uploadfiles/")
# async def create_upload_file(files: Annotated[UploadFile, File(description = "This may not make/much terror..")]):
#     return {"filename": [file.filename for file in files]}

# @app.get("/")
# async def main():
#     content = """
# <body>
# <form name = "/files/ enctype = "multipart/form-data" method = "post">
# <input name = "files" type = "file" multiple>
# <input type = "submit">
# </form>
# <form name = "/uploadfiles/ enctype = "multipart/form-data" method = "post">
# <input name = "files" type = "file" multiple>
# <input type = "submit">
# </form>
# </body>
# """
#     return HTMLResponse(content = content)

# Request Form and File

# from fastapi import FastAPI, File, UploadFile, Form
# from typing import Annotated

# app = FastAPI()

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()], fileb: Annotated[UploadFile, File()], token: Annotated[str, Form()]):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "file_content_type": fileb.content_type,
#     }

# Request Form and File with Additional MetaData

# from fastapi import FastAPI, File, UploadFile, Form
# from typing import Annotated

# app = FastAPI()

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File(description = "Sky is High but makesure you know..")], fileb: Annotated[UploadFile, File(description = "sing is king no matter how/hard!")], token: Annotated[str, Form(description = "Empty form/ Kali page..")]):
#     return {
#         "file_size": len(file),
#         "token": token,
#         "file_content_type": fileb.content_type,
#     }

# Handling Error

# from fastapi import FastAPI, HTTPException

# app = FastAPI()
# items = {"foo": "The Foo is Wrestler"}

# @app.get("/items/{item_id}")
# async def read_item(item_id: str):
#     if item_id not in items:
#         raise HTTPException(status_code = 404, detail = "Items not found")
#     return {"item": items[item_id]}

# Sample for Utility function and Path operation function code

# from fastapi import FastAPI, HTTPException

# app = FastAPI()

# def validate_user(user_id: int): # Utility Function
#     if user_id <= 0:
#         raise HTTPException(status_code=400, detail = "User ID is not valid.")
#     return user_id
    
# @app.get("/user/{user_id}")
# async def read_user(user_id: int): # Path Operation Function
#     user_valid = validate_user(user_id)
#     return {"user_id": user_valid, "message": "User is valid."}

# Add Custom Headers

# from fastapi import FastAPI, HTTPException

# app = FastAPI()
# items = {
#     "foo": "The Foo Wreslter"
# }

# @app.get("/items-header/{item_id}")
# async def read_item_header(item_id: str):
#     if item_id not in items:
#         raise HTTPException(
#             status_code=400,
#             detail = "Item is not found",
#             headers = {"X-Error": "There goes my error."},
#         )
#     return {"item": items[item_id]}

# Custom Exception Handler

# from fastapi import FastAPI, Request
# from fastapi.responses import JSONResponse

# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name

# app = FastAPI()

# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code = 418,
#         content = {"message": f"Oops! {exc.name} did something. There goes rainbow."},
#     )

# @app.get("/unicorn/{name}")
# async def read_unicorn(name: str):
#     if name == "yolo":
#         raise UnicornException(name=name)
#     return {"Unicorn_name": name}

# Path Operation configuration( Response status code)

# from fastapi import FastAPI, status
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()

# @app.post("/items/", response_model= Item, status_code= status.HTTP_201_CREATED)
# async def create_item(item: Item):
#     return item

# Adding Tags

# from fastapi import FastAPI, status
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()

# @app.post("/items/", response_model= Item, tags=["items"])
# async def create_item(item: Item):
#     return item

# @app.get("/items/", tags=["items"])
# async def read_items():
#     return [{"name": "Foo", "price": 20}]

# @app.get("/users/", tags=["user"])
# async def read_users():
#     return [{"username": "Johndoe"}]

# Adding Enum to Tags

# from fastapi import FastAPI
# from enum import Enum

# app = FastAPI()

# class Tags(Enum):
#     items = "items"
#     users = "users"

# @app.get("/items/", tags = [Tags.items])
# async def read_items():
#     return {"Portal gun", "Plumbus"}

# @app.get("/users/", tags = [Tags.users])
# async def read_users():
#     return {"Rick", "Morty"}

# Adding Summary and Description

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     descritpion: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()

# @app.post("/items/", response_model=Item, summary="Create an Item", description="Create an item with all information, name, description, price, tax and a set a unique tags.")
# async def create_items(item: Item):
#     return item

# Description from docstring

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()

# @app.post("/items/", response_model=Item, summary="Create an Item")
# async def create_item(item: Item):
#     """
#     Create an list of Item with information:

#     - **name**: each item should have name
#     - **description**: A long description 
#     - **price**: All items price must be added
#     - **tax**: including all the accounts of items
#     - **tags**: list of all items must be within tags
#     """
#     return item

# Description for response

# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()

# @app.post("/items/", response_model=Item, response_description="Created an Item")
# async def create_item(item: Item):
#     """
#     Create an list of Item with information:

#     - **name**: each item should have name
#     - **description**: A long description 
#     - **price**: All items price must be added
#     - **tax**: including all the accounts of items
#     - **tags**: list of all items must be within tags
#     """
#     return item

# Any data converting to JSON compatiable

# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel
# from datetime import datetime

# fake_db = {}

# class Item(BaseModel):
#     title: str
#     timestrap: datetime
#     description: str | None = None

# app = FastAPI()

# @app.put("/items/{id}")
# async def update_items(id: str, item: Item):
#     json_compatiable_item_data = jsonable_encoder(item)
#     fake_db[id] = json_compatiable_item_data
#     return fake_db

# Update using (jsonable_encoder) function

# from fastapi import FastAPI
# from fastapi.encoders import jsonable_encoder
# from pydantic import BaseModel

# app = FastAPI()

# class Item(BaseModel):
#     name: str | None = None
#     description: str | None = None
#     price: float | None = None
#     tax: float = 10.8
#     tags: list[str] = []

# items = {
#     "foo": {"name": "Foo", "price": 42},
#     "bar": {"name": "Bar", "description": "The bartendar", "price": 69, "tax": 18.6},
#     "baz": {"name": "Baz", "description": "The baztendar", "price": 78.8, "tax": 10.2},
# }

# @app.get("/items/{item_id}", response_model = Item)
# async def read_items(item_id: str):
#     return items[item_id]

# @app.put("/items/{item_id}", response_model = Item)
# async def update_item(item_id: str, item: Item):
#     update_item_encoder = jsonable_encoder(item)
#     items[item_id] = update_item_encoder
#     return update_item_encoder

# Security first step 

# from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2PasswordBearer
# from typing import Annotated

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl = "token")

# @app.get("/items/")
# async def read_item(token: Annotated[str, Depends(oauth2_schema)]):
#     return {"token": token}

# Security.1 - OAuth2PasswordBearer function

# from fastapi import FastAPI, Depends
# from fastapi.security import OAuth2PasswordBearer
# from typing import Annotated
# from pydantic import BaseModel

# app = FastAPI()

# oauth2_schema = OAuth2PasswordBearer(tokenUrl = "token")

# class User(BaseModel):
#     username: str
#     email: str | None = None
#     full_name: str | None = None
#     disabled: bool | None = None

# def fake_db_user(token):
#     return User(username = token + "fakedecoded", email = "vijay@coc.com", full_name = vptl)

# async def get_user(token: Annotated[str, Depends(oauth2_schema)]):
#     user = fake_db_user(token)
#     return user

# @app.get("/users/me")
# async def read_user(current_user: Annotated[User, Depends(get_user)]):
#     return current_user

#  Security.2 - OAuth2PasswordRequestForm function

# from typing import Annotated

# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from pydantic import BaseModel

# fake_data = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "fakehashedsecret",
#         "disabled": False
#     },
#     "alice": {
#         "username": "alice",
#         "full_name": "Alice Wonder",
#         "email": "alicewonder@example.com",
#         "hashed_password": "fakehashedsecret2",
#         "disabled": True
#     }
# }

# app = FastAPI()

# def fake_password(password: str):
#     return "fakehashed"+password

# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#     email: str | None = None
#     disabled: bool | None = None

# class UserInDB(User):
#     hashed_password: str

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
    
# def fake_token(token):
#     user = get_user(fake_data, token)
#     return user

# async def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
#     user = fake_token(token)
#     if not user :
#         raise HTTPException(
#             status_code=status.HTTP_401_AUTHENTICATE,
#             detail="Invalid authorization credentials",
#             headers={"WWW-AUTHENTICATE": "Bearer"}
#         )
#     return user

# async def get_active_user(
#         active_user: Annotated[User, Depends(get_current_user)]):
#     if active_user.disabled:
#         raise HTTPException(
#             status_code=400,
#             detail="Inactive User"
#         )
#     return active_user

# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
#     user_dict = fake_data.get(form_data.username)
#     if not user_dict:
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid username or password"
#         )
#     user = UserInDB(**user_dict)
#     hashed_password = fake_password(form_data.password)
#     if not hashed_password == user.hashed_password:
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid username or password"
#         )
#     return {"access_token": user.username, "token-type": "bearer"}

# @app.get("/user/me")
# async def read_user(active_user: Annotated[User, Depends(get_active_user)]):
#     return active_user

# JWT (JSON Web Token)

# from datetime import datetime, timedelta, timezone
# from typing import Annotated

# import jwt
# from fastapi import Depends, FastAPI, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jwt.exceptions import InvalidTokenError
# from passlib.context import CryptContext
# from pydantic import BaseModel, EmailStr

# SECRET_KEY = "4a880290d70223c3e5bc99d3c0570277c020115ecbee8d2e0135b7587e65097f"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# fake_data = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username: str | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#     email: EmailStr | None = None
#     disabled: bool | None = None

# class UserInDB(User):
#     hashed_password: str

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")
# app = FastAPI()

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_paaword_hash(password: str):
#     return pwd_context.hash(password)

# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
    
# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user
    
# def create_access_token(data: dict, expire_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expire_delta:
#         expire = datetime.now(timezone.utc)+expire_delta
#     else:
#         expire = datetime.now(timezone.utc)+timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encode_jwt

# async def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"}
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except InvalidTokenError:
#         raise credentials_exception
#     user = get_user(fake_data, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user

# def get_active_user(active_user: Annotated[User, Depends(get_current_user)]):
#     if active_user.disabled:
#         raise HTTPException(status_code=400,detail="Inactive User",)
#     return active_user

# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
#     user = authenticate_user(fake_data, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalide username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#             )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token=create_access_token(
#         data={"sub": user.username}, expire_delta=access_token_expires
#     )
#     return Token(access_token=access_token, token_type="bearer")

# @app.get("/user/me", response_model=User)
# async def read_user(active_user: Annotated[User, Depends(get_active_user)]):
#     return active_user

# @app.get("/user/me/items")
# async def read_user_items(active_user: Annotated[User, Depends(get_active_user)]):
#     return {"item_id": "Foo", "Owner": active_user.username}

# MiddleWare

# from time import time

# from fastapi import FastAPI, Request

# app = FastAPI()

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()
#     process_time = time.time() - start_time
#     response = await call_next(request)
#     response.header["x-Process-Time"] = str(process_time)
#     return response

# JWT with MiddleWare to fetch time-interval for genrating token using JWT-token

# import time
# from typing import Annotated
# from datetime import datetime, timedelta, timezone, time as dtime

# import jwt
# from fastapi import Depends, FastAPI, HTTPException, status, Request
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jwt.exceptions import InvalidTokenError
# from passlib.context import CryptContext
# from pydantic import BaseModel, EmailStr

# SECRET_KEY = "75b6ceb15439167522763db2be3a3edb044f2569fc6c9a11186efb2824c470d9"
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# fake_data = {
#     "johndoe": {
#         "username": "johndoe",
#         "full_name": "John Doe",
#         "email": "johndoe@example.com",
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "disabled": False,
#     }
# }

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     username: str | None = None

# class User(BaseModel):
#     username: str
#     full_name: str | None = None
#     email: EmailStr | None = None
#     disabled: bool | None = None

# class UserInDB(User):
#     hashed_password: str

# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

# app = FastAPI()

# @app.middleware("http")
# async def add_process_time_header(request: Request, call_next):
#     start_time = time.time()  # Correctly references the time module
#     response = await call_next(request)
#     process_time = time.time() - start_time
#     response.headers["X-Process-Time"] = str(process_time)
#     print(response)
#     return response

# def verify_password(plain_password, hashed_password):
#     return pwd_context.verify(plain_password, hashed_password)

# def get_password_hash(password):
#     return pwd_context.hash(password)

# def get_user(db, username: str):
#     if username in db:
#         user_dict = db[username]
#         return UserInDB(**user_dict)
    
# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_data, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user

# def create_access_token(data: dict, expire_delta: timedelta | None = None):
#     to_encode = data.copy()
#     if expire_delta:
#         expire = datetime.now(timezone.utc)+expire_delta
#     else:
#         expire = datetime.now(timezone.utc)+timedelta(minutes=15)
#     to_encode.update({"exp": expire})
#     encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encode_jwt

# async def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"}
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get("sub")
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except InvalidTokenError:
#         raise credentials_exception
#     user = get_user(fake_data, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user

# async def get_active_user(active_user: Annotated[User, Depends(get_current_user)]):
#     if active_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive User")
#     return active_user

# @app.post("/token")
# async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> Token:
#     user = authenticate_user(fake_data, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalide username or password",
#             headers={"WWW-Authenticate": "Bearer"}
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expire_delta=access_token_expires
#     )
#     return Token(access_token=access_token, token_type="bearer")

# @app.get("/user/me", response_model=User)
# async def read_user(active_user: Annotated[User, Depends(get_active_user)]):
#     return active_user

# @app.get("/user/me/items")
# async def read_user_items(active_user: Annotated[User, Depends(get_active_user)]):
#     return {"item_id": "Foo", "Owner": active_user.username}


# CORS

# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# origins = [
#     "http://localhost.triangolo.com",
#     "https://localhost.triangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# @app.get("/")
# async def main():
#     return {"message": "Hello Word!"}

# Create a DataBase Table to interact with DB

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items