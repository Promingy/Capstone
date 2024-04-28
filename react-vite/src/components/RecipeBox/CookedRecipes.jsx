import { useEffect } from "react";
import { useDispatch } from "react-redux"

export default function CookedRecipes() {
    const dispatch = useDispatch();
    // const allRecipes = useSelector(state => state.recipes);
    // const recipes = allRecipes.cookedRecipes;

    useEffect(() => {}, [dispatch])

    return (
        <div>
            <div className="saved-recipes-header-container">
                <h2 className="saved-recipes-header">Cooked Recipes</h2>
                <p className="saved-recipes-subheader">{} recipes</p>
            </div>
        </div>
    )
}
