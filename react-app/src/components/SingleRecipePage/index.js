import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import OpenModalButtonEdit from "../OpenModalEdit";
import OpenModalButton from "../OpenModalButton"
import CreateReviewModalForm from "../CreateReviewModal/CreateReviewModal";
import EditReviewModalForm from "../EditReviewModal/EditReviewModal";
import EditRecipeModalForm from "../EditRecipeModal/EditRecipeModal";
import { thunkGetSingleRecipe } from "../../store/recipes";
import { thunkDeleteReview, thunkGetAllReviews } from "../../store/reviews"
import './SingleRecipePage.css'

const SingleRecipePage = () => {
    const { recipeId } = useParams();
    console.log(typeof(recipeId), 'recipeId')
    const dispatch = useDispatch();

    const singleRecipe = useSelector(state => state.recipes);
    const allReviews = useSelector(state => state.reviews);
    const user = useSelector(state => state.session.user);

    console.log(singleRecipe, 'singleRecipe in component')

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

    const recipe = Object.values(singleRecipe).find(el => el.id === Number(recipeId))
    console.log(recipe, 'recipe here')

    const reviewArr = Object.values(allReviews)

    const dateObj = new Date(recipe?.createdAt);
    const formattedDate = dateObj.toLocaleDateString("en-US", {
        month: "long",
        day: "numeric",
        year: "numeric"
    });


    const handleDelete = (reviewId) => {
        dispatch(thunkDeleteReview(reviewId))
        .then(() => dispatch(thunkGetSingleRecipe(recipeId)))
        .then(() => dispatch(thunkGetAllReviews(recipeId)))
    }

   const handleClick = (reviewId) => {
        const confirmed = window.confirm("Are you sure you want to delete your review?");
        if (confirmed) {
          handleDelete(reviewId);
        }
    }

    return (
        <>
            {recipe && (
            <section className='details-page'>
                <div className = 'details-main'>
                    <div className='recipe-button'>
                    {user && recipe.user_id === user.id && (
                        <div className = 'edit-recipe-button'>
                            <OpenModalButtonEdit
                                buttonText="Edit Recipe"
                                modalComponent={<EditRecipeModalForm
                                    recipes={recipe}
                                />}
                            />
                        </div>

                    )}
                    </div>

                    <div className = 'details-header'>
                        <div key={recipe.id} className='recipe-info-container'>
                            <div className='recipe-info-container-name'>
                                {recipe.name}
                            </div>
                            <div className='recipe-info-container-author'>
                                By: {recipe.user && recipe.user.firstName} {recipe.user && recipe.user.lastName}
                            </div>
                            <div className='recipe-info-container-date'>
                                {formattedDate}
                            </div>
                        </div>
                        <div className='photo-container'>
                            <img src={recipe.img_url}
                                alt={"image of " + recipe.description}
                                id='recipeImg'>
                            </img>
                        </div>
                    </div>

                    <div className = 'single-page-main'>

                        <div className='recipe-description'>
                            {recipe.description}
                        </div>
                        <div className='kitchenware'>
                            What you'll need
                            <hr className="hr-break" />
                            <div className='kitchen-ele'>
                                {recipe.kitchenware && recipe.kitchenware.map((item, index) => (
                                    <div key={index} className = 'item-name'>
                                        <li>{item.name}</li>
                                    </div>
                                ))}
                            </div>
                        </div>

                        <div className='ingredients'>
                            Ingredients
                            <hr className="hr-break" />
                            <div className='ingredients-ele'>

                                <div className='servings'>
                                    {recipe.servingSize} servings
                                </div>

                                <div className = 'ingredient-field'>
                                    {recipe.ingredients && recipe.ingredients.map((item, index) => (
                                        <div key={index} className = 'ingredients-ele'>
                                            <li>{parseFloat(item.measurement_num).toFixed(0)} {item.measurement_type} {item.ingredient}</li>
                                        </div>
                                    ))}
                                </div>
                            </div>
                        </div>


                        <div className='preparations'>
                            Preparations
                            <hr className="hr-break" />
                            <div className='preparations-ele'>
                                {recipe.preparation && recipe.preparation.map((step, index) => (
                                    <div key={index} className = 'steps'>
                                        <div className='step-label'> Step {index + 1} </div>
                                        {step.description}
                                    </div>
                                ))}
                            </div>
                        </div>


                        <div className='reviews-section'>
                            Reviews
                            <hr className="hr-break" />
                            <div className='reviews-ele'>
                                {reviewArr.map((review, index) => {
                                    const dateObj = new Date(review.created_at);
                                    const formattedDate = dateObj.toLocaleDateString("en-US", {
                                        month: "long",
                                        day: "numeric",
                                        year: "numeric"
                                    });

                                    return (
                                    <>
                                        <div className='review-body'>
                                            <div className = 'review-body-review'>
                                                {review.review}
                                                <div className='review-sub-body-name'>
                                                    <div className='review-sub-body-first-name'>
                                                        - {review.user && review.user.first_name}
                                                    </div>

                                                        {review.user && review.user.last_name}

                                                    <div className='review-sub-body-location'>
                                                        from {review.location}
                                                    </div>

                                                    <div className='delete-button'>
                                                        {user && review.user_id === user.id &&
                                                            <div key = {review.id}>
                                                                <div className='delete-review-button-div'>
                                                                    <button onClick={() => handleClick(review.id)} type="submit" className='delete-review-button'>
                                                                    <i className="fa-sharp fa-solid fa-circle-xmark" style={{fontSize: 20}}></i>
                                                                    </button>
                                                                </div>
                                                            </div>
                                                        }
                                                    </div>
                                                </div>


                                                <div className='review-sub-body-date'>
                                                    edited at: {formattedDate}
                                                </div>

                                            </div>
                                        </div>


                                        <div className='review-button2'>
                                            {user && review.user_id === user.id &&
                                                <div className = 'edit-review-button'>
                                                <OpenModalButtonEdit
                                                    buttonText="Edit Review"
                                                    modalComponent={<EditReviewModalForm
                                                        reviews={review}
                                                        recipe = {recipe}
                                                    />}
                                                />
                                                </div>
                                            }
                                        </div>

                                        <div className='review-button'>
                                            {(recipe.user_id !== user.id) && (
                                            (!recipe.reviews || recipe.reviews.length === 0 ||
                                            !recipe.reviews.some(review => review.user_id === user.id))
                                            ) ? (
                                            <div className='create-review-button'>
                                                <OpenModalButtonEdit
                                                buttonText="Add Review"
                                                modalComponent={<CreateReviewModalForm recipe={recipe} />}
                                                />
                                            </div>
                                            ) : null}
                                        </div>


                                        {/* <div className='review-button'>
                                            {recipe.user_id !== user.id && review.user_id !== user.id ? (
                                                <div className='create-review-button'>
                                                    <OpenModalButtonEdit
                                                        buttonText="Add Review"
                                                        modalComponent={<CreateReviewModalForm recipe={recipe} />}
                                                    />
                                                </div>
                                            ) : review ? null : (
                                                <div className='create-review-button'>
                                                  <OpenModalButtonEdit
                                                    buttonText="Add Review"
                                                    modalComponent={<CreateReviewModalForm recipe={recipe} />}
                                                  />
                                                </div>
                                              )}

                                        </div> */}
                                    </>
                                    )
                                })}


                            </div>

                        </div>
                    </div>
                </div>

            </section>
            )}
        </>
    )

}

export default SingleRecipePage;
