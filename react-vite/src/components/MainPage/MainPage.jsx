import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import './MainPage.css'
import { thunkGetAllRecipes } from '../../redux/recipe'
import RecipeTile from './RecipeTile'

export default function MainPage() {
    const dispatch = useDispatch()
    const recipes = useSelector(state => state.recipes)

    useEffect(() => {
        dispatch(thunkGetAllRecipes())
    }, [dispatch])

    return (
        <>
        <div className="recipe_tile_container">
            {recipes && Object.values(recipes).map(recipe => {
                return <RecipeTile key={`recipe${recipe.id}`} recipe={recipe} />
            })}
        </div>
        </>
    )
}
