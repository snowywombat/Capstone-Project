import React from "react";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { thunkCreateRecipe, thunkGetSingleRecipe } from "../../store/recipes";
import { thunkGetAllReviews } from "../../store/reviews";
import { useModal } from "../../context/Modal";
import "../LoginFormModal/LoginForm.css";
import "./CreateRecipeModal.css";
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
      <div className="Global-Modal-Description">Fill out the form below to share your recipe!</div>
      <form onSubmit={handleSubmit} className="Global-ModalForm-Container">
        <ul className="Global-Errors-UL">
          {errors.map((error, idx) => (
            <li key={idx} className="Global-Errors-LI">
              {error}
            </li>
          ))}
        </ul>


        <label className='form-labels'>Name of your recipe:</label>
        <input
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          placeholder="Spaghetti & Meatballs"
          className="Global-Modal-input"
        />


        <label className='form-labels form-lables-exclude-first'>Add a description:</label>
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
          placeholder="Juicy meatballs made with ground beef, breadcrumbs..."
          className="Global-Modal-input"
        />


        <label className='form-labels form-lables-exclude-first'>Serving size:</label>
        <input
          type="number"
          value={servings_num}
          onChange={(e) => setServingsNum(e.target.value)}
          required
          placeholder="4"
          className="Global-Modal-input"
        />

        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>


        <div className='form-labels form-lables-exclude-first'>
          Add Ingredient:
        </div>


        <div className='sub-fields'>
          {ingredients.map((item, idx) => (
            <div key={idx} className='individual-sub-fields'>

              <input
                className='measurement-amount-field'
                label="Measurement Amount"
                value={item.measurement_num}
                onChange={(e) => { const newIngredients = [...ingredients];
                  newIngredients[idx].measurement_num= e.target.value;
                  setIngredients(newIngredients);
                }}
                type="number"
                required
                placeholder="3"
              />

              <input
                className='measurement-type-field'
                label='Measurement Type'
                value={item.measurement_type}
                onChange={(e) => {
                  const newIngredients = [...ingredients];
                  newIngredients[idx].measurement_type = e.target.value;
                  setIngredients(newIngredients);
                }}
                required
                placeholder="cups"
              />


              <input
                label='Ingredient'
                type="text"
                value={item.ingredient}
                onChange={(e) => {
                  const newIngredients = [...ingredients];
                  newIngredients[idx].ingredient = e.target.value;
                  setIngredients(newIngredients);
                }}
                required
                placeholder="flour"
              />
            </div>
          ))}
        </div>

        <button type="button" className='add-button' onClick={() => setIngredients([
          ...ingredients,
            {
              measurement_num: "",
              measurement_type: "",
              ingredient: "",
            },
          ])}
        >
          <i className ="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
        </button>


        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>


        <div className='form-labels form-lables-exclude-first'>
          Add Things You'll Need:
        </div>

        <div className='sub-fields'>
          {kitchenwares.map((item, idx) => (
              <div key={idx} className="individual-sub-fields">

                <input
                  label= "Kitchen Item"
                  type="text"
                  value={item.name}
                  onChange={(e) => {
                    const newKitchenwares = [...kitchenwares];
                    newKitchenwares[idx].name = e.target.value;
                    setKitchenwares(newKitchenwares);
                  }}
                  required
                  placeholder='12" sheet pan'
                />
              </div>
          ))}
        </div>

        <button type="button" className='add-button' onClick={() => setKitchenwares([
          ...kitchenwares,
            {
              name: "",
            },
          ])}
        >
          <i className ="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
        </button>


        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>


        <div className='form-labels form-lables-exclude-first'>
          Add Instuctions:
        </div>

        <div className='sub-fields'>
          {preparations.map((item, idx) => (
            <div key={idx} className="individual-sub-fields">

              <input
                label= {`Step ${idx + 1}`}
                type="text"
                value={item.description}
                onChange={(e) => {
                  const newPreparations = [...preparations];
                  newPreparations[idx].description = e.target.value;
                  setPreparations(newPreparations);
                }}
                required
                placeholder='Add step here'

              />
            </div>
          ))}
        </div>

        <button type="button" className='add-button' onClick={() => setPreparations([
          ...preparations,
            {
              description: "",
            },
          ])}
        >
          <i className ="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
        </button>

        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>

        <label className='form-labels form-lables-exclude-first'>Upload Image:</label>

        <input
          type="text"
          value={img_url}
          onChange={(e) => setImageUrl(e.target.value)}
          required
          placeholder="example.jpg"
          className="Global-Modal-input"
        />


        <button type="submit" className="Global-SubmitButton">
          Add Recipe
        </button>

      </form>
    </div>
  );
}

export default CreateRecipeModalForm;
