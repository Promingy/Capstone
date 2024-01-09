import { useState } from 'react'
import './Review.css'
import TextareaAutoSize from 'react-textarea-autosize'
import ReviewTile from './ReviewTile'
import { useDispatch, useSelector } from 'react-redux'
import { thunkDeleteRating, thunkPostRating, thunkPostReview, thunkUpdateRating } from '../../redux/review'

export default function Review ({ recipe }) {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)
    const [rating, setRating] = useState(recipe?.user_rating?.rating || 0)
    const [hoverRating, setHoverRating] = useState(recipe?.user_rating?.rating || 0)
    const [ratingConfirmed, setRatingConfirmed] = useState(!!recipe?.user_rating || false)
    const [review, setReview] = useState('')
    const [ratingSubmitted, setRatingSubmitted] = useState(false)

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
                    if (!ratingSubmitted){
                        setRatingConfirmed(true)
                        setRating(i + 1)
                        handlePostRating(i + 1)
                    }
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
            body: review
        }

        dispatch(thunkPostReview(newReview, recipe.id))
    }

    function handlePostRating(newRating) {
        setRatingSubmitted(true)

        const ratingToPost = {
            recipe_id: recipe.id,
            user_id: sessionUser.id,
            rating: newRating,
            submit: true
        }

        dispatch(recipe?.user_rating ?
            thunkUpdateRating(ratingToPost, recipe?.user_rating?.id)
            :
            thunkPostRating(ratingToPost, recipe.id)).then(() => setRatingSubmitted(false))
    }

    function HandleDeleteRating() {
        setRatingSubmitted(true)
        dispatch(thunkDeleteRating(recipe?.user_rating, recipe?.user_rating?.id)).then(() => setRatingSubmitted(false))
        recipe.user_rating = undefined
    }

    return (
        <div className='reviews_container'>
            <div className='review_left'>
                <h2 className='review_headers'>RATINGS</h2>
                <div className='ratings_container'>
                    <p className='fa-solid fa-star fa-xl ratings_star'/>
                    <div className='reviews_out_of_container'>
                        <h3 className='reviews_out_of'>{recipe.avg_rating.toFixed(1)} out of 5</h3>
                        <p className='reviews_out_of reviews_out_of_p'>{recipe.all_ratings} user ratings</p>
                    </div>
                </div>
                    <p className='your_rating_clear'>
                        Your rating
                        {!!hoverRating && <span onClick={() => {
                            if (!ratingSubmitted){
                                setRatingConfirmed(false)
                                setHoverRating(0)
                                setRating(0)
                                HandleDeleteRating(0)
                            }
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
                        {recipe.reviews.map(review => {
                            if (!review.private){
                               return <ReviewTile review={review} key={`review${review.id}`}/>
                            }
                        })}
                    </div>
                </div>
            </div>
        </div>
    )
}
