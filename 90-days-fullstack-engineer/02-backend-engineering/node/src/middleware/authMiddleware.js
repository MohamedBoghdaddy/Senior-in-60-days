const jwt = require("jsonwebtoken");
const config = require("../config");
const { UnauthorizedError, ForbiddenError } = require("../utils/errors");

exports.requireAuth =
  (roles = []) =>
  (req, res, next) => {
    const authHeader = req.headers.authorization;
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      throw new UnauthorizedError("Missing or invalid authorization header");
    }

    const token = authHeader.replace("Bearer ", "");
    try {
      const payload = jwt.verify(token, config.jwtSecret);
      req.user = payload;
      if (roles.length && !roles.includes(payload.role)) {
        throw new ForbiddenError(
          "User does not have permission for this operation",
        );
      }
      next();
    } catch (error) {
      if (error.name === "TokenExpiredError") {
        throw new UnauthorizedError("Access token expired");
      }
      next(error);
    }
  };
