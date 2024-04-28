import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"
import { thunkGetCookedRecipes } from "../../redux/recipe";
import RecipeTile from "../MainPage/RecipeTile";

export default function CookedRecipes() {
    const dispatch = useDispatch();
    const sessionUser = useSelector(state => state.session.user)
    const allRecipes = useSelector(state => state.recipes);
    const recipes = allRecipes.cookedRecipes;

    useEffect(() => {
        dispatch(thunkGetCookedRecipes(sessionUser.id))
    }, [dispatch])

    if (!recipes) return null

    return (
        <div>
            <div className="saved-recipes-header-container">
                <h2 className="saved-recipes-header">Cooked Recipes</h2>
                <p className="saved-recipes-subheader">{Object.values(recipes).length} recipes</p>
            </div>
            <div className="saved-recipes-container">
                {recipes && Object.values(recipes).map(recipe => {
                    return (
                        <RecipeTile key={recipe.id} recipe={recipe}/>
                    )
                })}
            </div>
        </div>
    )
}
