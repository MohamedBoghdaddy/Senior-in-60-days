const { logger } = require("../utils/logger");
const { saveListingMetadata } = require("../repositories/postgresRepository");
const { saveDocument } = require("../repositories/mongoRepository");

exports.processIngestJob = async (job) => {
  try {
    logger.info("job.ingest.start", { jobId: job.id, data: job.data });
    await saveListingMetadata(job.data.listing);
    await saveDocument(job.data.document);
    logger.info("job.ingest.completed", { jobId: job.id });
  } catch (error) {
    logger.error("job.ingest.failed", { jobId: job.id, error: error.message });
    throw error;
  }
};
