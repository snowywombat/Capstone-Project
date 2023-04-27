import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkGetAllCultures } from "../../store/culture";
import AllCultureCards from "./AllCultureCards";

const AllCulturesPage = () => {
    const dispatch = useDispatch();
    const allArticles = useSelector(state => state.cultures)

    useEffect(() => {
        dispatch(thunkGetAllCultures())
    }, [dispatch]);


    if(!allArticles) {
        return <div>Loading...</div>
    }

    return (
        <>
            {allArticles &&
                 <div className="AllRecipes-Container">
                 {Object.values(allArticles).map((culture, index) => (
                 <AllCultureCards culture={culture} key={index} />
                 ))}
             </div>
            }

        </>
    )
};
export default AllCulturesPage;
