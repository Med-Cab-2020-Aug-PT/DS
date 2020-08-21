from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from app.api import predict

app = FastAPI(
    title='Med Cabinet API',
    description='',
    version='0.1',
    docs_url='/',
)

app.include_router(predict.router)
app.include_router(viz.router)

# @app.get('/users/{strain_by_name}')
# def get_strain_info(strain_by_name: str):
#    return {'strain_by_name': strain_by_name}



app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

if __name__ == '__main__':
    uvicorn.run(app)
