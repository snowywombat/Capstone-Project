import { NavLink } from "react-router-dom";

const AllCultureCards = ({ culture }) => {
  let { id, title, description, banner_img, article } = culture;

  if (banner_img && banner_img === "No image uploaded yet")
    banner_img =
      "https://img.freepik.com/premium-vector/modern-minimal-found-error-icon-oops-page-found-404-error-page-found-with-concept_599740-716.jpg?w=2000";

  return (
    <NavLink to={`/culture/${id}`} className='recipe-card-nav-link'>
      <div className="card-holder">
        <img src={banner_img} alt={description} className='recipe-images'></img>
        <div className="content-holder">
          <div className="allRecipesName">{title}</div>
          <div className="allRecipesDescription">{description}</div>
        </div>
      </div>
    </NavLink>
  );
};

export default AllCultureCards;
