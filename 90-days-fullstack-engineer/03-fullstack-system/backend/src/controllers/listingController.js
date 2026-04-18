const listingService = require("../services/listingService");

exports.search = async (req, res, next) => {
  try {
    const result = await listingService.search(req.query);
    res.json(result);
  } catch (error) {
    next(error);
  }
};

exports.getById = async (req, res, next) => {
  try {
    const result = await listingService.getById(req.params.id);
    res.json(result);
  } catch (error) {
    next(error);
  }
};
