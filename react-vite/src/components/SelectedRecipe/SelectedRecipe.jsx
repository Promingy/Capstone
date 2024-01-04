import { useEffect } from 'react'
import './SelectedRecipe.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetSelectedRecipe } from '../../redux/recipe'
import { useParams } from 'react-router-dom'

export default function SelectedRecipe() {
    const dispatch = useDispatch()
    const {recipeId} = useParams()
    const recipe = useSelector(state => state.recipes[recipeId])

    useEffect(() => {
        dispatch(thunkGetSelectedRecipe(recipeId))
    }, [dispatch])

    if (!recipe) return
    return (
        <div>
            <h1>{recipe.title}</h1>
            <img src={recipe.preview_image} />
        </div>
    )
}
