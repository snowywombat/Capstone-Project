import React, { useState } from "react";
import { useHistory } from 'react-router-dom';
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import TextField from '@material-ui/core/TextField';
import "./SignupForm.css";

function SignupFormModal() {
	const history = useHistory();
	const dispatch = useDispatch();
	const [first_name, setFirstName ] = useState("")
	const [last_name, setLastName ] = useState("")
	const [email, setEmail] = useState("");
	const [username, setUsername] = useState("");
	const [password, setPassword] = useState("");
	const [confirmPassword, setConfirmPassword] = useState("");
	const [errors, setErrors] = useState([]);
	const { closeModal } = useModal();

	const handleSubmit = async (e) => {
		e.preventDefault();
		if (password === confirmPassword) {
			try {
				await dispatch(signUp(first_name, last_name, username, email, password))
					.then(() => {
						closeModal()
						history.push('/recipes')
					})
			} catch (e) {
				const errorResponse = e.errors;
				const errorMessages = errorResponse.map((error) => error.split(": ")[1]);
				setErrors(errorMessages);
			}
		} else {
			setErrors([
				"Confirm Password field must be the same as the Password field",
			]);
		}
	};

	return (
		<>
			<h1 className='sign-up-header'>Sign Up</h1>
			<form onSubmit={handleSubmit}>
				<ul>
					{errors.map((error, idx) => (
						<li className='errors-div' key={idx}>{error}</li>
					))}
				</ul>
				<div className='fields'>

					<div className='first-name-field'>
						<TextField
							label='First Name'
							className='inputs'
							value={first_name}
							variant='outlined'
                			size="small"
							// placeholder='Jane'
							onChange={(e) => setFirstName(e.target.value)}
							required
						/>
					</div>

					<div className='last-name-field'>
						<TextField
							label='Last Name'
							value={last_name}
							variant='outlined'
							size="small"
							// placeholder='Doe'
							onChange={(e) => setLastName(e.target.value)}
							required
						/>
					</div>

					<div className='email-signup-field'>
						<TextField
							label='Email'
							type="email"
							value={email}
							variant='outlined'
							size="small"
							// placeholder="janedoe@aa.io"
							onChange={(e) => setEmail(e.target.value)}
							required
						/>
					</div>

					<div className='username-signup-field'>
						<TextField
							label='Username'
							value={username}
							variant='outlined'
							size="small"
							// placeholder='janedoe'
							onChange={(e) => setUsername(e.target.value)}
							required
						/>
					</div>

					<div className='password-signup-field'>
						<TextField
							label='Password'
							type="password"
							value={password}
							variant='outlined'
							size="small"
							// placeholder='********'
							onChange={(e) => setPassword(e.target.value)}
							required
						/>
					</div>

					<div className='confirm-password-field'>
						<TextField
							label='Confirm Password'
							type="password"
							value={confirmPassword}
							variant='outlined'
							size="small"
							// placeholder='********'
							onChange={(e) => setConfirmPassword(e.target.value)}
							required
						/>
          			</div>
				</div>
				<button className='signup-button' type="submit">Sign Up</button>

				<ul className='errors-bottom'>
					{errors.map((error, idx) => (
						<li className='errors-div' key={idx}>{error}</li>
					))}
				</ul>

			</form>
		</>
	);
}

export default SignupFormModal;
