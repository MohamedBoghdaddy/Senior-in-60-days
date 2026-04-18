const jwt = require("jsonwebtoken");
const { UnauthorizedError, ForbiddenError } = require("../utils/errors");

exports.requireAuth =
  (roles = []) =>
  (req, res, next) => {
    const authHeader = req.headers.authorization;
    if (!authHeader || !authHeader.startsWith("Bearer ")) {
      return next(new UnauthorizedError("Authorization header missing"));
    }

    const token = authHeader.replace("Bearer ", "");
    try {
      const payload = jwt.verify(token, process.env.JWT_SECRET);
      req.user = payload;
      if (roles.length && !roles.includes(payload.role)) {
        throw new ForbiddenError("Insufficient permissions");
      }
      next();
    } catch (error) {
      return next(new UnauthorizedError(error.message));
    }
  };
