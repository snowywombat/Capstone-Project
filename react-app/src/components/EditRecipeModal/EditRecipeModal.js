import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { thunkEditRecipe } from "../../store/recipes";
import { thunkDeleteRecipe } from "../../store/recipes";
import { thunkGetSingleRecipe } from "../../store/recipes";
import { useModal } from "../../context/Modal";
import TextField from '@material-ui/core/TextField';
import InputAdornment from '@material-ui/core/InputAdornment';
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
  const [newIngredient, setNewIngredient] = useState([])
  const [newPreparation, setNewPreparation] = useState([])

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

  const newIngredients = () => {
    setIngredients([
      ...ingredients,
    ])
    setNewIngredient([
      ...newIngredient,
      {
        measurement_num: "",
        measurement_type: "",
        ingredient: "",
        recipe_id: recipes.id
      },
    ])
  }

  const newPreparations = () => {
    setPreparations([
      ...preparations,
    ])
    setNewPreparation([
      ...newPreparation,
      {
        description: "",
        recipe_id: recipes.id
      }
    ])
  }

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
      newKitchenware,
      newIngredient,
      newPreparation
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
        <TextField
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
          variant="outlined"
          className="Global-Modal-input"
        />


        <label className='form-labels form-lables-exclude-first'>Add a description:</label>
        <TextField
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
        <TextField
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


        {/* <div className='form-labels form-lables-exclude-first'>
          Add Ingredient:
        </div>


        <div className='sub-fields'>
          {ingredients.map((item, idx) => (
            <div key={item.id} className='individual-sub-fields'>

              <TextField
                key={item.id}
                label="Measurement Amount"
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  )
                }}
                value={item.measurement_num}
                onChange={(e) => {
                  const oldIngredients = [...ingredients];
                  oldIngredients[idx] = { ...oldIngredients[idx], measurement_num: e.target.value };
                  setIngredients(oldIngredients);
                }}
                type="number"
                // required
                variant="outlined"
              />

              <TextField
                key={item.id}
                label='Measurement Type'
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  ),
                }}
                type="text"
                value={item.measurement_type}
                onChange={(e) => {
                  const oldIngredients = [...ingredients];
                  oldIngredients[idx] = { ...oldIngredients[idx], measurement_type: e.target.value };
                  setIngredients(oldIngredients);
                }}
                // required
                variant="outlined"
              />


              <TextField
                key={item.id}
                label='Ingredient'
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  ),
                }}
                type="text"
                value={item.ingredient}
                onChange={(e) => {
                  const oldIngredients = [...ingredients];
                  oldIngredients[idx] = { ...oldIngredients[idx], ingredient: e.target.value };
                  setIngredients(oldIngredients);;
                }}
                // required
                variant="outlined"
              />
            </div>
          ))}

          {newIngredient.map((item, idx) => (
            <div key={item.id} className="individual-sub-fields">

              <TextField
                key={item.id}
                label= "Measurement Amount"
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  ),
                }}
                type="number"
                value={item.measurement_num}
                onChange={(e) => {
                  const newIngredients = [...newIngredient];
                  newIngredients[idx] = { ...newIngredients[idx], measurement_num: e.target.value };
                  setNewIngredient(newIngredients);
                }}
                // required
                variant="outlined"
              />

              <TextField
                key={item.id}
                label= "Measurement Type"
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  ),
                }}
                type="text"
                value={item.measurement_type}
                onChange={(e) => {
                  const newIngredients = [...newIngredient];
                  newIngredients[idx] = { ...newIngredients[idx], measurement_type: e.target.value };
                  setNewIngredient(newIngredients);
                }}
                // required
                variant="outlined"
              />

              <TextField
                key={item.id}
                label= "Ingredient"
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  ),
                }}
                type="text"
                value={item.ingredient}
                onChange={(e) => {
                  const newIngredients = [...newIngredient];
                  newIngredients[idx] = { ...newIngredients[idx], ingredient: e.target.value };
                  setNewIngredient(newIngredients);
                }}
                // required
                variant="outlined"
              />
            </div>
          ))}
        </div>

        <button type="button" className='add-button' onClick={newIngredients}>
          <i className ="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
        </button> */}


        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>


        <div className='form-labels form-lables-exclude-first'>
          Add Things You'll Need:
        </div>

        <div className='sub-fields'>
          {kitchenwares.map((item, idx) => (
            <div key={item.id} className="individual-sub-fields">

              <TextField
                key={item.id}
                label= "Kitchen Item"
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  ),
                }}
                type="text"
                value={item.name}
                onChange={(e) => {
                  const oldKitchenwares = [...kitchenwares];
                  oldKitchenwares[idx] = { ...oldKitchenwares[idx], name: e.target.value };
                  setKitchenwares(oldKitchenwares);
                }}
                // required
                variant="outlined"
              />
            </div>
          ))}

          {newKitchenware.map((item, idx) => (
            <div key={item.id} className="individual-sub-fields">

              <TextField
                key={item.id}
                label= "Kitchen Item"
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  ),
                }}
                type="text"
                value={item.name}
                onChange={(e) => {
                  const newKitchenwares = [...newKitchenware];
                  newKitchenwares[idx] = { ...newKitchenwares[idx], name: e.target.value };
                  setNewKitchenware(newKitchenwares);
                }}
                // required
                variant="outlined"
              />
            </div>
          ))}

        </div>

        <button type="button" className='add-button' onClick={newKitchenwares}>
          <i className ="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
        </button>


        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>


        {/* <div className='form-labels form-lables-exclude-first'>
          Add Instuctions:
        </div>

        <div className='sub-fields'>
          {preparations.map((item, idx) => (
            <div key={item.id} className="individual-sub-fields">

              <TextField
                key={item.id}
                label= {`Step ${idx + 1}`}
                InputProps={{
                    startAdornment: (
                      <InputAdornment position="start">

                      </InputAdornment>
                    ),
                  }}
                type="text"
                value={item.description}
                onChange={(e) => {
                  const oldPreparations = [...preparations];
                  oldPreparations[idx] = { ...oldPreparations[idx], description: e.target.value };
                  setPreparations(oldPreparations);
                }}
                // required
                variant="outlined"
              />
            </div>
          ))}


          {newPreparation.map((item, idx) => (
            <div key={item.id} className="individual-sub-fields">
              {preparations.map((prep, idx) => (

              <TextField
                key={item.id}
                label= {`Step ${prep.id + 1}`}
                InputProps={{
                  startAdornment: (
                    <InputAdornment position="start">

                    </InputAdornment>
                  ),
                }}
                type="text"
                value={item.description}
                onChange={(e) => {
                  const newPreparations = [...newPreparation];
                  newPreparations[idx] = { ...newPreparations[idx], description: e.target.value };
                  setNewPreparation(newPreparations);
                }}
                // required
                variant="outlined"
              />
              ))}
            </div>
          ))}

        </div>

        <button type="button" className='add-button' onClick={newPreparations}>
          <i className ="fa-solid fa-circle-plus" style={{fontSize: 30}}></i>
        </button> */}

        <div className='form-divider'>
          ––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
        </div>

        <label className='form-labels form-lables-exclude-first'>Upload Image:</label>
        <TextField
          type="text"
          value={img_url}
          onChange={(e) => setImageUrl(e.target.value)}
          required
          variant="outlined"
          className="Global-Modal-input"
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
