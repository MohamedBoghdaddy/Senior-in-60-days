const { Queue, Worker } = require("bullmq");
const { redis } = require("../config/redis");
const { processIngestJob } = require("./ingestJob");

const queueName = process.env.BULLMQ_QUEUE_NAME || "platform-jobs";
const ingestQueue = new Queue(queueName, { connection: redis });

const initializeQueues = () => {
  new Worker(queueName, processIngestJob, { connection: redis });
};

module.exports = { ingestQueue, initializeQueues };
