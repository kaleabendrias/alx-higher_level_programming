#!/usr/bin/node
const request = require('request')
url = process.argv[2]

request.get(url, (err, res, body) => {
    if (!err && res.statusCode === 200) {
        const todos = JSON.parse(body)
        const completed_tasks = {}
        todos.forEach(todo => {
            if (todo.completed) {
                if (completed_tasks[todo.userId]) {
                    completed_tasks[todo.userId] += 1;
                }
                else {
                    completed_tasks[todo.userId] = 1;
                }
            }
        });
        console.log(completed_tasks);
    }
    else {
        console.log(err)
    }
})