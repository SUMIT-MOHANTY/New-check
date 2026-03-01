import React, { useState, useEffect } from 'react';
import AuthContext from './AuthContext';
import { login as apiLogin, logout as apiLogout, getCurrentUser } from '../services/api';

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [token, setToken] = useState(() => localStorage.getItem('authToken'));
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    const initAuth = async () => {
      const storedUser = localStorage.getItem('authUser');
      if (token && storedUser) {
        try {
          const userData = await getCurrentUser();
          setUser(userData.user || JSON.parse(storedUser));
        } catch {
          setUser(JSON.parse(storedUser));
        }
      } else if (token) {
        const storedUserData = storedUser ? JSON.parse(storedUser) : null;
        setUser(storedUserData);
      }
      setIsLoading(false);
    };
    initAuth();
  }, [token]);

  const login = async (email, password) => {
    const data = await apiLogin(email, password);
    localStorage.setItem('authToken', data.access_token);
    localStorage.setItem('authUser', JSON.stringify(data.user));
    setToken(data.access_token);
    setUser(data.user);
    return data;
  };

  const logout = async () => {
    await apiLogout();
    setToken(null);
    setUser(null);
  };

  const isAuthenticated = !!token && !!user;

  return (
    <AuthContext.Provider value={{ user, token, isAuthenticated, isLoading, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
