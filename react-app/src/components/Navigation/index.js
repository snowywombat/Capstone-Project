import React from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import OpenModalButtonAddRecipe from '../OpenModalAddRecipe';
import CreateRecipeModalForm from '../CreateRecipeModal/CreateRecipeModal'
import './Navigation.css';
import './ProfileButton.css'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	return (

		<div className='nav-container'>
			<nav className='nav-bar'>
				<NavLink className='home-navlink' exact to="/recipes">
				{/* <i className="fa-solid fa-crown" /> */}
				<h1 className='title'>shana's kitchen</h1>
				</NavLink>
			</nav>

			<div className='profile-div'>
				{isLoaded && (
					<div className='profile'>
					<ProfileButton user={sessionUser} />
					</div>
				)}
			</div>

			<nav className='extra-header'>
				<div className='all-recipes-nav'>
					<NavLink className='recipes-navlink' exact to="/recipes">
						<h3 className='recipes-nav'> All Recipes</h3>
					</NavLink>
				</div>
				<div className='recipe-button'>
					{sessionUser && (
						<div className = 'create-recipe-button'>
							<OpenModalButtonAddRecipe

								user={sessionUser}
								// recipe={recipe}
								buttonText="Add a Recipe"
								modalComponent={<CreateRecipeModalForm
								/>}
							/>
						</div>
					)}
				</div>
			</nav>
		</div>

	);
}

export default Navigation;
