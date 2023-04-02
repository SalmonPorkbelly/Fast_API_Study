from fastapi import APIRouter

router = APIRouter()

todo_list = []


@router.post('/todo')
async def add_todo(todo: dict) -> dict:
    todo_list.append(todo)
    return {
        'message': 'this is routing test'
    }


@router.get('/todo')
async def retrieve_todos() -> dict:
    return {
        'todos': todo_list
    }