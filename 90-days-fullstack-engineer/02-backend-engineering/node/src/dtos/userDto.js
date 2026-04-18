exports.loginPayload = ({ email, password }) => ({
  email,
  password,
});

exports.userResponse = ({ id, email, role }) => ({
  id,
  email,
  role,
});
