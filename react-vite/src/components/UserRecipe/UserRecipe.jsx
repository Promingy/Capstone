import { useEffect, useState } from 'react'
import './UserRecipe.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetUserRecipes } from '../../redux/session'
import { useParams } from 'react-router-dom'

export default function UserRecipe() {
    const dispatch = useDispatch()
    const { userId } = useParams()
    let recipes = useSelector(state => state.session)
    const [recipeOwner, setRecipeOwner] = useState(null)
    recipes = recipes?.[userId]

    console.log('recipes', recipeOwner)

    useEffect(() => {
        dispatch(thunkGetUserRecipes(+userId))
    }, [dispatch])

    function capFirstLeter(str) {
        if (typeof str != 'string') return ''

        const firstLetter = str[0].toUpperCase()
        const body = str.slice(1).toLowerCase()

        return firstLetter + body
    }

    if (!recipes) return

    return (
        <div className='user_recipes_container'>
            <header className='user_profile_container'>
                <div className='header_left'>
                    <h2>
                        {capFirstLeter(recipeOwner?.first_name)} {capFirstLeter(recipeOwner?.last_name)}
                    </h2>
                    <img className='user_page_profile_pic' src={recipeOwner?.profile_pic}/>
                </div>
                <div className='header_right'>
                    <p>{recipeOwner?.bio}</p>
                </div>
            </header>
            <div>
                {Object.values(recipes).map(recipe => {
                    if (!recipeOwner) return setRecipeOwner(recipe.owner)

                    return (
                        <div>
                        </div>
                    )
                })}

            </div>
        </div>
    )
}
