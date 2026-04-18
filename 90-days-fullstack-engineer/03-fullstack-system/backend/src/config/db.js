const { Pool } = require("pg");
const { MongoClient } = require("mongodb");

const pool = new Pool({ connectionString: process.env.PG_CONNECTION });

const mongoClient = new MongoClient(process.env.MONGO_URI, {
  useUnifiedTopology: true,
});

const connectMongo = async () => {
  if (!mongoClient.isConnected()) {
    await mongoClient.connect();
  }
  return mongoClient.db();
};

module.exports = { pool, connectMongo };
