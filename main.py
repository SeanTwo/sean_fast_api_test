from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Hello World!'}

@app.get('/health')
def health_check():
    return {'status' : 'healthy'}

@app.get('/add/{a}/{b}')
def add_numbers(a: int, b: int):
    return {'result' : a + b}

@app.get('/subtract/{a}/{b}')
def subtract_numbers(a: int, b: int):
    return {'result' : a - b}
