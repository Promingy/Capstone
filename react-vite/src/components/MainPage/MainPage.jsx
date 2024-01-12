import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import './MainPage.css'
import { thunkGetAllRecipes } from '../../redux/recipe'
import RecipeTile from './RecipeTile'
import { thunkGetDropdowns } from '../../redux/dropdown'
import { useModal } from '../../context/Modal'
import { useLocation } from 'react-router-dom'

export default function MainPage() {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const sessionUser = useSelector(state => state.session.user)
    const dropdowns = useSelector(state => state.dropdowns.categories)
    let recipes = useSelector(state => state.recipes)
    const location = useLocation()
    const [firstRecipe, setFirstRecipe] = useState(null)
    recipes = recipes.categories

    useEffect(() => {

        dispatch(thunkGetAllRecipes())
        dispatch(thunkGetDropdowns())

        // set css styling back to normal if logged out and navigating from selected recipe page
        if (!sessionUser) {
            const body = document.getElementsByTagName('body')
            body[0].classList.remove('no_scroll')
        }

        closeModal()
    }, [dispatch, sessionUser])

    if (location?.state == firstRecipe?.preview_image) setFirstRecipe(null)

    return (
        <div className='recipe_tile_category_container'>
            <div className='header_image_container'>
                <img className='main_image' src={firstRecipe?.preview_image} />
                <header className='main_image_text'>
                    <h2>Easy Weeknight Dinners</h2>
                    <p>Make these recipes when you need a fast, flavorful meal.</p>
                </header>
            </div>
            {recipes && Object.keys(recipes).map(category => {
                const categoryRecipes = Object.values(recipes[category])
                category = dropdowns?.[category].category

                return (
                    <div key={`${category}`} className='recipe_tile_category_container'>
                        <h2>{category}</h2>
                        <div className={`recipe_tile_container`}>
                            {categoryRecipes.map(recipe => {
                                if (!firstRecipe) {setFirstRecipe(recipe)}

                                return <RecipeTile key={`recipe${recipe.id}`} recipe={recipe} />
                            })}
                        </div>
                    </div>
                )
            })}
        </div>

    )
}
