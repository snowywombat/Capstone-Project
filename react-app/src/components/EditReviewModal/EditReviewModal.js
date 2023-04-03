import React from "react";
import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { thunkEditReview } from "../../store/reviews";
import { thunkGetAllReviews } from "../../store/reviews";
import { thunkGetSingleRecipe } from "../../store/recipes";
import { useModal } from "../../context/Modal";
import "../LoginFormModal/LoginForm.css";
import "./EditReviewModal.css";

function EditReviewModalForm({ reviews, recipe }) {

    const dispatch = useDispatch();

    const [review, setReview] = useState(reviews.review);
    const [stars, setStars] = useState(reviews.stars);
    const [location, setLocation] = useState(reviews.location);
    const [errors, setErrors] = useState([]);
    const { closeModal } = useModal();

    const [reviewCreated, setReviewCreated] = useState(false);

    const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const body = {
        review,
        stars,
        location,
    };

    try {
      await dispatch(thunkEditReview(body, reviews.id))
        .then(() => dispatch(thunkGetSingleRecipe(recipe.id)))
        .then(() => dispatch(thunkGetAllReviews(recipe.id)))
        .then(() => {
          setReviewCreated(true);
          closeModal();
        })
    } catch (e) {
      const errorResponse = e.errors;
      const errorMessages = errorResponse.map((error) => error.split(": ")[1]);
      setErrors(errorMessages);
    }
  };

  useEffect(() => {
    if (reviewCreated) {
      // fetch updated data here
      setReviewCreated(false); // reset the state variable
    }
  }, [reviewCreated]);

    return (
        <div className="Global-Modal-Container3">
          <div className="Global-Modal-Header">Edit a review</div>
          <form onSubmit={handleSubmit} className="Global-ModalForm-Container">
            <ul>
              {errors.map((error, idx) => (
                <li className='errors-div' key={idx}>{error}</li>
              ))}
            </ul>

              <div className='review-field'>
              <label>Your Review:</label>
              <input
                value={review}
                onChange={(e) => setReview(e.target.value)}
                required
              />
            </div>

            <div className='stars-field'>
              <label>Rate this recipe 1-5 stars:</label>
              <input
                type="number"
                min='1'
                max='5'
                value={stars}
                onChange={(e) => setStars(e.target.value)}
                required
              />
            </div>

            <div className='location-field'>
              <label>Where are you from?</label>
              <input
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                required
              />
            </div>


            <button type="submit" className="review-submit-button">
              Edit Review
            </button>

            <ul className='errors-bottom'>
              {errors.map((error, idx) => (
                <li className='errors-div' key={idx}>{error}</li>
              ))}
          </ul>

          </form>
        </div>
      );

}

export default EditReviewModalForm;
