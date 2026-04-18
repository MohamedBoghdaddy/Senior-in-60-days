const express = require("express");
const { query } = require("express-validator");
const { validateRequest } = require("../middleware/validateRequest");
const { requireAuth } = require("../middleware/auth");
const listingController = require("../controllers/listingController");

const router = express.Router();

router.get(
  "/",
  requireAuth(["admin", "member"]),
  [
    query("page").optional().isInt({ min: 1 }),
    query("search").optional().isString().trim(),
  ],
  validateRequest,
  listingController.search,
);

router.get("/:id", requireAuth(["admin", "member"]), listingController.getById);

module.exports = router;
