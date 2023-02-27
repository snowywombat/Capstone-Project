//Actions
const GET_ALL_REVIEWS = "reviews/get_all_reviews"
const CREATE_NEW_REVIEW = "reviews/create_new_review"
const EDIT_REVIEW = "reviews/edit_review"

//Action creators
const getAllReviews = (reviews) => ({
    type: GET_ALL_REVIEWS,
    payload: reviews
})

const createReview = (review) => ({
    type: CREATE_NEW_REVIEW,
    payload: review
})

const editReview = (review) => ({
    type: EDIT_REVIEW,
    payload: review
})

//Review thunks

export const thunkGetAllReviews = (recipeId) => async (dispatch) => {
    const response = await fetch(`/api/recipes/${recipeId}/reviews`);
    if(response.ok) {
        const data = await response.json();
        dispatch(getAllReviews(data));
        return data;
    } else if (response.status < 500) {
        const data = await response.json();
        if(data.errors) {
            return data.errors;
        }
    } else {
        return ["An error occured. Please try again."]
    }
}


export const thunkCreateReview = (body, recipeId) => async (dispatch) => {
    const { review, stars, location, first_name, last_name } = body
    const response = await fetch(`/api/recipes/${recipeId}/reviews`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
            review: review,
            stars: stars,
            location: location,
            first_name: first_name,
            last_name: last_name
        })
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(createReview(data));
        return data;
      } else if (response.status < 500) {
        const data = await response.json();
        throw new Error(JSON.stringify(data));
    }

}

export const thunkEditReview = (body, reviewId) => async (dispatch) => {
    const { review, stars, location, first_name, last_name } = body
    console.log(body, 'body')
    console.log(reviewId, 'review id')
    const response = await fetch(`/api/reviews/${reviewId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            review: review,
            stars: stars,
            location: location,
            first_name: first_name,
            last_name: last_name
        })
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(editReview(data));
        return data;
      } else if (response.status < 500) {
        const data = await response.json();
        throw new Error(JSON.stringify(data));
    }
}


//Reducers
const initialState = {};
export default function reviewReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_REVIEWS: {
            const newState = {...state};
            action.payload.Reviews.forEach(review => {
                newState[review.id] = review;
            });
            return { Reviews: newState };
        }
        case CREATE_NEW_REVIEW: {
            const newState = Object.assign({}, state);
            newState[action.payload.id] = action.payload;
            return newState;
        }
        case EDIT_REVIEW: {
            const newState = Object.assign({}, state);
            newState[action.payload.id] = {...newState[action.payload.id], ...action.payload}
            return newState;
        }
        default:
            return state;
    }
}
