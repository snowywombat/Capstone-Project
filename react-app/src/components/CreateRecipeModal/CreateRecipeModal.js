import React from "react";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useHistory } from "react-router-dom";
import { thunkCreateRecipe } from "../../store/recipes";
import { useModal } from "../../context/Modal";
import "../LoginFormModal/LoginForm.css";
import "./CreateRecipeModal.css";

function CreateRecipeModalForm() {

  const dispatch = useDispatch();
  const history = useHistory();

  const [name, setName] = useState("");
  const [description, setDescription] = useState("");
  const [servings_num, setServingsNum] = useState("");
  const [ingredients, setIngredients] = useState([]);
  const [kitchenwares, setKitchenwares] = useState([]);
  const [preparations, setPreparations] = useState([]);
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
      await dispatch(thunkCreateRecipe(body))
      .then((data) => {
          closeModal()
          history.push(`/recipes/${data.id}`)
          history.go(0)
      })
    } catch (e) {
      const errorResponse = e.errors;
      const errorMessages = errorResponse.map((error) => error);
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
                  required
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
                  required
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
                  required
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
                  required
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
                required
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
            type="number"
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
          Add Recipe
        </button>
      </form>
    </div>
  );
}

export default CreateRecipeModalForm;
