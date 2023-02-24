import { NavLink } from "react-router-dom";

const AllRecipeCards = ({ recipe }) => {
  let { id, name, description, servings_num, img_url } = recipe;

  if (img_url && img_url === "No images uploaded yet")
    img_url =
      "https://img.freepik.com/premium-vector/modern-minimal-found-error-icon-oops-page-found-404-error-page-found-with-concept_599740-716.jpg?w=2000";

  return (
    <NavLink to={`/recipes/${id}`}>
      <div className="card-holder" style={ {backgroundImage:`url(${img_url})`} }>
        <div className="content-holder">
          <div className="allRecipesName">{name}</div>
          <div className="allRecipesDescription">{description}</div>
          <div className="allRecipesServingsNum">{servings_num}</div>
        </div>
      </div>
    </NavLink>
  );
};

export default AllRecipeCards;
