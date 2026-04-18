const authService = require("../services/authService");

exports.login = async (req, res, next) => {
  try {
    const { user, accessToken, refreshToken } = await authService.authenticate(
      req.body,
    );
    res.status(200).json({ user, accessToken, refreshToken });
  } catch (error) {
    next(error);
  }
};

exports.refreshToken = async (req, res, next) => {
  try {
    const tokens = await authService.refresh(req.body.refreshToken);
    res.status(200).json(tokens);
  } catch (error) {
    next(error);
  }
};
