import React from 'react';
import { useState } from 'react';
import { NavLink } from 'react-router-dom';
import { useSelector } from 'react-redux';
import ProfileButton from './ProfileButton';
import OpenCreateRecipeModalButton from '../CreateRecipeModal'
import CreateRecipeModalForm from '../CreateRecipeModal/CreateRecipeModal'
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
				<NavLink className='home-navlink' exact to="/recipes">
				{/* <i className="fa-solid fa-crown" /> */}
				<h1 className='title'>shana's kitchen</h1>
				</NavLink>
			</div>
			</div>

			<div className='recipe-button'>
                {!modalRendered && sessionUser && (
                    <div className = 'create-recipe-button'>
                        <OpenCreateRecipeModalButton
                            user={sessionUser}
                            buttonText="Add Recipe"
                            modalComponent={<CreateRecipeModalForm
                            />}
                        />
                    </div>
                )}
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
