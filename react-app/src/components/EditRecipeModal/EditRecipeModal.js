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
    ingredient: item.ingredient,
    measurement_num: item.measurement_num,
    measurement_type: item.measurement_type,
  })),);
  const [kitchenwares, setKitchenwares] = useState(recipes.kitchenware.map((item) => ({
    name: item.name,
  })),);
  const [preparations, setPreparations] = useState(recipes.preparation.map((item) => ({
    description: item.description,
  })),);
  const [img_url, setImageUrl] = useState(recipes.img_url);
  const [errors, setErrors] = useState([]);
  const { closeModal } = useModal();

  const handleDelete = () => {
    dispatch(thunkDeleteRecipe(recipes.id))
    .then(() => {
      history.push('/recipes')
      closeModal()
    })
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrors([]);

    const body = {
      name,
      description,
      servings_num,
      img_url,
      ingredients: ingredients.map((item) => ({
        ingredient: item.ingredient,
        measurement_num: item.measurement_num,
        measurement_type: item.measurement_type,
      })),
      kitchenwares: kitchenwares.map((item) => ({
        name: item.name,
      })),
      preparations: preparations.map((item) => ({
        description: item.description,
      })),
    };

    try {
        await dispatch(thunkEditRecipe(body, recipes.id))
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
    <div className="Global-Modal-Container3">
      <div className="Global-Modal-Header">Edit a recipe</div>
      <form onSubmit={handleSubmit} className="Global-ModalForm-Container">
        <ul className="Global-Errors-UL">
          {errors.map((error, idx) => (
            <li key={idx} className="Global-Errors-LI">
              {error}
            </li>
          ))}
        </ul>


        <button type="button" onClick={() => setIngredients([
              ...ingredients,
              {
                measurement_num: "",
                measurement_type: "",
                ingredient: "",
              },
            ])
          }
        >
          Add Ingredient
        </button>
        {ingredients.map((item, idx) => (
            <div key={idx}>
              <label>
                Amount of Measurement
                <input
                  type="number"
                  value={item.measurement_num}
                  onChange={(e) => {
                    const newIngredients = [...ingredients];
                    newIngredients[idx].measurement_num= e.target.value;
                    setIngredients(newIngredients);
                  }}
                />
              </label>
              <label>
                Type of Measurement
                <input
                  type="text"
                  value={item.measurement_type}
                  onChange={(e) => {
                    const newIngredients = [...ingredients];
                    newIngredients[idx].measurement_type = e.target.value;
                    setIngredients(newIngredients);
                  }}
                />
              </label>
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
                />
              </label>
            </div>
        ))}

        <button type="button" onClick={() => setKitchenwares([
              ...kitchenwares,
              {
                name: "",
              },
            ])
          }
        >
          Add Things You'll Need
        </button>
        {kitchenwares.map((item, idx) => (
            <div key={idx} className="kitchenwares">
              <label>
                Things You'll Need
                <input
                  type="text"
                  value={item.name}
                  onChange={(e) => {
                    const newKitchenwares = [...kitchenwares];
                    newKitchenwares[idx].name = e.target.value;
                    setKitchenwares(newKitchenwares);
                  }}
                />
              </label>
            </div>
        ))}


        <button type="button" onClick={() => setPreparations([
              ...preparations,
              {
                description: "",
              },
            ])
          }
        >
          Add Instuctions
        </button>
        {preparations.map((item, idx) => (
          <div key={idx} className="preparations">
            <label>
              Instructions
              <input
                type="text"
                value={item.description}
                onChange={(e) => {
                  const newPreparations = [...preparations];
                  newPreparations[idx].description = e.target.value;
                  setPreparations(newPreparations);
                }}
              />
            </label>
          </div>
        ))}

        <label for="name" className="Global-Modal-Label">
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            placeholder="Name"
            className="Global-Modal-input"
          />
        </label>
        <label for="description" className="Global-Modal-Label">
          <textarea
            type="text"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
            placeholder="Description"
            className="Global-Modal-input"
          ></textarea>
        </label>
        <label for="serving_num" className="Global-Modal-Label">
          <input
            type="text"
            value={servings_num}
            onChange={(e) => setServingsNum(e.target.value)}
            required
            placeholder="Serving Size"
            className="Global-Modal-input"
          />
        </label>
        <label for="img_url" className="Global-Modal-Label">
          <input
            type="text"
            value={img_url}
            onChange={(e) => setImageUrl(e.target.value)}
            required
            placeholder="Image"
            className="Global-Modal-input"
          />
        </label>
        <button type="submit" className="Global-SubmitButton">
          Edit Recipe
        </button>
        <button onClick={handleDelete} type="submit" className='delete-button'>
          Delete
        </button>
      </form>
    </div>
  );
}

export default EditRecipeModalForm;
