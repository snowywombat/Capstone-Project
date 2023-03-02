import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import OpenCreateReviewModalButton from "../CreateReviewModal";
import CreateReviewModalForm from "../CreateReviewModal/CreateReviewModal";
import OpenEditReviewModalButton from "../EditReviewModal"
import EditReviewModalForm from "../EditReviewModal/EditReviewModal";
import OpenEditRecipeModalButton from "../EditRecipeModal";
import EditRecipeModalForm from "../EditRecipeModal/EditRecipeModal";
import { thunkGetSingleRecipe } from "../../store/recipes";
import { thunkDeleteReview, thunkGetAllReviews } from "../../store/reviews"
import './SingleRecipePage.css'

const SingleRecipePage = () => {
    const { recipeId } = useParams();
    const dispatch = useDispatch();

    const singleRecipe = useSelector(state => state.recipes[recipeId]);
    const allReviews = useSelector(state => state.reviews);
    const user = useSelector(state => state.session.user);

    const [modalRendered, setModalRendered] = useState(false);


    useEffect(() => {
        dispatch(thunkGetSingleRecipe(recipeId))
    }, [dispatch]);

    useEffect(() => {
        dispatch(thunkGetAllReviews(recipeId))
    }, [dispatch]);

    if(!singleRecipe) {
        return <div>Loading...</div>
    }


    if(!allReviews)  {
        return <div>Loading...</div>
    }

    const reviewArr = Object.values(allReviews)


    const handleDelete = (reviewId) => {
        dispatch(thunkDeleteReview(reviewId))
        .then(() => dispatch(thunkGetSingleRecipe(recipeId)))
        .then(() => dispatch(thunkGetAllReviews(recipeId)))
    }

    console.log(user.email, 'ibi')
    const dateObj = new Date(singleRecipe.createdAt);
    const formattedDate = dateObj.toLocaleDateString("en-US", {
        month: "long",
        day: "numeric",
        year: "numeric"
    });


    console.log(singleRecipe, 'de hulye')
    console.log(singleRecipe.userId, 'recipe user id')
    console.log(user.id, 'user id ')


    return (
        <>
            <section className='details-page'>
                <div className = 'datails-main'>
                    <div className = 'details-header'>
                        <div className='recipe-info-container'>
                            <div className='recipe-info-container-name'>
                                {singleRecipe.name}
                            </div>
                            <div className='recipe-info-container-author'>
                                By: {singleRecipe.user && singleRecipe.user.firstName} {singleRecipe.user && singleRecipe.user.lastName}
                            </div>
                            <div className='recipe-info-container-date'>
                                {formattedDate}
                            </div>
                        </div>
                        <div className='photo-container'>
                            <img src={singleRecipe.imgUrl} alt={"image of " + singleRecipe.description} id='recipeImg'></img>
                        </div>

                        <div className='recipe-button'>
                            {!modalRendered && user && singleRecipe.userId === user.id && (
                                <div className = 'edit-recipe-button'>
                                    <OpenEditRecipeModalButton
                                        buttonText="Edit Recipe"
                                        modalComponent={<EditRecipeModalForm
                                            recipes={singleRecipe}
                                        />}
                                    />
                                </div>

                            )}
                        </div>

                        <div>
                            {singleRecipe.description}
                        </div>
                        <div>
                            {singleRecipe.kitchenware && singleRecipe.kitchenware.map((item, index) => (
                                <div key={index} className = 'item-name'>
                                    {item.name}
                                </div>
                            ))}
                        </div>
                        <div>
                            {singleRecipe.servingSize} servings
                            {singleRecipe.ingredients && singleRecipe.ingredients.map((item, index) => (
                                <div key={index} className = 'item-name'>
                                    {item.measurement_num}
                                </div>
                            ))}
                            {singleRecipe.ingredients && singleRecipe.ingredients.map((item, index) => (
                                <div key={index} className = 'item-name'>
                                    {item.measurement_type}
                                </div>
                            ))}
                            {singleRecipe.ingredients && singleRecipe.ingredients.map((item, index)=> (
                                <div key={index} className = 'item-name'>
                                    {item.ingredient}
                                </div>
                            ))}
                        </div>
                        <div>
                            {singleRecipe.preparation && singleRecipe.preparation.map((step, index) => (
                                <div key={index} className = 'item-name'>
                                    {step.description}
                                </div>
                            ))}
                        </div>


                        <div className='reviews-section'>
                            {reviewArr.map((review, index) => {
                                const dateObj = new Date(review.created_at);
                                const formattedDate = dateObj.toLocaleDateString("en-US", {
                                    month: "long",
                                    day: "numeric",
                                    year: "numeric"
                                });

                                return (
                                <>
                                    <div key={index} className = 'review-body'>
                                        <div>
                                            {review.review}
                                            {review.location}
                                            {formattedDate}
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
                                                    reviews={review}
                                                    recipe = {singleRecipe}
                                                />}
                                            />
                                            </div>
                                        }

                                        {!modalRendered && user && review.user_id === user.id &&
                                            <div key = {review.id}>
                                                <div className='delete-review-button-div'>
                                                    <button onClick={() => handleDelete(review.id)} type="submit" className='delete-review-button'>
                                                        Delete Review
                                                    </button>
                                                </div>
                                            </div>
                                        }
                                    </div>


                                </>

                                )
                            })}
                            <div className='review-button'>
                                {!modalRendered && user && singleRecipe.userId !== user.id && (
                                    <div className = 'create-review-button'>
                                        <OpenCreateReviewModalButton
                                            buttonText="Add Review"
                                            modalComponent={<CreateReviewModalForm
                                                recipe={singleRecipe}
                                            />}
                                        />
                                    </div>

                                )}
                            </div>
                        </div>

                    </div>
                </div>

            </section>
        </>
    )

}

export default SingleRecipePage;
