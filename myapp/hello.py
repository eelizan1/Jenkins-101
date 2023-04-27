import fire
import requests

def hello(name="World"):
    response = requests.get(f"https://jsonplaceholder.typicode.com/users?username={name}")

    if response.status_code == 200:
        user_data = response.json()
        if user_data:
            return f"Hello, {user_data[0]['name']}!"
        else:
            return f"Hello {name}! User not found in the API."
    else:
        return f"Hello {name}! Error while calling the API: {response.status_code}"

def todo(): 
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')

    if response.status_code == 200:
        json_data = response.json()
        print(json_data)
    else:
        print(f"Error while fetching data: {response.status_code}")

if __name__ == '__main__':
    fire.Fire(todo)
