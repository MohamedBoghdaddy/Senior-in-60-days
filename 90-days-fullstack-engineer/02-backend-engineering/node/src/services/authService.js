const jwt = require("jsonwebtoken");
const config = require("../config");
const userRepository = require("../repositories/userRepository");
const {
  InvalidCredentialsError,
  TokenExpiredError,
} = require("../utils/errors");

const signToken = (payload, secret, expiresIn) =>
  jwt.sign(payload, secret, { expiresIn });

exports.authenticate = async ({ email, password }) => {
  const user = await userRepository.findByEmail(email);
  if (!user || !(await userRepository.verifyPassword(user, password))) {
    throw new InvalidCredentialsError("Invalid email or password");
  }

  const accessToken = signToken(
    { sub: user.id, role: user.role },
    config.jwtSecret,
    config.tokenExpiry,
  );
  const refreshToken = signToken(
    { sub: user.id },
    config.refreshSecret,
    config.refreshExpiry,
  );

  await userRepository.saveRefreshToken(user.id, refreshToken);

  return {
    user: { id: user.id, email: user.email, role: user.role },
    accessToken,
    refreshToken,
  };
};

exports.refresh = async (token) => {
  try {
    const payload = jwt.verify(token, config.refreshSecret);
    const user = await userRepository.findById(payload.sub);
    if (!user || user.refreshToken !== token) {
      throw new InvalidCredentialsError("Refresh token is invalid");
    }

    const accessToken = signToken(
      { sub: user.id, role: user.role },
      config.jwtSecret,
      config.tokenExpiry,
    );
    return { accessToken };
  } catch (error) {
    if (error.name === "TokenExpiredError") {
      throw new TokenExpiredError("Refresh token expired");
    }
    throw error;
  }
};
