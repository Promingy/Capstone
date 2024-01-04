import './SelectedRecipe.css'
import { useLocation, useParams } from 'react-router-dom'

export default function SelectedRecipe() {
    const recipe = useLocation().state

    if (!recipe) return
    return (
        <div>
            <h1>{recipe.title}</h1>
            <img src={recipe.preview_image} />
        </div>
    )
}
