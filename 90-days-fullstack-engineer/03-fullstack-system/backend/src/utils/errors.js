class ApplicationError extends Error {
  constructor(
    message,
    statusCode = 500,
    code = "APPLICATION_ERROR",
    publicMessage = "A server error occurred",
    details = null,
  ) {
    super(message);
    this.statusCode = statusCode;
    this.code = code;
    this.publicMessage = publicMessage;
    this.details = details;
  }
}

class InvalidCredentialsError extends ApplicationError {
  constructor(message = "Invalid credentials") {
    super(message, 401, "INVALID_CREDENTIALS", "Invalid email or password");
  }
}

class UnauthorizedError extends ApplicationError {
  constructor(message = "Unauthorized") {
    super(message, 401, "UNAUTHORIZED", "Authentication required");
  }
}

class ForbiddenError extends ApplicationError {
  constructor(message = "Forbidden") {
    super(message, 403, "FORBIDDEN", "Insufficient permissions");
  }
}

module.exports = {
  ApplicationError,
  InvalidCredentialsError,
  UnauthorizedError,
  ForbiddenError,
};
