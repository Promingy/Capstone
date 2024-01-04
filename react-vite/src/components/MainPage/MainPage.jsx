import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import './MainPage.css'
import { thunkGetAllRecipes } from '../../redux/recipe'
import RecipeTile from './RecipeTile'

export default function MainPage() {
    const dispatch = useDispatch()
    const recipes = useSelector(state => state.recipes.categories)

    useEffect(() => {
        dispatch(thunkGetAllRecipes())
    }, [dispatch])

    return (
        <>
            {recipes && Object.keys(recipes).map(category => {
                const categoryRecipes = Object.values(recipes[category])

                return (
                    <div className='recipe_tile_category_container'>
                        <h2>{category}</h2>
                        <div className={`recipe_tile_container`}>
                            {categoryRecipes.map(recipe => <RecipeTile key={`recipe${recipe.id}`} recipe={recipe} />)}
                        </div>
                    </div>
                )
            })}
        </>

    )
}
