import React from 'react';
import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import CreateRecipeModal from '../CreateRecipeModal';
import CreateReviewModal from '../CreateReviewModal'
import CreateRecipeModalForm from '../CreateRecipeModal/CreateRecipeModal';
import OpenCreateRecipeModalButton from '../CreateRecipeModal';
import './Navigation.css';
import './ProfileButton.css'

function Navigation({ isLoaded }){
	const sessionUser = useSelector(state => state.session.user);

	const [modalRendered, setModalRendered] = useState(false);

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
		<div className='recipe-button'>
			{!modalRendered && (
				<div className = 'create-recipe-button'>
					<OpenCreateRecipeModalButton
						user={ sessionUser }
						buttonText="Add Recipe"
						modalComponent={<CreateRecipeModalForm
						/>}
					/>
				</div>
			)}
		</div>
		{/* <div className="CreateRecipe-Holder">
            <CreateRecipeModal user={sessionUser} />
        </div>
		<div className="CreateReview-Holder">
            <CreateReviewModal user={sessionUser} />
        </div> */}
	</>
	);
}

export default Navigation;
