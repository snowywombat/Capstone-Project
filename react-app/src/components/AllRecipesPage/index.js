import { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import { thunkGetAllRecipes } from "../../store/recipes";
import AllRecipeCards from "./AllRecipeCards";
import './AllRecipeCards.css'

const AllRecipesPage = () => {
    const { recipeId } = useParams();
    const dispatch = useDispatch();
    const [loadedPage, setLoadedPage] = useState(false);

    //get all recipe data via thunk
    const allRecipes = useSelector(state => state.recipes.Recipes)


    useEffect(() => {
        dispatch(thunkGetAllRecipes()).then(() => setLoadedPage(true))
    }, [dispatch])


    if (!loadedPage) return null;

    return (
        <>
            <div className="AllRecipes-Container">
                {Object.values(allRecipes).map(recipe => (
                <AllRecipeCards recipe={recipe} key={recipe.id} />
            ))}
            </div>
        </>
    )
};
export default AllRecipesPage;
