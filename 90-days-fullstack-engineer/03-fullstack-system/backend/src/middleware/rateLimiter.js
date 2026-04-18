const { redis } = require("../config/redis");

module.exports = async (req, res, next) => {
  const limit = Number(process.env.RATE_LIMIT || 100);
  const key = `rate:${req.ip}`;
  const current = await redis.incr(key);
  if (current === 1) {
    await redis.expire(key, 60);
  }
  if (current > limit) {
    return res
      .status(429)
      .json({ code: "RATE_LIMIT_EXCEEDED", message: "Too many requests" });
  }
  next();
};
