const { connectMongo } = require("../config/db");

exports.fetchListingDocument = async (listingId) => {
  const db = await connectMongo();
  return db
    .collection("listing_documents")
    .findOne({ listingId: Number(listingId) });
};

exports.saveDocument = async ({ listingId, content, metadata }) => {
  const db = await connectMongo();
  return db
    .collection("listing_documents")
    .insertOne({
      listingId: Number(listingId),
      content,
      metadata,
      createdAt: new Date(),
    });
};
