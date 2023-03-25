//Actions
const GET_ALL_RECIPES = "recipes/get_all_recipes";
const GET_SINGLE_RECIPE = "recipes/get_single_recipe"
const CREATE_NEW_RECIPE = "recipes/create_new_recipe"
const EDIT_RECIPE = "recipes/edit_recipe"
const DELETE_RECIPE = "recipes/delete_recipe"

//Action creators
const getAllRecipes = (recipes) => ({
    type: GET_ALL_RECIPES,
    payload: recipes
})

const getSingleRecipe = (recipe) => ({
    type: GET_SINGLE_RECIPE,
    payload: recipe
})

const createRecipe = (recipe) => ({
    type: CREATE_NEW_RECIPE,
    payload: recipe
})

const editRecipe = (recipe) => ({
    type: EDIT_RECIPE,
    payload: recipe
})

const deleteRecipe = (recipe) => ({
    type: DELETE_RECIPE,
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
        console.log(data, 'data in get single recipes')
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


export const thunkCreateRecipe = (recipe) => async (dispatch) => {
    const { name, description, servings_num, img_url, ingredients, kitchenwares, preparations } = recipe;
    const response = await fetch(`/api/recipes/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            name: name,
            description: description,
            servings_num: servings_num,
            img_url: img_url,
            ingredients: ingredients,
            kitchenwares: kitchenwares,
            preparations: preparations
        })
    });

    if (response.ok) {
        const data = await response.json();
        console.log(data, 'lily')
        dispatch(createRecipe(data));
        console.log(data, 'rose')
        console.log(data['errors'], 'elephant')
        return data;
    }   else if (response.status < 500) {
        const data = await response.json();
        if (data["errors"]) {
            throw data;
        }
      } else {
            return ["An error occurred. Please try again."];
    }
}

export const thunkEditRecipe = (recipe, recipeId) => async (dispatch) => {
    const { name, description, servings_num, img_url, ingredients, kitchenwares, preparations, newKitchenware } = recipe;
    console.log(kitchenwares, 'kitchenware in edit thunk')
    const response = await fetch(`/api/recipes/${recipeId}`, {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            name: name,
            description: description,
            servings_num: servings_num,
            img_url: img_url,
            ingredients: ingredients,
            kitchenwares: kitchenwares,
            preparations: preparations,
            newKitchenware: newKitchenware
        })
    });

    // const response2 = await fetch(`/api/recipes/`, {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify({
    //         name: name,
    //         description: description,
    //         servings_num: servings_num,
    //         img_url: img_url,
    //         ingredients: ingredients,
    //         kitchenwares: kitchenwares,
    //         preparations: preparations
    //     })
    // });

    if (response.ok) {
        console.log('hi')
        const data = await response.json();
        dispatch(editRecipe(data));
        console.log(data, 'sparkle pants')
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


export const thunkDeleteRecipe = (recipeId) => async (dispatch) => {
    const response = await fetch(`/api/recipes/${recipeId}`, {
        method: 'DELETE',
    })

    if(response.ok) {
        const data = await response.json();
        dispatch(deleteRecipe(recipeId))
        return data;
    }
}


//Reducers
const initialState = {};
export default function recipeReducer(state = initialState, action) {
    // let newState;
    switch (action.type) {
        case GET_ALL_RECIPES: {
            const newState = {};
            action.payload.Recipes.forEach(recipe => {
                newState[recipe.id] = recipe;
            });
            return newState;
        }
        case GET_SINGLE_RECIPE: {
            const newState = Object.assign({}, state);
            action.payload.Recipes.forEach(recipe => {
                newState[recipe.id] = recipe;
            });
            return newState;
        }
        case CREATE_NEW_RECIPE: {
            const newState = Object.assign({}, state);
            newState[action.payload.id] = action.payload;
            return newState;
        }
        case EDIT_RECIPE: {
            const newState = Object.assign({}, state);
            newState[action.payload.id] = {...action.payload}
            return newState;
        }
        case DELETE_RECIPE: {
            const newState = Object.assign({}, state)
            delete newState[action.payload]
            return newState;
        }
        default:
            return state;
    }
}
