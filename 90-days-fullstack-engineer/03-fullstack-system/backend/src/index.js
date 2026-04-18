const express = require("express");
const dotenv = require("dotenv");
const { errorHandler } = require("./middleware/errorHandler");
const { logger } = require("./utils/logger");
const listingRoutes = require("./routes/listings");
const authRoutes = require("./routes/auth");
const { initializeQueues } = require("./jobs/queue");

dotenv.config();

const app = express();
app.use(express.json());
app.use((req, res, next) => {
  logger.info("request.received", { method: req.method, path: req.path });
  next();
});

app.use("/api/auth", authRoutes);
app.use("/api/listings", listingRoutes);
app.use(errorHandler);

initializeQueues();

const port = process.env.PORT || 5000;
app.listen(port, () => {
  logger.info("backend.started", { port });
});
