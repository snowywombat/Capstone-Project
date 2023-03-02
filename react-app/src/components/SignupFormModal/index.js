import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { signUp } from "../../store/session";
import TextField from '@material-ui/core/TextField';
import "./SignupForm.css";

function SignupFormModal() {
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
			<h1>Sign Up</h1>
			<form onSubmit={handleSubmit}>
				<ul>
					{errors.map((error, idx) => (
						<li key={idx}>{error}</li>
					))}
				</ul>
				<div className='fields'>
					<div className='first-name-field'>
						<TextField
						label="First Name"
						value={first_name}
						variant="outlined"
						size="small"
						InputLabelProps={{ style: { fontSize: 12 } }}
						onChange={(e) => setFirstName(e.target.value)}
						required
						/>
					</div>
					<div className='last-name-field'>
						<TextField
						label="Last Name"
						value={last_name}
						variant="outlined"
						size="small"
						InputLabelProps={{ style: { fontSize: 12 } }}
						onChange={(e) => setLastName(e.target.value)}
						required
						/>
					</div>
					<div className='email-signup-field'>
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
					<div className='username-signup-field'>
						<TextField
						label="Username"
						value={username}
						variant="outlined"
						size="small"
						InputLabelProps={{ style: { fontSize: 12 } }}
						onChange={(e) => setUsername(e.target.value)}
						required
						/>
					</div>
					<div className='password-signup-field'>
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

					<div className='confirm-password-field'>
						<TextField
						label="Confirm Password"
						type="password"
						value={confirmPassword}
						variant="outlined"
						size="small"
						InputLabelProps={{ style: { fontSize: 12 } }}
						onChange={(e) => setConfirmPassword(e.target.value)}
						required
						/>
          			</div>
				</div>
				<button className='signup-button' type="submit">Sign Up</button>
			</form>
		</>
	);
}

export default SignupFormModal;
