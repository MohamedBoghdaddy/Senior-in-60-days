const { logger } = require("../utils/logger");

exports.errorHandler = (err, req, res, next) => {
  logger.error("request.error", {
    code: err.code || "INTERNAL_ERROR",
    message: err.message,
    path: req.path,
  });
  const status = err.statusCode || 500;
  res.status(status).json({
    code: err.code || "INTERNAL_ERROR",
    message: err.publicMessage || "Internal server error",
    details:
      process.env.NODE_ENV === "development"
        ? err.details || err.stack
        : undefined,
  });
};
