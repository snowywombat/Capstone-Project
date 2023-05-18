const GET_ALL_CULTURES = "cultures/get_all_cultures";
const GET_SINGLE_CULTURE = "cultures/get_single_culture"
const CREATE_NEW_CULTURE = "cultures/create_new_culture"
const EDIT_CULTURE = "cultures/edit_culture"
const DELETE_CULTURE = "cultures/delete_culture"

//Action creators
const getAllCultures = (cultures) => ({
    type: GET_ALL_CULTURES,
    payload: cultures
})

const getSingleCulture = (culture) => ({
    type: GET_SINGLE_CULTURE,
    payload: culture
})

const createCulture = (culture) => ({
    type: CREATE_NEW_CULTURE,
    payload: culture
})

const editCulture = (culture) => ({
    type: EDIT_CULTURE,
    payload: culture
})

const deleteCulture = (culture) => ({
    type: DELETE_CULTURE,
    payload: culture
})


//Culture thunks
export const thunkGetAllCultures = () => async (dispatch) => {
    const response = await fetch(`/api/cultures`);
    if(response.ok) {
        const data = await response.json();
        dispatch(getAllCultures(data));
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

export const thunkGetSingleCulture = (cultureId) => async (dispatch) => {
    const response = await fetch(`/api/cultures/${cultureId}`);
    if(response.ok) {
        const data = await response.json();
        dispatch(getSingleCulture(data));
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

export const thunkCreateCulture = (culture) => async (dispatch) => {
    const { title, description, banner_img, article } = culture;
    const response = await fetch(`/api/cultures/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title: title,
            description: description,
            banner_img: banner_img,
            article: article,
        })
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(createCulture(data));
        return data;
    }   else if (response.status < 500) {
        const data = await response.json();
        if(data.errors) {
            return data.errors;
        }
      } else {
            return ["An error occurred. Please try again."];
    }
}


export const thunkEditCulture = (culture, cultureId) => async (dispatch) => {
    const { title, description, banner_img, article } = culture;
    const response = await fetch(`/api/cultures/${cultureId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            title: title,
            description: description,
            banner_img: banner_img,
            article: article,
        })
    });

    if (response.ok) {
        const data = await response.json();
        dispatch(editCulture(data));
        return data;
    }   else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) {
            throw data;
        }
      } else {
            return ["An error occurred. Please try again."];
    }
}


export const thunkDeleteCulture = (cultureId) => async (dispatch) => {
    const response = await fetch(`/api/cultures/${cultureId}`, {
        method: 'DELETE',
    })

    if(response.ok) {
        const data = await response.json();
        dispatch(deleteCulture(cultureId))
        return data;
    }
}


//Reducers
const initialState = {};
export default function cultureReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_CULTURES: {
            const newState = {};
            action.payload.Articles.forEach(article => {
                newState[article.id] = article;
            });
            return newState;
        }
        case GET_SINGLE_CULTURE: {
            const newState = Object.assign({}, state);
            action.payload.Article.forEach(article => {
                newState[article.id] = article;
            });
            return newState;
        }
        case CREATE_NEW_CULTURE: {
            const newState = Object.assign({}, state);
            newState[action.payload.id] = action.payload;
            return newState;
        }
        case EDIT_CULTURE: {
            const newState = Object.assign({}, state);
            newState[action.payload.id] = {...action.payload}
            return newState;
        }
        case DELETE_CULTURE: {
            const newState = Object.assign({}, state)
            delete newState[action.payload]
            return newState;
        }
        default:
            return state;
    }
}
