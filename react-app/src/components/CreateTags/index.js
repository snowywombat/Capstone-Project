import React from "react";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { thunkGetSingleRecipe } from "../../store/recipes";
import { thunkCreateTag, thunkGetAllTags} from "../../store/tags";

function CreateTagForm({ recipe }) {

    const dispatch = useDispatch();

    const [tag_name, setTagName] = useState("");
    const [errors, setErrors] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrors([]);

        const body = {
          tag_name
        };


        try {
          await dispatch(thunkCreateTag(body, recipe.id))
            .then(() => dispatch(thunkGetSingleRecipe(recipe.id)))
            .then(() => dispatch(thunkGetAllTags(recipe.id)))
        } catch (e) {
          const errorResponse = e.errors;
          console.log(errorResponse, 'error Response')
          const errorMessages = errorResponse.map((error) => error);
          setErrors(errorMessages);
        }
    };

    return (
        <div className="tag-container">
          <div className="tag-header">Add a new tag</div>
          <form onSubmit={handleSubmit} className="tag-form">
            <ul>
                        {errors.map((error, idx) => (
                            <li className='errors-div' key={idx}>{error}</li>
                        ))}
                    </ul>

            <div className='tag-field'>
              <label>Tag Name:</label>
              <input
                value={tag_name}
                onChange={(e) => setTagName(e.target.value)}
                required
                placeholder="delicious"
              />
            </div>


            <button type="submit" className="tag-submit-button">
              Add Tag
            </button>

          </form>
        </div>
      );


}

export default CreateTagForm;
