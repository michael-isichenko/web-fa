from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)
templates = Jinja2Templates(directory="static")

@app.get('/url')
def get_url(request: Request):
    return request.url

@app.get('/', response_class=HTMLResponse)
async def serve_page(request: Request):
    url = str(request.url)
    base_url = url[0:-1]
    return templates.TemplateResponse('index.html',
                                      context={'request': request, 'base_url': base_url})
