# factory-test

Creating polls for users

# installation

1. clone project
1. create and activate virtual environment if needed
1. run `python manage.py migrate`
1. run `python manage.py createsuperuser`
1. run `python manage.py runserver`
1. go to `http://127.0.0.1:8080/polls`


# known problems

1. bad urls?
1. generate anon user ids on server side
1. multiple answers for one question

# poll urls

1. GET /polls/polls  list polls
1. POST /polls/polls create poll
`{"title": "test poll 1", "start_dt": "2024-06-24 10:00:00", "end_dt": "2024-06-24 14:00:00", "descr": "test poll 1 descr"}`
1. GET /polls/polls/1  retrieve poll
1. PUT /polls/polls/1 update poll
`{"title": "test poll 1", "start_dt": "2024-06-24 10:00:00", "end_dt": "2024-06-24 14:00:00", "descr": "test poll 1 descr"}`
1. DELETE /polls/polls/1 delete poll

# question urls

1. GET /polls/questions/  list questions
1. POST /polls/questions/ create question
`{"text": "test question 1", "type": "text", "poll": 1}`
1. GET /polls/questions/1  retrieve question
1. PUT /polls/questions/1 update question
`{"text": "test question 1 for poll 1", "type": "text", "poll": 1}`
1. DELETE /polls/questions/1 delete question

# question choices urls

1. GET /polls/questions-choices/  list questions choices
1. POST /polls/questions-choices/ create questions choice
`{"text": "test choice 1", "question": 1}`
1. GET /polls/questions-choices/1  retrieve questions choice
1. PUT /polls/questions-choices/1 update questions choice
`{"text": "test choice 1 for question 1", "question": 1}`
1. DELETE /polls/questions-choices/1 delete questions choice

# users polls urls

1. GET /polls/users/  list user's polls
1. GET /polls/users/?uid=user_id  list anon user's polls
1. POST /polls/users/ create user's poll
`{"user_id": 1, "poll": 1}`

# users answers urls

1. POST /polls/answers/ create answer
`{"text": "test answer", "user_poll": 1, "question": 1, "chosen": null}`
1. POST /polls/answers/?uid=user_id create answer for anon user
`{"text": "test answer", "user_poll": 1, "question": 1, "chosen": null}`
