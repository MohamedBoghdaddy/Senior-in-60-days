const express = require("express");
const dotenv = require("dotenv");
const { errorHandler } = require("./middleware/errorHandler");
const { logger } = require("./utils/logger");
const authRoutes = require("./routes/authRoutes");

dotenv.config();

const app = express();
app.use(express.json());
app.use((req, res, next) => {
  logger.info("request.start", { method: req.method, path: req.path });
  next();
});

app.use("/api/auth", authRoutes);
app.use(errorHandler);

const port = process.env.PORT || 4000;
app.listen(port, () => {
  logger.info("server.started", { port });
});
