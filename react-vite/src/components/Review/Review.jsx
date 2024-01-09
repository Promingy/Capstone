import { useState } from 'react'
import './Review.css'
import TextareaAutoSize from 'react-textarea-autosize'
import ReviewTile from './ReviewTile'
import { useDispatch } from 'react-redux'
import { thunkPostReview } from '../../redux/review'

export default function Review ({ recipe }) {
    const dispatch = useDispatch()
    const [rating, setRating] = useState(0)
    const [hoverRating, setHoverRating] = useState(0)
    const [ratingConfirmed, setRatingConfirmed] = useState(false)
    const [review, setReview] = useState('')
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

    function handleSubmit(e) {
        e.preventDefault()

        const newReview = {
            rating: +rating,
            body: review,
            submit: true
        }

        dispatch(thunkPostReview(newReview, recipe.id))
    }

    return (
        <div className='reviews_container'>
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
                <div>
                    <h4 className='post_review_title'>Add Note</h4>
                    <TextareaAutoSize
                        value={review}
                        onChange={e => setReview(e.target.value)}
                        className='post_review'
                        placeholder='Share your notes with other cooks...'
                    />
                    <div className='submit_review_container'>
                        {!!review.length && <span onClick={() => setReview('')}>Cancel</span>}
                        <button className='submit_review' onClick={handleSubmit}>Submit</button>
                    </div>
                    <div className='review_container'>
                        {!recipe.reviews.length && <h2>Be the first to post a note!</h2>}
                        {recipe.reviews.map(review => (
                            <ReviewTile review={review} key={`review${review.id}`}/>
                        ))}
                    </div>
                </div>
            </div>
        </div>
    )
}
