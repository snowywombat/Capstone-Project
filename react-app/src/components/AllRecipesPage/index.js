import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetAllRecipes } from "../../store/recipes";
import AllRecipeCards from "./AllRecipeCards";
import './AllRecipeCards.css'

const AllRecipesPage = () => {
    const dispatch = useDispatch();
    const [loadedPage, setLoadedPage] = useState(false);

    //get all recipe data via thunk
    const allRecipes = useSelector(state => state?.recipes?.Recipes)
    console.log(allRecipes, 'all recipes')

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
