import { useEffect } from 'react'
import './SelectedRecipe.css'
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetSelectedRecipe } from '../../redux/recipe'
import { thunkGetDropdowns } from "../../redux/dropdown"
import { useNavigate, useParams } from 'react-router-dom'
import { starCreator } from '../MainPage/RecipeTile'
import Review from '../Review'
import OpenModalButton from '../OpenModalButton/OpenModalButton'
import ConfirmDelete from '../ConfirmDelete'
import LoginFormModal from '../LoginFormModal'
import { useModal } from '../../context/Modal'

export default function SelectedRecipe() {
    const dispatch = useDispatch()
    let { recipeId } = useParams()
    const navigate = useNavigate()
    const sessionUser = useSelector(state => state.session.user)
    const {setModalContent, closeable} = useModal()

    useEffect(() => {
        // get body to disable scroll
        const body = document.getElementsByTagName('body')

        // if user is logged in, re-enable scroll
        if (sessionUser) {
            body[0]?.classList.remove('no_scroll')
            return closeable(true)
        }

        // disable scroll
        body[0]?.classList?.add('no_scroll')

        // scroll back to top of screen
        window.scrollTo({behavior: "smooth", top: 0})

        // disable ability to close modal and open modal
        closeable(false)
        setModalContent(<LoginFormModal />)
    }, [sessionUser])

    recipeId = recipeId.split('-')[0]
    const recipes = useSelector(state => state.recipes)
    const recipe = recipes[recipeId]
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

    const totalPublicComments = recipe?.reviews && Object.values(recipe?.reviews).filter(review => !review.private).length

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
        <div className='selected_recipe'>
            <div className='header_image_title'>
                <div className='single_title_owner'>
                    <h1 >{recipe.title}</h1>
                    <div className='title_icon_container'>
                        {sessionUser?.id == recipe.owner_id &&
                        <>
                            <span onClick={() => {navigate(`/recipes/${recipeId}/edit`)}}>
                            <i className={`fa-regular fa-pen-to-square fa-lg`} />
                        </span>
                        <span className='delete_recipe_icon_title' >
                            <OpenModalButton
                            buttonText={<span className="fa-regular fa-trash-can fa-xl"/>}
                            modalComponent={<ConfirmDelete recipe={recipe}/>}
                            />
                        </span>
                        </>
                        }
                    </div>
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
                                    <span>
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
                        <div>
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
                        </div>

                        <h3>Notes</h3>
                        <p onClick={() => document.getElementById('public_comments').scrollIntoView({behavior: "smooth"})}>
                            <span className='notes'>
                                {recipe?.all_ratings ? `Read ${totalPublicComments} community notes` : 'Be the first to leave a note!'}
                            </span>
                            <span>
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
                    <h2>INGREDIENTS</h2>

                    <div className='yield_container'>
                        <h4 className='yield_title'>Yeild:</h4> &nbsp;
                        {recipe?.servings} servings
                    </div>

                    {recipe?.ingredients && Object.values(recipe?.ingredients)?.map(ingredient => {
                        const measurementId = ingredient?.ingredient_measurement_id
                        let measurement = dropdowns?.measurements?.[+measurementId]?.measurement_name
                        measurement = +ingredient?.ingredient_quantity > 1 ? measurement + 's' : measurement

                        return (<p key={`ingredient${recipe.id}${ingredient?.id}`}>{ingredient?.ingredient_quantity} {measurement} {ingredient?.ingredient}</p>)
                        })}
                </div>
                <div className='ingredients_and_steps_right'>
                    <h2>PREPERATION</h2>

                    <div className='selected_recipe_steps_container'>
                        {Object.values(recipe.steps).map(step => {

                            return (
                                <div className='selected_recipe_step' key={`step${recipe.id}${step.step_number}`}>
                                    <h3>Step {step.step_number}.</h3>
                                    <p>{step.description}</p>
                                </div>
                            )
                        })}
                    </div>
                </div>
            </div>

            <div>
                <Review recipe={recipe} />
            </div>
        </div>
    )
}
