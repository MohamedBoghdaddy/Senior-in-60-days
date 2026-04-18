const bcrypt = require("bcryptjs");

const users = [
  {
    id: 1,
    email: "admin@example.com",
    passwordHash: bcrypt.hashSync("Admin1234", 10),
    role: "admin",
  },
];

exports.findByEmail = async (email) =>
  users.find((user) => user.email === email);
exports.findById = async (id) => users.find((user) => user.id === Number(id));
exports.verifyPassword = async (user, password) =>
  bcrypt.compare(password, user.passwordHash);
exports.saveRefreshToken = async (userId, token) => {
  const user = users.find((row) => row.id === Number(userId));
  if (user) user.refreshToken = token;
};
