import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import './MainPage.css'
import { thunkGetAllRecipes } from '../../redux/recipe'
import RecipeTile from './RecipeTile'
import { thunkGetDropdowns } from '../../redux/dropdown'
import { useModal } from '../../context/Modal'

export default function MainPage() {
    const dispatch = useDispatch()
    const { closeModal } = useModal()
    const sessionUser = useSelector(state => state.session.user)
    let recipes = useSelector(state => state.recipes)
    recipes = recipes.categories
    const dropdowns = useSelector(state => state.dropdowns.categories)

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

    return (
        <div className=''>
            {recipes && Object.keys(recipes).map(category => {
                const categoryRecipes = Object.values(recipes[category])
                category = dropdowns?.[category].category

                return (
                    <div key={`${category}`} className='recipe_tile_category_container'>
                        <h2>{category}</h2>
                        <div className={`recipe_tile_container`}>
                            {categoryRecipes.map(recipe => <RecipeTile key={`recipe${recipe.id}`} recipe={recipe} />)}
                        </div>
                    </div>
                )
            })}
        </div>

    )
}
