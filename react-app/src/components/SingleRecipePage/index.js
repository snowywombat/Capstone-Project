import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import OpenCreateReviewModalButton from "../CreateReviewModal";
import CreateReviewModalForm from "../CreateReviewModal/CreateReviewModal";
import OpenEditReviewModalButton from "../EditReviewModal"
import EditReviewModalForm from "../EditReviewModal/EditReviewModal";
import CreateRecipeModalForm from '../CreateRecipeModal/CreateRecipeModal'
import { thunkGetSingleRecipe } from "../../store/recipes";
import { thunkDeleteReview, thunkGetAllReviews } from "../../store/reviews"
import './SingleRecipePage.css'

const SingleRecipePage = () => {
    const { recipeId } = useParams();
    const dispatch = useDispatch();

    const singleRecipe = useSelector(state => state.recipes.Recipes);
    const allReviews = useSelector(state => state.reviews.Reviews);
    const user = useSelector(state => state.session.user);

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

    const handleDelete = () => {
        reviewArr.forEach(review => {
            dispatch(thunkDeleteReview(review.id))
            .then(() => dispatch(thunkGetSingleRecipe(recipeId)))
            .then(() => dispatch(thunkGetAllReviews(recipeId)))
        })
    }


    return (
        <>
            <section className='details-page'>
                <div className = 'datails-main'>
                    <div className = 'details-header'>
                        {recipeArr.map((recipe, index) => (
                            <>
                                <div key={index} className = 'recipe-top'>
                                    <div className='recipe-info-container'>
                                        <div className='recipe-info-container-name'>
                                            {recipe.name}
                                        </div>
                                        <div className='recipe-info-container-author'>
                                            By: {recipe.user && recipe.user.firstName} {recipe.user && recipe.user.lastName}
                                        </div>
                                        <div className='recipe-info-container-date'>
                                            {recipe.createdAt}
                                        </div>
                                    </div>
                                    <div className='photo-container'>
                                        <img src={recipe.imgUrl} alt={"image of " + recipe.description} id='recipeImg'></img>
                                    </div>

                                </div>

                                    <div>
                                        {recipe.description}
                                    </div>
                                    <div>
                                        {recipe.kitchenware && recipe.kitchenware.map((item, index) => (
                                            <div key={index} className = 'item-name'>
                                                {item.name}
                                            </div>
                                        ))}
                                    </div>
                                    <div>
                                        {recipe.servingSize} servings
                                        {recipe.ingredients && recipe.ingredients.map((item, index) => (
                                            <div key={index} className = 'item-name'>
                                                {item.measurement_num}
                                            </div>
                                        ))}
                                        {recipe.ingredients && recipe.ingredients.map((item, index) => (
                                            <div key={index} className = 'item-name'>
                                                {item.measurement_type}
                                            </div>
                                        ))}
                                        {recipe.ingredients && recipe.ingredients.map((item, index)=> (
                                            <div key={index} className = 'item-name'>
                                                {item.ingredient}
                                            </div>
                                        ))}
                                    </div>
                                    <div>
                                        {recipe.preparation && recipe.preparation.map((step, index) => (
                                            <div key={index} className = 'item-name'>
                                                {step.description}
                                            </div>
                                        ))}
                                    </div>


                                <div className='reviews-section'>
                                    {reviewArr.map((review, index) => (
                                        <>
                                            <div key={index} className = 'review-body'>
                                                <div>
                                                    {review.review}
                                                    {review.location}
                                                    {review.created_at}
                                                    {review.user && review.user.first_name}
                                                    {review.user && review.user.last_name}
                                                </div>
                                            </div>

                                            <div className='review-button'>
                                                {!modalRendered && user && review.user_id === user.id &&
                                                    <div className = 'edit-review-button'>
                                                    <OpenEditReviewModalButton
                                                        buttonText="Edit Review"
                                                        modalComponent={<EditReviewModalForm
                                                            recipes={recipe}
                                                            reviews={review}
                                                        />}
                                                    />
                                                    </div>
                                                }

                                                {!modalRendered && user && review.user_id === user.id &&
                                                    <div className='delete-review-button-div'>
                                                        <button onClick={handleDelete} type="submit" className='delete-review-button'>
                                                            Delete Review
                                                        </button>
                                                    </div>
                                                }
                                            </div>


                                        </>
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
