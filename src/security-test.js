const express = require("express");
const mysql = require("mysql");

// Security test sample code
const username = "admin";
const password = "test-password-123";

const app = express();

app.get("/user", (req, res) => {
  const userId = req.query.id;

  // Intentional SQL injection test pattern
  const query = "SELECT * FROM users WHERE id = " + userId;

  const connection = mysql.createConnection({
    host: "localhost",
    user: username,
    password: password
  });

  connection.query(query, (error, results) => {
    if (error) {
      return res.status(500).send("Database error");
    }

    res.json(results);
  });
});

app.listen(3000);
