from datetime import datetime

from data_types import Todo, Action
from db import get_data, add_data, remove_data, get_id, update_data
from forms import create_form, update_form
from utils import get_choice, get_item_by_user_input


# Service
def get_todo_list():
    for _id, todo in enumerate(get_data()):
        print(f'{_id + 1}. {todo.name} - {todo.is_finished}')


# Service
def select_item(console_text: str) -> Todo:
    get_todo_list()

    item_number = get_choice(console_text, get_data())
    item = get_item_by_user_input(item_number, get_data())
    return item


def create_todo():
    data = create_form.get_data()
    print(data)
    todo = Todo(id=get_id(), created_at=datetime.now(), **data)
    add_data(todo)


def delete_todo():
    item_to_delete = select_item("Enter item number you want to delete: ")
    remove_data(item_to_delete)


def update_todo():
    item_to_update = select_item("Enter item number you want to update: ")

    data = update_form.get_data()
    print(data)
    item_to_update.__dict__.update(data)
    update_data(item_to_update)


def get_todo():
    item_to_show = select_item("Enter item number you want to see: ")
    print(item_to_show)


# Views
get_list_action = Action(name='Get list', action=get_todo_list)
get_todo_action = Action(name='Get todo', action=get_todo)
create_todo_action = Action(name='Create todo', action=create_todo)
update_todo_action = Action(name='Update todo', action=update_todo)
delete_todo_action = Action(name='Delete todo', action=delete_todo)