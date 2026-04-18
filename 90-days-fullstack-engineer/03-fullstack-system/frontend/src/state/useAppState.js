import { useState } from "react";

export function useAppState() {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(null);

  return {
    user,
    setUser,
    token,
    setToken,
  };
}
