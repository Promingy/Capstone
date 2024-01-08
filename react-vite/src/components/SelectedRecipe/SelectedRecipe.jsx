import { useEffect } from 'react'
import './SelectedRecipe.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetSelectedRecipe } from '../../redux/recipe'
import { thunkGetDropdowns } from "../../redux/dropdown"
import { useParams } from 'react-router-dom'
import { starCreator } from '../MainPage/RecipeTile'

export default function SelectedRecipe() {
    const dispatch = useDispatch()
    let { recipeId } = useParams()

    recipeId = recipeId.split('-')[0]
    const recipe = useSelector(state => state.recipes[recipeId])
    const dropdowns = useSelector(state => state.dropdowns)
    const postDate = new Date(recipe?.created_at)

    const ownerFirstName = recipe?.owner?.first_name[0].toUpperCase() + recipe?.owner?.first_name.slice(1)
    const ownerLastName = recipe?.owner?.last_name[0].toUpperCase() + recipe?.owner?.last_name.slice(1)

    const prepTimeHours = Math.floor(recipe?.prep_time / 60)
    const prepTimeMinutes = recipe?.prep_time % 60

    const cookTimeHours = Math.floor(recipe?.cook_time / 60)
    const cookTimeMinutes = recipe?.cook_time % 60

    const totalCookTimeHours = Math.floor((recipe?.cook_time + recipe?.prep_time) / 60)
    const totalCookTimeMinutes = (recipe?.cook_time + recipe?.prep_time) % 60

    const months = {
        1: "Jan.",
        2: "Feb.",
        3: "Mar.",
        4: "Apr",
        5: "May.",
        6: "Jun.",
        7: "Jul.",
        8: "Aug.",
        9: "Sep.",
        10: "Oct.",
        11: "Nov.",
        12: "Dec."
    }

    useEffect(() => {
        dispatch(thunkGetSelectedRecipe(recipeId))
        dispatch(thunkGetDropdowns())
    }, [dispatch, recipeId])


    if (!recipe || !recipe.steps || !recipe.ingredients) return
    return (
        <div className='spacer selected_recipe'>
            <div className='header_image_title'>
                <div className='single_title_owner'>
                    <h1>{recipe.title}</h1>
                    <div>
                        <h4 >By <span className='single_owner'>{ownerFirstName} {ownerLastName}</span></h4>
                        <p>Posted {months[postDate.getMonth() + 1]} {postDate.getDay()}, {postDate.getFullYear()}</p>

                    </div>
                </div>
                <div className='single_preview_image'>
                    <img src={recipe.preview_image} />
                </div>
            </div>

            <div className='body_prep_time_bio'>
                <div className='prep_time_bio_left'>
                    <div className='recipe_info_titles'>

                    <div className='title_and_info'>
                        <h3 className='time_margin'>Total Time</h3>
                        <p>
                            {!!totalCookTimeHours &&
                            <span>
                                    {totalCookTimeHours && !totalCookTimeMinutes ? "About" : ""}
                                    {totalCookTimeHours} {totalCookTimeHours > 1 ? "hours" : "hour"}
                            </span>}
                            &nbsp;
                            {!!totalCookTimeMinutes &&
                            <span>
                                {totalCookTimeMinutes} {totalCookTimeMinutes > 1 ? "minutes" : "minute"}
                            </span>}
                        </p>

                        <h4 className='time_margin'>Prep Time</h4>
                        <p>
                            <span>
                                {!!prepTimeHours &&
                                    <span>
                                        {prepTimeHours} {prepTimeHours > 1 ? "hours" : "hour"}
                                    </span>
                                }
                                &nbsp;
                                {!!prepTimeMinutes &&
                                    <span>
                                        {prepTimeMinutes} {prepTimeMinutes > 1 ? "minutes": "minute"}
                                    </span>
                                }
                            </span>
                        </p>

                        <h4 className='time_margin'>Cook Time</h4>
                        <p>
                            <span>
                                {!!cookTimeHours &&
                                    <span className='test'>
                                        {cookTimeHours} {cookTimeHours > 1 ? "hours" : "hour"}
                                    </span>
                                }
                                &nbsp;
                                {!!cookTimeMinutes &&
                                    <span>
                                        {cookTimeMinutes} {cookTimeMinutes > 1 ? "minutes": "minute"}
                                    </span>
                                }
                            </span>
                        </p>
                        <h3>Ratings</h3>
                        <p>
                            {recipe?.avg_rating > 0 &&
                                <p className='ratings_box'>
                                    &nbsp;&nbsp;{recipe?.avg_rating} {starCreator(recipe)} ({recipe?.all_ratings})
                                </p>
                            }
                            {!recipe.avg_rating &&
                                <span>
                                    Be the first to leave a rating!
                                </span>
                            }
                        </p>

                        <h3>Notes</h3>
                        <p>
                            <span className='notes'>
                                &nbsp;&nbsp;{recipe?.all_ratings ? `Read ${recipe?.all_ratings} community notes` : 'Be the first to leave a note!'}
                                &nbsp;&nbsp;<i className='fa-solid fa-turn-down fa-xs' />
                            </span>
                        </p>
                    </div>

                    </div>

                </div>
                <div className='prep_time_bio_right'>
                    <p>{recipe?.description}</p>
                </div>
            </div>

            <div className='ingredients_and_steps_container'>
                <div className='ingredients_and_steps_left'>
                    <h2>Ingredients</h2>

                    <div className='yield_container'>
                        <h4 className='yield_title'>Yeild:</h4> &nbsp;
                        {recipe?.servings} servings
                    </div>

                    {Object.values(recipe.ingredients)?.map(ingredient => {
                        const measurementId = ingredient.ingredient_measurement_id
                        let measurement = dropdowns.measurements[+measurementId].measurement_name
                        measurement = +ingredient.ingredient_quantity > 1 ? measurement + 's' : measurement

                        return (<p>{ingredient.ingredient_quantity} {measurement} {ingredient.ingredient}</p>)
                        })}
                </div>
                <div className='ingredients_and_steps_right'>
                    <h2>Preperation</h2>

                    <div className='selected_recipe_steps_container'>
                        {Object.values(recipe.steps).map(step => {

                            return (
                                <div className='selected_recipe_step'>
                                    <h3>Step {step.step_number}.</h3>
                                    <p>{step.description}</p>
                                </div>

                            )
                        })}
                    </div>
                </div>
            </div>
        </div>
    )
}
