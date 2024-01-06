import { useEffect } from 'react'
import './SelectedRecipe.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetSelectedRecipe } from '../../redux/recipe'
import { useParams } from 'react-router-dom'
import { starCreator } from '../MainPage/RecipeTile'

export default function SelectedRecipe() {
    const dispatch = useDispatch()
    let { recipeId } = useParams()

    recipeId = recipeId.split('-')[0]
    const recipe = useSelector(state => state.recipes[recipeId])
    const postDate = new Date(recipe?.created_at)

    const ownerFirstName = recipe?.owner.first_name[0].toUpperCase() + recipe?.owner.first_name.slice(1)
    const ownerLastName = recipe?.owner.last_name[0].toUpperCase() + recipe?.owner.last_name.slice(1)

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
    }, [dispatch, recipeId])


    if (!recipe) return
    return (
        <div>
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
                    <div className='cook_times'>
                        <span className='time_format'>
                            <h3>Total Time</h3>
                            <p>
                                {!!totalCookTimeHours &&
                                    <span>
                                        {totalCookTimeMinutes ? "" : "About"}
                                        {totalCookTimeHours} {totalCookTimeHours > 1 ? "hours" : "hour"}
                                    </span>
                                }
                                &nbsp;
                                {!!totalCookTimeMinutes &&
                                    <span>
                                        {totalCookTimeMinutes} {totalCookTimeMinutes > 1 ? "minutes": "minute"}
                                    </span>
                                }
                                </p>
                        </span>
                        <span className='time_format'>
                            <h4>Prep Time</h4>
                            <p>
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
                                </p>
                        </span>
                        <span className='time_format'>
                            <h4>Cook Time</h4>
                            <p>
                                {!!cookTimeHours &&
                                    <span>
                                        {cookTimeHours} {cookTimeHours > 1 ? "hours" : "hour"}
                                    </span>
                                }
                                &nbsp;
                                {!!prepTimeMinutes &&
                                    <span>
                                        {cookTimeMinutes} {cookTimeMinutes > 1 ? "minutes": "minute"}
                                    </span>
                                }
                                </p>
                        </span>
                    </div>
                    <span className='time_format'>
                        <h3>Rating</h3>
                        {recipe.avg_rating &&
                            <p>
                                {recipe.avg_rating} &nbsp;
                                {starCreator(recipe)} &nbsp;
                                ({recipe.all_ratings})
                            </p>
                        }

                        {!recipe.avg_rating &&
                            <p>
                                Be the first to leave a rating!
                            </p>
                        }

                    </span>
                    <span className='time_format'>
                        <h3>Notes</h3>
                        <p style={{display: "flex", gap: "10px", alignItems: "center"}}>
                            {recipe.all_ratings ? `Read ${recipe.all_ratings} community notes` : 'Be the first to leave a note!'}
                            <i className='fa-solid fa-turn-down fa-xs' />
                        </p>
                    </span>

                </div>
                <div className='prep_time_bio_right'>
                    <p>{recipe.description}</p>
                </div>
            </div>
        </div>
    )
}
