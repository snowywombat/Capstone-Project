import { useState, useEffect } from "react";
import { useParams } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import { thunkGetAllRecipes } from "../../store/recipes";
import AllRecipeCards from "./AllRecipeCards";
import './AllRecipeCards.css'

const AllRecipesPage = () => {
    const dispatch = useDispatch();
    const [loadedPage, setLoadedPage] = useState(false);
    const allRecipes = useSelector(state => state.recipes)

    console.log(allRecipes, 'allRecipes')


    useEffect(() => {
        dispatch(thunkGetAllRecipes()).then(() => setLoadedPage(true))
    }, [dispatch])


    if (!loadedPage) return null;

    return (
        <>
            <div className="AllRecipes-Container">
                {Object.values(allRecipes).map((recipe, index) => (
                <AllRecipeCards recipe={recipe} key={index} />
            ))}
            </div>

        </>
    )
};
export default AllRecipesPage;
