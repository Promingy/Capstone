import { useEffect } from 'react'
import './SelectedRecipe.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetSelectedRecipe } from '../../redux/recipe'
import { useLocation, useParams } from 'react-router-dom'

export default function SelectedRecipe() {
    const dispatch = useDispatch()
    let { recipeId } = useParams()
    recipeId = recipeId.split('-')[0]
    const recipe = useLocation().state || useSelector(state => state.recipes[recipeId])

    useEffect(() => {
        dispatch(thunkGetSelectedRecipe(recipeId))
    }, [dispatch, recipeId])

    if (!recipe) return
    return (
        <div>
            <h1>{recipe.title}</h1>
            <img style={{height: "500px", width: "500px", objectFit: "cover"}} src={recipe.preview_image} />
        </div>
    )
}
