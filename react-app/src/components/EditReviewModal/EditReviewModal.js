import React from "react";
import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { thunkEditReview } from "../../store/reviews";
import { thunkGetAllReviews } from "../../store/reviews";
import { thunkGetSingleRecipe } from "../../store/recipes";
import TextField from '@material-ui/core/TextField';
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
            <ul className="Global-Errors-UL">
              {errors.map((error, idx) => (
                <li key={idx} className="Global-Errors-LI">
                  {error}
                </li>
              ))}
            </ul>
            <div className='review-field'>
              <TextField
                label="Your Review"
                value={review}
                variant="outlined"
                size="small"
                InputLabelProps={{ style: { fontSize: 12 } }}
                onChange={(e) => setReview(e.target.value)}
                required
              />
            </div>
            <div className='stars-field'>
              <TextField
                label="Rate this recipe 1-5 stars"
                value={stars}
                variant="outlined"
                size="small"
                InputLabelProps={{ style: { fontSize: 12 } }}
                onChange={(e) => setStars(e.target.value)}
                required
                type="number"
                min='1'
                max='5'
              />
            </div>
            <div className='location-field'>
              <TextField
                label="Where are you from?"
                value={location}
                variant="outlined"
                size="small"
                InputLabelProps={{ style: { fontSize: 12 } }}
                onChange={(e) => setLocation(e.target.value)}
                required
              />
            </div>
            <button type="submit" className="review-submit-button">
              Edit Review
            </button>
          </form>
        </div>
      );

}

export default EditReviewModalForm;
