import React from "react";
import { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { thunkCreateReview } from "../../store/reviews";
import { thunkGetAllReviews } from "../../store/reviews";
import { thunkGetSingleRecipe } from "../../store/recipes";
import { useModal } from "../../context/Modal";
import "../LoginFormModal/LoginForm.css";
import "./CreateReviewModal.css";

function CreateReviewModalForm({ recipe }) {

  const dispatch = useDispatch();

  const [review, setReview] = useState("");
  const [stars, setStars] = useState("");
  const [location, setLocation] = useState("");
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
      await dispatch(thunkCreateReview(body, recipe.id))
        .then(() => dispatch(thunkGetSingleRecipe(recipe.id)))
        .then(() => dispatch(thunkGetAllReviews(recipe.id)))
        .then(() => {
          setReviewCreated(true);
          closeModal();
        })
    } catch (e) {
      const errorResponse = e.errors;
      const errorMessages = errorResponse.map((error) => error);
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
      <div className="Global-Modal-Header">Add a new review</div>
      <form onSubmit={handleSubmit} className="Global-ModalForm-Container">
        <ul className="Global-Errors-UL">
          {errors.map((error, idx) => (
            <li key={idx} className="Global-Errors-LI">
              {error}
            </li>
          ))}
        </ul>

        <div className='review-field'>
          <label>Your Review:</label>
          <input
            value={review}
            onChange={(e) => setReview(e.target.value)}
            required
            placeholder="I loved this recipe!"
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
            placeholder="5"
          />
        </div>

        <div className='location-field'>
          <label>Where are you from?</label>
          <input
            value={location}
            onChange={(e) => setLocation(e.target.value)}
            required
            placeholder="Seattle, WA"
          />
        </div>
        <button type="submit" className="review-submit-button">
          Add Review
        </button>
      </form>
    </div>
  );
}

export default CreateReviewModalForm;
