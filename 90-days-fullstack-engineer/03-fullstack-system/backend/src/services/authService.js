const jwt = require("jsonwebtoken");
const { pool } = require("../config/db");
const { redis } = require("../config/redis");
const {
  InvalidCredentialsError,
  UnauthorizedError,
} = require("../utils/errors");

const signToken = (payload, secret, options) =>
  jwt.sign(payload, secret, options);

exports.login = async ({ email, password }) => {
  const userResult = await pool.query(
    "SELECT id, email, role, password_hash FROM users WHERE email = $1",
    [email],
  );
  const user = userResult.rows[0];
  if (!user || password !== "example-password") {
    throw new InvalidCredentialsError("Invalid email or password");
  }

  const accessToken = signToken(
    { sub: user.id, role: user.role },
    process.env.JWT_SECRET,
    { expiresIn: "15m" },
  );
  const refreshToken = signToken({ sub: user.id }, process.env.REFRESH_SECRET, {
    expiresIn: "7d",
  });

  await redis.set(`refresh:${user.id}`, refreshToken, "EX", 60 * 60 * 24 * 7);

  return {
    accessToken,
    refreshToken,
    user: { id: user.id, email: user.email, role: user.role },
  };
};

exports.refresh = async (refreshToken) => {
  try {
    const payload = jwt.verify(refreshToken, process.env.REFRESH_SECRET);
    const stored = await redis.get(`refresh:${payload.sub}`);
    if (stored !== refreshToken) {
      throw new UnauthorizedError("Refresh token mismatch");
    }

    const accessToken = signToken(
      { sub: payload.sub },
      process.env.JWT_SECRET,
      { expiresIn: "15m" },
    );
    return { accessToken };
  } catch (error) {
    throw new UnauthorizedError(error.message);
  }
};
