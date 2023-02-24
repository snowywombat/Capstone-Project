//Actions
const GET_ALL_RECIPES = "recipes/get_all_recipes";
const GET_SINGLE_RECIPE = "recipes/get_single_recipe"


//Action creators
const getAllRecipes = (recipes) => ({
    type: GET_ALL_RECIPES,
    payload: recipes
})

const getSingleRecipe = (recipe) => ({
    type: GET_SINGLE_RECIPE,
    payload: recipe
})


//Recipe thunks
export const thunkGetAllRecipes = () => async (dispatch) => {
    const response = await fetch(`/api/recipes`);
    if(response.ok) {
        const data = await response.json();
        dispatch(getAllRecipes(data));
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

export const thunkGetSingleRecipe = (recipeId) => async (dispatch) => {
    const response = await fetch(`/api/recipes/${recipeId}`);
    if(response.ok) {
        const data = await response.json();
        console.log(data, 'datatatata')
        dispatch(getSingleRecipe(data));
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

//Reducers
const initialState = {};
export default function recipeReducer(state = initialState, action) {
    // let newState;
    switch (action.type) {
        case GET_ALL_RECIPES: {
            const newState = {...state};
            action.payload.Recipes.forEach(recipe => {
                newState[recipe.id] = recipe;
            });
            return {Recipes: newState};
        }
        case GET_SINGLE_RECIPE: {
            return { ...state.recipes, recipeDetails: action.payload }
        }
        default:
            return state;
    }
}
