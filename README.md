# Todo-project-backend

## ROUTES TO IMPLEMENT (ACCOUNT)
| METHOD   |                        ROUTE | FUNCTIONALITY                    |ACCESS|
|----------|-----------------------------:|----------------------------------| ------------- |
| *POST*   |      ```/account/profile/``` | _Register new user_              | _All users_|
| *POST*   |        ```/account/login/``` | _Login user_                     |_All users_|
| *GET*    |      ```/account/profile/``` | _Search accounts_                |_All users_|
| *GET*    | ```/account/profile/{id}/``` | _Account profile read_           | _All users_|
| *PUT*    |            ```/account/profile/{id}/``` | _Account profile update_         |_All users_|
| *PATCH*  |                 ```/account/profile/{id}/``` | _Account profile partial update_ |_All users_|
| *DELETE* |          ```/account/profile/{id}/``` | _Account profile delete_         | _All users_|

## ROUTES TO IMPLEMENT (TODO)
| METHOD   |                        ROUTE | FUNCTIONALITY     |ACCESS|
|----------|-----------------------------:|-------------------| ------------- |
| *GET*    |             ```/todo/api/``` | _Todo api list_   | _All users_|
| *POST*   |             ```/todo/api/``` | _Todo api create_ |_All users_|
| *GET*    |   ```/todo/api/{todo_id}/``` | _Todo api read_   |_All users_|
| *PUT*    | ```/todo/api/{todo_id}/``` | _Todo api update_ | _All users_|
| *DELETE* | ```/todo/api/{todo_id}/``` | _Todo api delete_ | _All users_|



