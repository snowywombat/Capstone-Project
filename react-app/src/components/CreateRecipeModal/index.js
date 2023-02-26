import OpenModalButton from "../OpenModalButton";
import CreateRecipeModalForm from "./CreateRecipeModal";
import "./CreateRecipeModal.css"

const CreateRecipeModal = () => {
  return (
    <div className="createRecipeBox">
      <OpenModalButton
        buttonText="Add a recipe"
        modalComponent={<CreateRecipeModalForm />}
        className="CreateRecipe-Button"
      />
    </div>
  );
};

export default CreateRecipeModal;
