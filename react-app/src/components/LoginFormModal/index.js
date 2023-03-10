import React, { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import TextField from '@material-ui/core/TextField';
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await dispatch(login(email, password))
        .then(() => {
          closeModal()
        })
    } catch (e) {
      const errorResponse = e.errors;
      const errorMessages = errorResponse.map((error) => error.split(": ")[1]);
      setErrors(errorMessages);
    }
  };

  return (
    <>
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
        <div className='fields'>
          <div className='email-login-field'>
            <TextField
              label="Email"
              value={email}
              variant="outlined"
              size="small"
              InputLabelProps={{ style: { fontSize: 12 } }}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className='password-login-field'>
            <TextField
              label="Password"
              type="password"
              value={password}
              variant="outlined"
              size="small"
              InputLabelProps={{ style: { fontSize: 12 } }}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
        </div>
        <button type="submit" className='login-button'>Log In</button>
      </form>
    </>
  );
}

export default LoginFormModal;
