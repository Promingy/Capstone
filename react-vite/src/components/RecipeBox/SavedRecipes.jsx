import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { thunkGetSavedRecipes } from "../../redux/recipe"
import RecipeTile from "../MainPage/RecipeTile"

export default function SavedRecipes() {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)
    const allRecipes = useSelector(state => state.recipes)
    const recipes = allRecipes.savedRecipes

    useEffect(() => {
        dispatch(thunkGetSavedRecipes(sessionUser.id))
    }, [])

    if (!recipes) return null
    
    return (
        <div className="saved-recipes-wrapper">
            <div className="saved-recipes-header-container">
               <h2 className="saved-recipes-header">Saved Recipes</h2>
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
