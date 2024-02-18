import { useEffect } from 'react'
import './UserRecipe.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetUserRecipes } from '../../redux/session'
import { useParams } from 'react-router-dom'
import RecipeTile from '../MainPage/RecipeTile'
import { useModal } from '../../context/Modal'
import { thunkGetSavedRecipes } from '../../redux/recipe'

export default function UserRecipe() {
    const dispatch = useDispatch()
    let { userId } = useParams()
    const { closeModal } = useModal()
    const sessionUser = useSelector(state => state.session.user)
    userId = +userId?.split(' ')?.[0]
    let recipes = useSelector(state => state.session)
    const savedRecipes = useSelector(state => state.recipes.savedRecipes)
    const owner = recipes?.[+userId]?.owner
    recipes = recipes?.[+userId]

    useEffect(() => {
        dispatch(thunkGetUserRecipes(userId))
        dispatch(thunkGetSavedRecipes(sessionUser?.id))
        window.scrollTo(0, 0)
    }, [dispatch, userId])

    useEffect(() => {
        closeModal()
    }, [sessionUser])

    function capFirstLeter(str) {
        if (typeof str != 'string') return ''

        const firstLetter = str[0].toUpperCase()
        const body = str.slice(1).toLowerCase()

        return firstLetter + body
    }

    if (!recipes || !owner) return

    return (
        <div className='user_recipes_container'>
            <header className='user_profile_container'>
            <h2 className='user-profile-name'>
                {capFirstLeter(owner?.first_name)} {capFirstLeter(owner?.last_name)}
            </h2>
            <div className='user-pic-desc'>
                <div className='header_left'>
                    <img className='user_page_profile_pic' src={owner?.profile_pic}/>
                </div>
                <div className='header_right'>
                    <p>{owner?.bio}</p>
                </div>
            </div>
            </header>
            <div className='user_recipes_content_container'>
                <p>{Object.values(recipes).length - 1} results</p>
                <div className='user_recipe_tile_container'>
                    {Object.values(recipes).map(recipe => {
                        if (recipe == owner) return
                        return (
                            <RecipeTile recipe={recipe} isSaved={recipe.id in savedRecipes} key={`recipe${recipe.id}`}/>
                        )
                    })}
                </div>

            </div>
        </div>
    )
}
