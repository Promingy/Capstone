import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import './MainPage.css'
import { thunkCreateRecipe, thunkDeleteRecipe, thunkGetAllRecipes, thunkUpdateRecipe } from '../../redux/recipe'
import RecipeTile from './RecipeTile'

export default function MainPage() {
    const dispatch = useDispatch()
    const recipes = useSelector(state => state.recipes.categories)

    useEffect(() => {
        dispatch(thunkGetAllRecipes())
    }, [dispatch])

    // function createTestRecipe (e) {
    //     e.preventDefault()
    //     dispatch(thunkCreateRecipe({}))
    // }
    // function deleteRecipe (e) {
    //     e.preventDefault()
    //     dispatch(thunkDeleteRecipe(7))
    // }
    // function updateRecipe (e) {
    //     e.preventDefault()
    //     dispatch(thunkUpdateRecipe(8))
    // }

    return (
        <>
        {/* <button onClick={createTestRecipe} >Create Recipe</button>
        <button onClick={updateRecipe} >Update Recipe</button>
        <button onClick={deleteRecipe} >Delete Recipe</button> */}
            {recipes && Object.keys(recipes).map(category => {
                const categoryRecipes = Object.values(recipes[category])

                return (
                    <div key={`${category}`} className='recipe_tile_category_container'>
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
