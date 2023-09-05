# code-challenge-phase3-wk3


This is the README file for the code challenge phase 3 week 3. In this challenge, you will be building a simple web application that allows users to create and manage a todo list.

## Step 1: Create a new project

First, you need to create a new project directory and initialize a new Git repository. You can do this by running the following commands in your terminal:

```
mkdir code-challenge-phase3-wk3
cd code-challenge-phase3-wk3
git init
```

## Step 2: Install dependencies

Next, you need to install the dependencies for your project. You can do this by running the following command in your terminal:

```
npm install express ejs
```

## Step 3: Create the server

Now, you need to create the server for your web application. You can do this by creating a new file called `server.js` and adding the following code:

```javascript
const express = require('express');
const app = express();

// Set the view engine to EJS
app.set('view engine', 'ejs');

// Define the home route
app.get('/', (req, res) => {
  res.render('index');
});

// Define the add todo route
app.post('/add-todo', (req, res) => {
  // Get the todo text from the request body
  const todoText = req.body.todoText;

  // Add the todo to the database
  // ...

  // Redirect to the home page
  res.redirect('/');
});

// Define the delete todo route
app.post('/delete-todo', (req, res) => {
  // Get the todo id from the request body
  const todoId = req.body.todoId;

  // Delete the todo from the database
  // ...

  // Redirect to the home page
  res.redirect('/');
});

// Start the server
app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
```

## Step 4: Create the views

Next, you need to create the views for your web application. You can do this by creating a new directory called `views` and adding the following files:

* `index.ejs


## Contribution 
Thank you for considering contributing to our project! We welcome contributions of all kinds, including bug reports, feature requests, documentation updates, and code contributions.

To contribute to the project, please follow these steps:

Fork the repository.
Make your changes.
Submit a pull request.

## License
MIT License 
Copyright (c) [2023] [Austin Mbogo]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Author
This project was created by Austin Mbogo. You can contact me at (austin.mbogo@student.moringaschool.com).

## Support
For help, you can contact (austin.mbogo@student.moringaschool.com).