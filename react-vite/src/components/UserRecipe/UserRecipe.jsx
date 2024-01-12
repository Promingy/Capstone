import { useEffect } from 'react'
import './UserRecipe.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetUserRecipes } from '../../redux/session'
import { useParams } from 'react-router-dom'

export default function UserRecipe() {
    const dispatch = useDispatch()
    const { userId } = useParams()
    let recipes = useSelector(state => state.session)
    let recipeOwner;
    recipes = recipes?.[userId]


    console.log('recipes', recipes)

    useEffect(() => {
        dispatch(thunkGetUserRecipes(+userId))
    }, [dispatch])

    if (!recipes) return

    return (
        <div className='user_recipes_container'>
            <header>
                test
            </header>
            <div>
                {Object.values(recipes).map(recipe => {
                    if (!recipeOwner) recipeOwner = recipe.owner

                    return (
                        <div>
                        </div>
                    )
                })}

            </div>
        </div>
    )
}
