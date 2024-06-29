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
| Team | str  | foreignKey |


## Endpoints

Groups endpoints:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET | /codewars/group/ <group> | get students in group  |

Students endpoints:

| Method | Endpoint | Description |
| ------ | -------- | ----------- |
| GET    | /codewars/users/   | Get all students |
| GET   | /codewars/user/ <username>  | Get a student |

Results endpoints:

|Method| Endpoint | Description|
|------|----------|------------|
|GET  | /codewars/train/ <group>/ <team> | Get all results in group |
|GET  | /codewars/train/ <group> | Get the a day results of everyone in the group |