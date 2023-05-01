//Actions
const GET_ALL_TAGS = "tags/get_all_tags"
const CREATE_NEW_TAG = "tags/create_new_tag"
const DELETE_TAG = "tags/delete_tag"

//Action creators
const getAllTags = (tags) => ({
    type: GET_ALL_TAGS,
    payload: tags
})

const createTag = (tag) => ({
    type: CREATE_NEW_TAG,
    payload: tag
})

const deleteTag = (tag) => ({
    type: DELETE_TAG,
    payload: tag
})


export const thunkGetAllTags = (recipeId) => async (dispatch) => {
    const response = await fetch(`/api/recipes/${recipeId}/tags`);
    if(response.ok) {
        const data = await response.json();
        dispatch(getAllTags(data));
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

export const thunkCreateTag = (body, recipeId) => async (dispatch) => {
    const { tag_name } = body
    const response = await fetch(`/api/recipes/${recipeId}/tags`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
            tag_name: tag_name
        })
    });
    if (response.ok) {
        const data = await response.json();
        dispatch(createTag(data));
        return data;
      } else if (response.status < 500) {
        const data = await response.json();
        if (data.errors) {
            throw data;
        }
      } else {
            return ["An error occurred. Please try again."];
    }
}


export const thunkDeleteTag = (tagId) => async (dispatch) => {
    const response = await fetch(`/api/tags/${tagId}`, {
        method: 'DELETE',
    })

    if(response.ok) {
        const data = await response.json();
        dispatch(deleteTag(tagId))
        return data;
    }
}


//Reducers
const initialState = {};
export default function tagReducer(state = initialState, action) {
    switch (action.type) {
        case GET_ALL_TAGS: {
            const newState = {};
            action.payload.Tags.forEach(tag => {
                newState[tag.id] = tag;
            });
            return newState;
        }
        case CREATE_NEW_TAG: {
            const newState = Object.assign({}, state);
            newState[action.payload.id] = action.payload;
            return newState;
        }
        case DELETE_TAG: {
            const newState = Object.assign({}, state)
            delete newState[action.payload]
            return newState;
        }
        default:
            return state;
    }
}
