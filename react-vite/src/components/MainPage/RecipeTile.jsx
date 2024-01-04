import { useNavigate } from 'react-router-dom'
import './RecipeTile.css'

export default function RecipeTile({ recipe }) {
    const navigate = useNavigate()
    return (
        <div className='recipeTile' onClick={() => navigate(`/recipes/${recipe.title.toLowerCase().split(' ').join('-')}`, {state: recipe})}>
            <h3>{recipe.title}</h3>
            <img className='test' src={recipe.preview_image} />
        </div>
    )
}
