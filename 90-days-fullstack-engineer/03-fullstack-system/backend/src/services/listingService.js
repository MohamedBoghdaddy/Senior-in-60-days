const { redis } = require("../config/redis");
const {
  searchListings,
  getListingById,
} = require("../repositories/postgresRepository");
const { fetchListingDocument } = require("../repositories/mongoRepository");

const cacheKey = (id) => `listing:${id}`;

exports.search = async ({ search = "", page = 1 }) => {
  const limit = 20;
  const offset = (Number(page) - 1) * limit;
  return searchListings(search, offset, limit);
};

exports.getById = async (id) => {
  const key = cacheKey(id);
  const cached = await redis.get(key);
  if (cached) {
    return JSON.parse(cached);
  }

  const listing = await getListingById(id);
  if (!listing) {
    return null;
  }

  const document = await fetchListingDocument(id);
  const result = { ...listing, document };
  await redis.set(key, JSON.stringify(result), "EX", 60);
  return result;
};
