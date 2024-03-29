import { NavLink } from "react-router-dom";
import './AllRecipeCards.css'

const AllRecipeCards = ({ recipe }) => {
  let { id, name, description, servings_num, img_url } = recipe;

  if (img_url && img_url === "No images uploaded yet")
    img_url =
      "https://img.freepik.com/premium-vector/modern-minimal-found-error-icon-oops-page-found-404-error-page-found-with-concept_599740-716.jpg?w=2000";

  return (
    <NavLink to={`/recipes/${id}`} className='recipe-card-nav-link'>
      <div className="card-holder">
        <img src={img_url} alt={description} className='recipe-images'></img>
        <div className="content-holder">
          <div className="allRecipesName">{name}</div>
          <div className="allRecipesDescription">{description}</div>
        </div>
      </div>
    </NavLink>
  );
};

export default AllRecipeCards;
