import express from 'express';

const app = express();

app.use(express.static('public'));

app.use(express.urlencoded({ extended: true }));

app.use(express.json());

app.get("/users", async (req, res) => {
    const limit = +req.query.limit || 10;
    const response = await fetch(`https://jsonplaceholder.typicode.com/users?_limit=${limit}`);
    const users = await response.json();
    res.send(`
        <h2>Users</h2>
        <ul class="list-group">
            ${users.map((user) => `<li class="list-group-item">${user.name}</li>`).join('')}
        </ul>
    `);
});

app.listen(3000, () => {
    console.log("Server is running on port: 3000");
});

// document.getElementById('showListButton').addEventListener('click', function () {
//     var listContainer = document.getElementById('showListButton');
//     if (listContainer.style.display === 'none') {
//         listContainer.style.display = 'block'; // or 'inline' or 'inline-block' depending on your styling
//     } else {
//         listContainer.style.display = 'none';
//     }
// });