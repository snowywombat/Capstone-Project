import React from "react";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { thunkCreateRecipe, thunkGetSingleRecipe } from "../../store/recipes";
import { thunkGetAllReviews } from "../../store/reviews";
import { useModal } from "../../context/Modal";
// import TextField from '@material-ui/core/TextField';
import "../LoginFormModal/LoginForm.css";
import "./CreateRecipeModal.css";
import { v4 as uuidv4 } from 'uuid';
import SingleRecipePage from "../SingleRecipePage";

function CreateRecipeModalForm() {

  const dispatch = useDispatch();
  const history = useHistory();

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [servings_num, setServingsNum] = useState("");
  const [ingredients, setIngredients] = useState([])
  const [kitchenwares, setKitchenwares] = useState([]);
  const [preparations, setPreparations] = useState([])
  const [img_url, setImageUrl] = useState("");
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const body = {
      name,
      description,
      servings_num,
      img_url,
      ingredients: ingredients.map((item) => ({
        id: item.id,
        ingredient: item.ingredient,
        measurement_num: parseInt(item.measurement_num),
        measurement_type: item.measurement_type,
        recipe_id: item.recipe_id
      })),
      kitchenwares: kitchenwares.map((item) => ({
        // id: item.id,
        name: item.name,
        // recipe_id: item.recipe_id

      })),
      preparations: preparations.map((item) => ({
        id: item.id,
        description: item.description,
        recipe_id: item.recipe_id
      })),
    };

    console.log(body, 'edit body')

    try {
      await dispatch(thunkCreateRecipe(body))
      .then((data) => {
          dispatch(thunkGetSingleRecipe(data.id))
          dispatch(thunkGetAllReviews(data.id))
          closeModal()
          history.push(`/recipes/${data.id}`)
      })
    } catch (e) {
      const errorResponse = e.errors;
      console.log(errorResponse, 'fish')
      const errorMessages = errorResponse.map((error) => error.split(": ")[1]);
      setErrors(errorMessages);
    }
  };

  return (
    <div className="Global-Modal-Container3">
      <div className="Global-Modal-Header">Add a new recipe</div>
      <form onSubmit={handleSubmit} className="Global-ModalForm-Container">
        <ul className="Global-Errors-UL">
          {errors.map((error, idx) => (
            <li key={idx} className="Global-Errors-LI">
              {error}
            </li>
          ))}
        </ul>

        <div className='ingredient-name'>
          Add Ingredient
        </div>
        <button type="button" className='add-button' onClick={() => setIngredients([
              ...ingredients,
              {
                measurement_num: "",
                measurement_type: "",
                ingredient: "",
              },
            ])
          }
        >
          <i class="fa-solid fa-circle-plus" style={{fontSize: 25}}></i>
        </button>

        {ingredients.map((item, idx) => (
            <div key={idx}>

              <div className='recipe-text-fields'>
                <label>
                  Measurement Amount
                  <input
                    value={item.measurement_num}
                    onChange={(e) => { const newIngredients = [...ingredients];
                      newIngredients[idx].measurement_num= e.target.value;
                      setIngredients(newIngredients);
                    }}
                    type="number"
                    required
                  />
                </label>
              </div>

              <div className='recipe-text-fields'>
                <label>
                  Meaurement Type
                  <input
                    value={item.measurement_type}
                    onChange={(e) => {
                      const newIngredients = [...ingredients];
                      newIngredients[idx].measurement_type = e.target.value;
                      setIngredients(newIngredients);
                    }}
                    required
                  />
                </label>
              </div>

              <div className='recipe-text-fields'>
              <label>
                Ingredient
                <input
                  type="text"
                  value={item.ingredient}
                  onChange={(e) => {
                    const newIngredients = [...ingredients];
                    newIngredients[idx].ingredient = e.target.value;
                    setIngredients(newIngredients);
                  }}
                  required
                />
              </label>
              </div>

            </div>
        ))}

        <div className='kitchenware-name'>
          Add Things You'll Need
        </div>
        <button type="button" className='add-button' onClick={() => setKitchenwares([
              ...kitchenwares,
              {
                name: "",
              },
            ])
          }
        >
          <i class="fa-solid fa-circle-plus" style={{fontSize: 25}}></i>
        </button>
        {kitchenwares.map((item, idx) => (
            <div key={idx} className="recipe-text-fields">
              <label>
                Kitchen Item
                <input
                  type="text"
                  value={item.name}
                  onChange={(e) => {
                    const newKitchenwares = [...kitchenwares];
                    newKitchenwares[idx].name = e.target.value;
                    setKitchenwares(newKitchenwares);
                  }}
                  required
                />
              </label>
            </div>
        ))}

        <div className='preparation-name'>
          Add Instuctions
        </div>
        <button type="button" className='add-button' onClick={() => setPreparations([
              ...preparations,
              {
                description: "",
              },
            ])
          }
        >
          <i class="fa-solid fa-circle-plus" style={{fontSize: 25}}></i>
        </button>
        {preparations.map((item, idx) => (
          <div key={idx} className="recipe-text-fields">
            <label>
              Step {idx + 1}
              <input
                type="text"
                value={item.description}
                onChange={(e) => {
                  const newPreparations = [...preparations];
                  newPreparations[idx].description = e.target.value;
                  setPreparations(newPreparations);
                }}
                required
              />
            </label>
          </div>
        ))}

        <label for="name" className="Global-Modal-Label">
          Name
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            // placeholder="Name"
            className="Global-Modal-input"
          />
        </label>
        <label for="description" className="Global-Modal-Label">
          Description
          <textarea
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
            // placeholder="Description"
            className="Global-Modal-input"
          ></textarea>
        </label>
        <label for="serving_num" className="Global-Modal-Label">
          Serving Size
          <input
            type="number"
            value={servings_num}
            onChange={(e) => setServingsNum(e.target.value)}
            required
            // placeholder="Serving Size"
            className="Global-Modal-input"
          />
        </label>
        <label for="img_url" className="Global-Modal-Label">
          Upload Image
          <input
            type="text"
            value={img_url}
            onChange={(e) => setImageUrl(e.target.value)}
            required
            // placeholder="Image"
            className="Global-Modal-input"
          />
        </label>
        <button type="submit" className="Global-SubmitButton">
          Add Recipe
        </button>
      </form>
    </div>
  );
}

export default CreateRecipeModalForm;
