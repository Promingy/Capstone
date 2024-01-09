import { useState } from 'react'
import './Review.css'

export default function Review ({ recipe }) {
    const [rating, setRating] = useState(0)
    const [hoverRating, setHoverRating] = useState(0)
    const [ratingConfirmed, setRatingConfirmed] = useState(false)
    function starCreatorHover() {
        const stars = []

        for (let i = 0; i < 5; i++){
            stars.push(
                <i
                onMouseOver={() => setHoverRating(i + 1)}
                onMouseLeave={() => {
                    if (!ratingConfirmed) {
                        setHoverRating(0)
                    } else {
                        setHoverRating(rating)
                    }
                }}
                onClick={() => {
                    setRatingConfirmed(true)
                    setRating(i + 1)
                }}
                key={`${recipe.id}star${i}`}
                className={`fa-solid fa-star fa-sm ${ i < hoverRating ? 'your_rating' : 'your_rating2'}`}/>
            )
        }

        return stars
    }

    return (
        <div className='review_container'>
            <div className='review_left'>
                <h2 className='review_headers'>RATINGS</h2>
                <div className='ratings_container'>
                    <p className='fa-solid fa-star fa-xl ratings_star'/>
                    <div className='reviews_out_of_container'>
                        <h3 className='reviews_out_of'>{recipe.avg_rating} out of 5</h3>
                        <p className='reviews_out_of reviews_out_of_p'>{recipe.reviews.length} user ratings</p>
                    </div>
                </div>
                    <p className='your_rating_clear'>
                        Your rating
                        {!!rating && <span onClick={() => {
                            setRatingConfirmed(false)
                            setHoverRating(0)
                            setRating(0)
                            }}>clear</span>}
                    </p>
                    <div className='your_rating_stars'>
                        {starCreatorHover()}
                    </div>
            </div>
            <div className='review_right'>
                <h2 className='review_headers'>COOKING NOTES</h2>
            </div>
        </div>
    )
}
