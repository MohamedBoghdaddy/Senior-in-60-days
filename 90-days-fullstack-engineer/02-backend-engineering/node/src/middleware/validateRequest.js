const { validationResult } = require("express-validator");

exports.validateRequest = (req, res, next) => {
  const errors = validationResult(req);
  if (!errors.isEmpty()) {
    return res.status(400).json({
      code: "VALIDATION_ERROR",
      message: "Request payload validation failed",
      details: errors
        .array()
        .map((error) => ({ field: error.param, error: error.msg })),
    });
  }
  next();
};
