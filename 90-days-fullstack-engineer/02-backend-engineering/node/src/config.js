const dotenv = require("dotenv");

dotenv.config();

module.exports = {
  port: process.env.PORT || 4000,
  jwtSecret: process.env.JWT_SECRET,
  refreshSecret: process.env.JWT_REFRESH_SECRET,
  tokenExpiry: process.env.TOKEN_EXPIRATION || "15m",
  refreshExpiry: process.env.REFRESH_TOKEN_EXPIRATION || "7d",
  databaseUrl: process.env.DATABASE_URL,
  mongoUri: process.env.MONGO_URI,
  redisUrl: process.env.REDIS_URL,
  logLevel: process.env.LOG_LEVEL || "info",
};
