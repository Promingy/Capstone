import { useNavigate } from 'react-router-dom'
import './RecipeTile.css'
import { useState } from 'react'

export default function RecipeTile({ recipe }) {
    const navigate = useNavigate()
    const cookTimeHours = Math.floor((recipe.cook_time + recipe.prep_time) / 60)
    const cookTimeMinutes = recipe.cook_time % 60
    const ownerFirstName = recipe.owner.first_name[0].toUpperCase() + recipe.owner.first_name.slice(1)
    const ownerLastName = recipe.owner.last_name[0].toUpperCase() + recipe.owner.last_name.slice(1)
    const [bookmark, setBookmark] = useState('fa-regular fa-bookmark')
    const [saved, setSaved] = useState(false)

    function starCreator() {
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

    return (
        <div className='recipeTile'
        onClick={() => navigate(`/recipes/${recipe.id}-${recipe.title.toLowerCase().split(' ').join('-')}`, {state: recipe})}
        >
            <img className='card_image' src={recipe.preview_image} />
            <div className='card_bottom'>

                <div className='card_title_owner'>
                    <h4>{recipe.title}</h4>
                    <p>{ownerFirstName} {ownerLastName}</p>
                </div>

                <div className='card_rating_time_container'>

                    <p>{starCreator()} {recipe.all_ratings}</p>

                    <div className='time_and_bookmark'>

                        <p>
                            {!!cookTimeHours &&
                            <span>
                                {cookTimeHours} {cookTimeHours > 1 ? "hours" : "hour"}
                            </span>}&nbsp;
                            {cookTimeMinutes} Minutes
                        </p>

                        <span
                            className={bookmark}
                            onMouseOver={() => {
                                if (!saved){
                                    setBookmark('fa-solid fa-bookmark')}}
                                }
                            onMouseLeave={() =>{
                                if (!saved){
                                    setBookmark('fa-regular fa-bookmark')
                                }
                            }}
                            onClick={() => {
                                if (!saved){
                                    setBookmark('fa-solid fa-bookmark')
                                } else {
                                    setBookmark("fa-regular fa-bookmark")
                                }
                                setSaved(!saved)
                            }}
                            />

                    </div>
                </div>
            </div>

        </div>
    )
}
