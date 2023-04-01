import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetAllRecipes } from "../../store/recipes";
import AllRecipeCards from "./AllRecipeCards";
import './AllRecipeCards.css'

const AllRecipesPage = () => {
    const dispatch = useDispatch();
    // const [loadedPage, setLoadedPage] = useState(false);
    const allRecipes = useSelector(state => state.recipes)

    // useEffect(() => {
    //     dispatch(thunkGetAllRecipes()).then(() => setLoadedPage(true))
    // }, [dispatch])

    useEffect(() => {
        dispatch(thunkGetAllRecipes())
    }, [dispatch]);


    if(!allRecipes) {
        return <div>Loading...</div>
    }

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
