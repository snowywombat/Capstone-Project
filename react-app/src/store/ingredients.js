const GET_ALL_INGREDIENTS = "ingredients/get_all_ingredients"
const GET_SINGLE_INGREDIENT = "ingredients/get_single_ingredient"
const DELETE_INGREDIENT = "ingredients/delete_ingredient"

const getAllIngredients = (ingredients) => ({
    type: GET_ALL_INGREDIENTS,
    payload: ingredients
})

const getSingleIngredient = (ingredient) => ({
    type: GET_SINGLE_INGREDIENT,
    payload: ingredient
})

const deleteIngredient = (ingredient) => ({
    type: DELETE_INGREDIENT,
    payload: ingredient
})


export const thunkGetAllIngredients = (recipeId) => async (dispatch) => {
    const response = await fetch(`/api/recipes/${recipeId}/ingredients`);
    if(response.ok) {
        const data = await response.json();
        dispatch(getAllIngredients(data));
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

export const thunkSingleIngredient = (ingredientId) => async (dispatch) => {
    const response = await fetch(`/api/recipes/ingredients/${ingredientId}`)

    if(response.ok) {
        const data = await response.json();
        dispatch(getSingleIngredient(data));
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

export const thunkDeleteIngredient = (recipeId, ingredientId, closeModal = true) => async (dispatch) => {
    const response = await fetch(`/api/recipes/${recipeId}/ingredients/${ingredientId}`, {
        method: 'DELETE',
    })

    if(response.ok) {
        const data = await response.json();
        dispatch(deleteIngredient(ingredientId))
        return data;
    }
}

const initialState = {};
export default function ingredientReducer(state = initialState, action) {
    // let newState;
    switch (action.type) {
        case GET_ALL_INGREDIENTS: {
            const newState = {};
            action.payload.Ingredients.forEach(ingredient => {
                newState[ingredient.id] = ingredient;
            });
            return newState;
        }
        case GET_SINGLE_INGREDIENT: {
            const newState = Object.assign({}, state);
            action.payload.Ingredient.forEach(item => {
                newState[item.id] = item;
            });
            return newState;
        }
        case DELETE_INGREDIENT: {
            const newState = Object.assign({}, state)
            delete newState[action.payload]
            return newState;
        }
        default:
            return state;
    }
}
