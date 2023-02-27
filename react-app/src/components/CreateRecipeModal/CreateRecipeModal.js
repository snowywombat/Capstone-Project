import React from "react";
import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
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
      img_url
    };

    dispatch(thunkCreateRecipe(body))
      .then((data) => {
          closeModal()
          history.push(`/recipes/${data.id}`)
          history.go(0)
      })
      .catch(
          async (res) => {
              const data = await res.json();
              if (data && data.errors) setErrors(data.errors);
          }
      );

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
          Add Recipe
        </button>
      </form>
    </div>
  );
}

export default CreateRecipeModalForm;
