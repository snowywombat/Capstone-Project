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
    // const [first_name, setFirstName ] = useState(reviews.user.first_name)
    // const [last_name, setLastName ] = useState(reviews.user.last_name)
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
        // user: {
        //   first_name: first_name,
        //   last_name: last_name
        // }
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
            <label for="review" className="Global-Modal-Label">
              <input
                type="text"
                value={review}
                onChange={(e) => setReview(e.target.value)}
                required
                className="Global-Modal-input"
              />
            </label>
            <label for="stars" className="Global-Modal-Label">
                <input
                type="number"
                value={stars}
                onChange={(e) => setStars(e.target.value)}
                required
                className="Global-Modal-input"
                />
            </label>
            <label for="location" className="Global-Modal-Label">
              <input
                type="text"
                value={location}
                onChange={(e) => setLocation(e.target.value)}
                required
                className="Global-Modal-input"
              />
            </label>
            {/* <label for="first-name" className="Global-Modal-Label">
              <input
                type="text"
                value={first_name}
                onChange={(e) => setFirstName(e.target.value)}
                required
                className="Global-Modal-input"
              />
            </label>
            <label for="last-name" className="Global-Modal-Label">
              <input
                type="text"
                value={last_name}
                onChange={(e) => setLastName(e.target.value)}
                required
                className="Global-Modal-input"
              />
            </label> */}
            <button type="submit" className="Global-SubmitButton">
              Edit Review
            </button>
          </form>
        </div>
      );

}

export default EditReviewModalForm;
