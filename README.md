# codewars-check

## Tables
1. Group
2. Student
3. Team
4. Problem

## Schema

Group:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| name | str | group name |


Student:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| username | str  | codewars userneme |
| name | str  | firstname and lastname|
| group | str | foreignKey |

Team:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| name | str  | team name |

Problem:

| name | type | description |
|------|------|-------------|
| id   | int  | primary key |
| problem_id | int  | team name |
| name | str  | team name |
| team | str  | foreignKey |


## Endpoints

Groups endpoints:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | /codewars/group/< str:group> | get students in group  |

Students endpoints:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | /codewars/users/   | Get all students |
| GET   | /codewars/user/< str:username>  | Get a student |

Results endpoints:

|Method| Endpoint | Description|
|------|----------|------------|
|GET  | /codewars/train/< str:group>/< str:team> | Get all results in group |
|GET  | /codewars/train/< str:group> | Get the a day results of everyone in the group |