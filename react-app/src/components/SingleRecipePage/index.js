import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { thunkGetSingleRecipe } from "../../store/recipes";
import './SingleRecipePage.css'

const SingleRecipePage = () => {
    const { recipeId } = useParams();
    const dispatch = useDispatch();

    const [loadedPage, setLoadedPage] = useState(false);

    const singleRecipe = useSelector((state) => state.recipes.recipeDetails);
    console.log(singleRecipe, 'kajdflkajkf')

    useEffect(() => {
        dispatch(thunkGetSingleRecipe(recipeId)).then(() => setLoadedPage(true))
    }, [dispatch, recipeId]);

    if (!loadedPage) return null;
    if(!singleRecipe) return null;

    const {
        createdAt,
        description,
        id,
        imgUrl,
        ingredients,
        kitchenware,
        name,
        preparation,
        servingSize,
        user,
        userId
      } = singleRecipe;

    return (
        <>
            <div className='page-container'>
                <div className='photo-container'>
                    <img src={imgUrl} alt={"image of " + description} id='recipeImg'></img>
                </div>
                <div>
                    {name}
                    By
                    {user.firstName}
                    {user.lastName}
                    {createdAt}
                </div>
                <div>
                    {description}
                </div>
                <div>
                    {kitchenware.map(item => (
                        item.name
                    ))}
                </div>
                <div>
                    {servingSize} servings
                    {ingredients.map(item => (
                        item.measurement_num
                    ))}
                    {ingredients.map(item => (
                        item.measurement_type
                    ))}
                    {ingredients.map(item => (
                        item.ingredient
                    ))}
                </div>
                <div>
                    {preparation.map(step => (
                        step.description
                    ))}
                </div>
            </div>

        </>
    )

}

export default SingleRecipePage;
