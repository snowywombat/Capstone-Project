import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import OpenCreateReviewModalButton from "../CreateReviewModal";
import CreateReviewModalForm from "../CreateReviewModal/CreateReviewModal";
import CreateRecipeModalForm from '../CreateRecipeModal/CreateRecipeModal'
import { thunkGetSingleRecipe } from "../../store/recipes";
import { thunkGetAllReviews } from "../../store/reviews"
import './SingleRecipePage.css'

const SingleRecipePage = () => {
    const { recipeId } = useParams();
    const dispatch = useDispatch();

    const singleRecipe = useSelector(state => state.recipes.Recipes);
    const allReviews = useSelector(state => state.reviews.Reviews)

    const [modalRendered, setModalRendered] = useState(false);


    useEffect(() => {
        dispatch(thunkGetSingleRecipe(recipeId))
    }, [dispatch, recipeId]);

    useEffect(() => {
        dispatch(thunkGetAllReviews(recipeId))
    }, [dispatch, recipeId]);

    if(!singleRecipe) {
        return <div>Loading...</div>
    }
    if(!allReviews)  {
        return <div>Loading...</div>
    }


    const recipeArr = Object.values(singleRecipe)
    const reviewArr = Object.values(allReviews)


    return (
        <>
            <section className='details-page'>
                <div className = 'datails-main'>
                    <div className = 'details-header'>
                        {recipeArr.map(recipe => (
                            <>
                                <div key={recipe.id} className = 'recipe-body'>
                                    <div className='photo-container'>
                                        <img src={recipe.imgUrl} alt={"image of " + recipe.description} id='recipeImg'></img>
                                    </div>

                                        {recipe.name}
                                        By
                                        {recipe.user && recipe.user.firstName}
                                        {recipe.user && recipe.user.lastName}
                                        {recipe.createdAt}
                                        {recipe.name}

                                    <div>
                                        {recipe.description}
                                    </div>
                                    <div>
                                        {recipe.kitchenware && recipe.kitchenware.map(item => (
                                            item.name
                                        ))}
                                    </div>
                                    <div>
                                        {recipe.servingSize} servings
                                        {recipe.ingredients && recipe.ingredients.map(item => (
                                            item.measurement_num
                                        ))}
                                        {recipe.ingredients && recipe.ingredients.map(item => (
                                            item.measurement_type
                                        ))}
                                        {recipe.ingredients && recipe.ingredients.map(item => (
                                            item.ingredient
                                        ))}
                                    </div>
                                    <div>
                                        {recipe.preparation && recipe.preparation.map(step => (
                                            step.description
                                        ))}
                                    </div>
                                </div>

                                <div className='reviews-section'>
                                    {reviewArr.map(review => (
                                        <div key={review.id} className = 'review-body'>
                                            <div>
                                                {review.review}
                                                {review.location}
                                                {review.created_at}
                                                {review.user && review.user.first_name}
                                                {review.user && review.user.last_name}
                                            </div>
                                        </div>
                                    ))}
                                    <div className='review-button'>
                                        {!modalRendered && (
                                            <div className = 'create-review-button'>
                                                <OpenCreateReviewModalButton
                                                    buttonText="Add Review"
                                                    modalComponent={<CreateReviewModalForm
                                                        recipe={recipe}
                                                    />}
                                                />
                                            </div>
                                        )}
                                    </div>
                                </div>
                            </>
                        ))}
                    </div>
                </div>

            </section>
        </>
    )

}

export default SingleRecipePage;
