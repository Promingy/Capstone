import { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import { thunkGetSavedRecipes } from "../../redux/recipe"
import RecipeTile from "../MainPage/RecipeTile"

export default function SavedRecipes() {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)
    const recipes = useSelector(state => state.recipes.savedRecipes)

    useEffect(() => {
        dispatch(thunkGetSavedRecipes(sessionUser.id))
    }, [])

    console.log('recipes', recipes)
    if (!recipes) return null
    return (
        <div className="saved-recipes-container">
            {recipes && Object.values(recipes).map(recipe => {
                return (
                    <RecipeTile key={recipe.id} recipe={recipe} />
                )
            })}
        </div>
    )
}
