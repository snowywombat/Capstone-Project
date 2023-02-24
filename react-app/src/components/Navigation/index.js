import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import './Navigation.css';
import './ProfileButton.css'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (
	<>
		<section className='header'>
		<nav className='nav-bar'>

			<div className='inner-nav-bar'>
			<div className='home'>
				<NavLink className='home-navlink' exact to="/">
				{/* <i className="fa-solid fa-crown" /> */}
				<h1 className='title'>shana's kitchen</h1>
				</NavLink>
			</div>

			{/* <div className = 'create-button'>
				<OpenCreateSpotModalButton
						buttonText="Heirbnb your home"
						modalComponent={<CreateSpotModal />}
					/>
			</div> */}
			</div>

			{isLoaded && (
				<div className='profile'>
				<ProfileButton user={sessionUser} />
				</div>
			)}
		</nav>
		</section>
		<div className='extra-header'>
			<div className='navigation'>
			Recipes
			</div>
		</div>
	</>
	);
}

export default Navigation;
