import React, { useState } from "react";
import { useHistory } from 'react-router-dom';
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import TextField from '@material-ui/core/TextField';
import "./LoginForm.css";

function LoginFormModal() {
  const history = useHistory();
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
      <h1>Log In</h1>
      <form onSubmit={handleSubmit}>
      <ul>
					{errors.map((error, idx) => (
						<li className='errors-div' key={idx}>{error}</li>
					))}
				</ul>
        <div className='fields'>

          <div className='email-login-field'>
            <TextField
              label="Email"
              type="email"
              value={email}
              variant='outlined'
              size="small"
              onChange={(e) => setEmail(e.target.value)}
              required
            />

          </div>

          <div className='password-login-field'>
            <TextField
              label="Password"
              type="password"
              value={password}
              variant='outlined'
              size="small"
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
