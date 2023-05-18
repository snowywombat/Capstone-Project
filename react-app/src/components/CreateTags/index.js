import React from "react";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { thunkGetSingleRecipe } from "../../store/recipes";
import { thunkCreateTag, thunkGetAllTags} from "../../store/tags";
import './CreateTags.css'

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
            .then(() => setTagName(''))
        } catch (e) {
          const errorResponse = e.errors;
          const errorMessages = errorResponse.map((error) => error);
          setErrors(errorMessages);
        }
    };

    return (
        <div className="tag-container">
          {/* <div className="tag-header">Add tags to your recipe below!</div> */}
          <form onSubmit={handleSubmit} className="tag-form">

            <div className='tag-field'>


              <label>Add tags to your recipe below!</label>


              <ul>
                {errors.map((error, idx) => (
                    <li className='errors-div' key={idx}>{error}</li>
                ))}
              </ul>


              <div className='tag-input-div'>
                <input
                  value={tag_name}
                  onChange={(e) => setTagName(e.target.value)}
                  required
                  placeholder="delicious"
                  className='tag-input'
                />
              </div>
            </div>




            <button type="submit" className="tag-submit-button">
              Add Tag
            </button>

          </form>
        </div>
      );


}

export default CreateTagForm;
