#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests as rq
from fastapi import FastAPI, Form, Response, Request


from random import seed
from random import randint

# seed(1)


app = FastAPI()

@app.get("/image")
async def returnTemplate():
    value = randint(0, 800)
    respone = rq.get(f'https://picsum.photos/id/{ value }/info')

    data = respone.json()
    img = data.get('download_url')
    width = data.get('width')
    height = data.get('height')

    page = f'''

    <img src = "{ img }" width="1200" height="800"></img> 
    
    '''

    # page = content.readTemplate()
    # data = {
    #     'content': response
    # }
    return Response(content=str(page), media_type="text/html")
