const { logger } = require("../utils/logger");

exports.errorHandler = (err, req, res, next) => {
  logger.error("request.error", { message: err.message, stack: err.stack });

  const status = err.statusCode || 500;
  const response = {
    code: err.code || "INTERNAL_SERVER_ERROR",
    message: err.publicMessage || "An unexpected error occurred.",
  };
  if (process.env.NODE_ENV === "development") {
    response.details = err.details || null;
  }

  res.status(status).json(response);
};
