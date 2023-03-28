import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { thunkEditRecipe } from "../../store/recipes";
import { thunkDeleteRecipe } from "../../store/recipes";
import { thunkGetSingleRecipe } from "../../store/recipes";
import { useModal } from "../../context/Modal";
import "../LoginFormModal/LoginForm.css";
import "./EditRecipeModal.css";

function EditRecipeModalForm({ recipes }) {

  const dispatch = useDispatch();
  const history = useHistory();

  const [name, setName] = useState(recipes.name);
  const [description, setDescription] = useState(recipes.description);
  const [servings_num, setServingsNum] = useState(recipes.servingSize);
  const [ingredients, setIngredients] = useState(recipes.ingredients.map((item) => ({
    id: item.id,
    ingredient: item.ingredient,
    measurement_num:parseFloat(item.measurement_num).toFixed(0),
    measurement_type: item.measurement_type,
    recipe_id: item.recipe_id
  })),);
  const [kitchenwares, setKitchenwares] = useState(recipes.kitchenware.map((item) => ({
    id: item.id,
    name: item.name,
    recipe_id: item.recipe_id
  })),);
  const [preparations, setPreparations] = useState(recipes.preparation.map((item) => ({
    id: item.id,
    description: item.description,
    recipe_id: item.recipe_id
  })),);
  const [img_url, setImageUrl] = useState(recipes.img_url);
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();
  const [newKitchenware, setNewKitchenware] = useState([])

  const newKitchenwares = () => {
    setKitchenwares([
      ...kitchenwares,
    ])
    setNewKitchenware([
      ...newKitchenware,
      {
        name: "",
        recipe_id: recipes.id
      },
    ])
  }

  console.log(newKitchenware, 'newKitchenware')

  const handleDelete = () => {
    dispatch(thunkDeleteRecipe(recipes.id))
    .then(() => {
      history.push('/recipes')
      closeModal()
    })
  }

  const handleClick = () => {
    const confirmed = window.confirm("Are you sure you want to delete the recipe?");
    if (confirmed) {
      handleDelete();
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const recipe = {
      name,
      description,
      servings_num,
      img_url,
      ingredients,
      kitchenwares,
      preparations,
      newKitchenware
    };

    try {
        await dispatch(thunkEditRecipe(recipe, recipes.id))
          .then(() => dispatch(thunkGetSingleRecipe(recipes.id)))
          .then(() => {
            closeModal()
          })
    } catch (e) {
        const errorResponse = e.errors;
        const errorMessages = errorResponse.map((error) => error.split(": ")[1]);
        setErrors(errorMessages);
    }
  };


  return (
    <div className="Global-Modal-Container">
      <div className="Global-Modal-Header">Edit a recipe</div>
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
          variant="outlined"
          className="Global-Modal-input"
        />


        <label className='form-labels form-lables-exclude-first'>Add a description:</label>
        <input
          type="text"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          required
          variant="outlined"
          multiline
          minRows={3}
          className="Global-Modal-input"
        />


        <label className='form-labels form-lables-exclude-first'>Serving size:</label>
        <input
          type="number"
          value={servings_num}
          onChange={(e) => setServingsNum(e.target.value)}
          required
          variant="outlined"
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
                type="number"
                value={item.measurement_num}
                onChange={(e) => {
                  const newIngredients = [...ingredients];
                  newIngredients[idx].measurement_num= e.target.value;
                  setIngredients(newIngredients);
                }}
                required

              />

              <input
                className='measurement-type-field'
                label='Measurement Type'
                type="text"
                value={item.measurement_type}
                onChange={(e) => {
                  const newIngredients = [...ingredients];
                  newIngredients[idx].measurement_type = e.target.value;
                  setIngredients(newIngredients);
                }}
                required
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
          <i className="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
        </button>


        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>


        <div className='form-labels form-lables-exclude-first'>
          Add Things You'll Need:
        </div>

        <div className='sub-fields'>
          {kitchenwares.map((item, idx) => (
            <div key={item.id} className="individual-sub-fields">

              <input
                key={item.id}
                label= "Kitchen Item"
                type="text"
                value={item.name}
                onChange={(e) => {
                  const oldKitchenwares = [...kitchenwares];
                  oldKitchenwares[idx] = { ...oldKitchenwares[idx], name: e.target.value };
                  setKitchenwares(oldKitchenwares);
                }}
                required
              />
            </div>
          ))}

          {newKitchenware.map((item, idx) => (
            <div key={item.id} className="individual-sub-fields">

              <input
                key={item.id}
                label= "Kitchen Item"
                type="text"
                value={item.name}
                onChange={(e) => {
                  const newKitchenwares = [...newKitchenware];
                  newKitchenwares[idx] = { ...newKitchenwares[idx], name: e.target.value };
                  setNewKitchenware(newKitchenwares);
                }}
                required
              />
            </div>
          ))}

        </div>

        <button type="button" className='add-button' onClick={newKitchenwares}>
          <i className="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
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
          <i className="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
        </button>

        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>

        <label className='form-labels form-lables-exclude-first'>Upload Image:</label>
        <input
          className="Global-Modal-input"
          type="text"
          value={img_url}
          onChange={(e) => setImageUrl(e.target.value)}
          required
        />

        <button type="submit" className="Global-SubmitButton">
          Edit Recipe
        </button>
        <button onClick={handleClick} type="submit" className='edit-delete-button'>
          Delete
        </button>
      </form>
    </div>
  );
}

export default EditRecipeModalForm;
