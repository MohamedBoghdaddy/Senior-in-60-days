const express = require("express");
const { body } = require("express-validator");
const { validateRequest } = require("../middleware/validateRequest");
const authController = require("../controllers/authController");

const router = express.Router();

router.post(
  "/login",
  [body("email").isEmail(), body("password").isString().isLength({ min: 8 })],
  validateRequest,
  authController.login,
);

router.post(
  "/refresh",
  [body("refreshToken").isString().notEmpty()],
  validateRequest,
  authController.refreshToken,
);

module.exports = router;
