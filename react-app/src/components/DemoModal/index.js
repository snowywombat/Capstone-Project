import React, { useState } from "react";
import { useHistory } from 'react-router-dom';
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import TextField from '@material-ui/core/TextField';
import "./DemoForm.css";

function DemoFormModal() {
  const history = useHistory();
  const dispatch = useDispatch();
  const [email, setEmail] = useState("demo@aa.io");
  const [password, setPassword] = useState("password");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await dispatch(login(email, password))
        .then(() => {
          closeModal()
          history.push('/recipes')
        })
    } catch (e) {
      const errorResponse = e.errors;
      const errorMessages = errorResponse.map((error) => error.split(": ")[1]);
      setErrors(errorMessages);
    }
  };

  return (
    <>
      <h1 className='login-title'>Try the Demo</h1>
      <form onSubmit={handleSubmit}>
        <ul>
          {errors.map((error, idx) => (
            <li key={idx}>{error}</li>
          ))}
        </ul>
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
        <button type="submit" className='demo-button'>Log In</button>
      </form>
    </>
  );
}

export default DemoFormModal;
