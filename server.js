const express = require("express");
const path = require("path");
const http = require("http");
const bodyParser = require("body-parser");

const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));

app.use(express.static(path.join(__dirname, "assets")));

app.get("/", (req, res) => {
  console.log("requested");
  res.sendFile(path.join(__dirname, "/assets/index.html"));
});

/**
 * Get port from environment and store in Express.
 */
const port = "2901";
app.set("port", port);

/**
 * Create HTTP server.
 */
const server = http.createServer(app);

/**
 * Listen on provided port, on all network interfaces.
 */
server.listen(port, () => console.log(`API running on localhost:${port}`));
