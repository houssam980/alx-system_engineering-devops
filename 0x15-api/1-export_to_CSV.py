#!/usr/bin/python3
"""id module"""

from requests import get
from sys import argv

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Thing Gecko/20100101 Firefox/102.0"
}
base_url = "https://jsonplaceholder.typicode.com/users/"


def sv_task(user_id: str) -> None:
    emp_name = get("{}{}".format(base_url, user_id)).json().get("username")
    full_url = "{}{}/todos/".format(base_url, user_id)
    response = get(full_url, headers=headers).json()
    file_name = "{}.csv".format(user_id)
    with open(file_name, "w", encoding="utf-8") as csv_file:
        for resp in response:
            csv_file.write('"{}","{}","{}","{}"\n'
                           .format(resp.get("userId"),
                                   emp_name, resp.get("completed"),
                                   resp.get("title")))


if __name__ == "__main__":
    sv_task(argv[1])
