import { useNavigate } from 'react-router-dom'
import './RecipeTile.css'
import { useState } from 'react'
import { useSelector } from 'react-redux'
import OpenModalButton from '../OpenModalButton/OpenModalButton'
import ConfirmDelete from '../ConfirmDelete'
export function starCreator(recipe) {
    const stars = []

    for (let i = 0; i < 5; i++){
        stars.push(
            <i
            key={`${recipe.id}star${i}`}
            className={`fa-${i >= recipe.avg_rating? 'regular' : 'solid'} fa-star fa-sm`}/>
        )
    }

    return stars
}

export default function RecipeTile({ recipe }) {
    const navigate = useNavigate()
    const sessionUser = useSelector(state => state.session.user)
    const cookTimeHours = Math.floor((recipe.cook_time + recipe.prep_time) / 60)
    const cookTimeMinutes = (recipe.cook_time + recipe.prep_time) % 60
    const ownerFirstName = recipe.owner.first_name[0].toUpperCase() + recipe.owner.first_name.slice(1)
    const ownerLastName = recipe.owner.last_name[0].toUpperCase() + recipe.owner.last_name.slice(1)
    // const [bookmark, setBookmark] = useState('fa-regular fa-bookmark fa-lg') /// future feature
    // const [saved, setSaved] = useState(false) /// future feature
    const [confirmDelete, setConfirmDelete] = useState(false)

    function onClickHandle (e) {
        const node = e.target.attributes.id?.value

        if (node != 'delete_recipe' &&
            node != 'bookmark_icon_tile' &&
            node != "edit_recipe_icon" &&
            node != "modalButton") {
            navigate(`/recipes/${recipe.id}-${recipe.title.toLowerCase().split(' ').join('-')}`, {state: recipe})
        }
    }

    return (
        <div className='recipeTile'
        onClick={onClickHandle}
        >
            <img className='card_image' src={recipe.preview_image} />
            <div className='card_bottom'>

                <div className='card_title_owner'>
                    <h4>{recipe.title}</h4>
                    <p>{ownerFirstName} {ownerLastName}</p>
                </div>

                <div className='card_rating_time_container'>

                    <p>{starCreator(recipe)} {recipe.all_ratings}</p>

                    <div className='time_and_bookmark'>

                        <p>
                            {!!cookTimeHours &&
                            <span>
                                {cookTimeMinutes ? "" : "About"}
                                &nbsp;
                                {cookTimeHours} {cookTimeHours > 1 ? "hours" : "hour"}
                            </span>
                            }

                            &nbsp;

                            {!!cookTimeMinutes &&
                            <span>
                                {cookTimeMinutes} Minutes
                            </span>
                            }
                        </p>
                        <div className='tile_icons_container'>
                            {/* <span ///future feature
                                id='bookmark_icon_tile'
                                className={bookmark}
                                onMouseOver={() => {
                                    if (!saved){
                                        setBookmark('fa-solid fa-bookmark fa-lg')}}
                                    }
                                onMouseLeave={() =>{
                                    if (!saved){
                                        setBookmark('fa-regular fa-bookmark fa-lg')
                                    }
                                }}
                                onClick={() => {
                                    if (!saved){
                                        setBookmark('fa-solid fa-bookmark fa-lg')
                                    } else {
                                        setBookmark("fa-regular fa-bookmark fa-lg")
                                    }
                                    setSaved(!saved)
                                }}
                                /> */}

                                {sessionUser?.id == recipe.owner_id &&
                                <>
                                    <span className='delete_recipe_icon'>
                                        <OpenModalButton
                                            buttonText={<span
                                                id='delete_recipe'
                                                className='fa-regular fa-trash-can fa-xl delete_recipe'
                                                onClick={() => setConfirmDelete(!confirmDelete)}
                                            />}
                                            modalComponent={<ConfirmDelete recipe={recipe} />}
                                        />
                                    </span>
                                    <span className='edit_recipe_icon_container'>
                                        <i className='fa-regular fa-pen-to-square fa-lg' id="edit_recipe_icon"
                                            onClick={() => navigate(`/recipes/${recipe.id}/edit`)}/>
                                    </span>
                                </>
                                }

                        </div>

                    </div>
                </div>
            </div>

        </div>
    )
}
