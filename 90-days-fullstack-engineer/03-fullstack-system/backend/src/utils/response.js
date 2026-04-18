exports.success = (res, data, status = 200) =>
  res.status(status).json({ success: true, data });
exports.error = (res, code, message, status = 400) =>
  res.status(status).json({ success: false, error: { code, message } });
