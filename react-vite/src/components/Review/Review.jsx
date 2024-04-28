import { useEffect, useState } from 'react'
import './Review.css'
import TextareaAutoSize from 'react-textarea-autosize'
import ReviewTile from './ReviewTile'
import { useDispatch, useSelector } from 'react-redux'
import { thunkDeleteRating, thunkPostRating, thunkPostReview, thunkUpdateRating } from '../../redux/review'

export default function Review ({ recipe }) {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)
    const [rating, setRating] = useState(0)
    const [hoverRating, setHoverRating] = useState(0)
    const [ratingConfirmed, setRatingConfirmed] = useState(!!recipe?.user_rating || false)
    const [isCooked, setIsCooked] = useState(recipe.cooked)
    const [review, setReview] = useState('')
    const [ratingSubmitted, setRatingSubmitted] = useState(false)
    const [isPrivate, setIsPrivate] = useState(false)
    const [viewPrivate, setViewPrivate] = useState(false)
    const sortedReviews = Object.values(recipe.reviews).sort((a, b) => new Date(b.created_at) - new Date(a.created_at))

    useEffect(() => {
        setRating(sessionUser && recipe?.user_rating?.rating || 0)
        setHoverRating(sessionUser && recipe?.user_rating?.rating || 0)
    }, [sessionUser, recipe?.user_rating?.rating])

    useEffect(() => {
        setViewPrivate(false)
    }, [sessionUser])

    const totalPrivateComments = sessionUser && Object.values(recipe.reviews).filter(review => review.user_id == sessionUser.id && review.private).length || 0
    const totalPublicComments = Object.values(recipe.reviews).filter(review => !review.private).length
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

    function handlePostReview(e) {
        e.preventDefault()

        if (review.length > 2000 || e.key && e.key != 'Enter' || ratingSubmitted) return

        setRatingSubmitted(true)

        const newReview = {
            body: review,
            edited: false,
            private: isPrivate,
            submit: true
        }

        dispatch(thunkPostReview(newReview, recipe.id)).then(() => setRatingSubmitted(false))

        setReview('')
        setIsPrivate(false)
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

    console.log('recipe', recipe)

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
                    <div>
                        <h3>Have you cooked this?</h3>
                        <p className={isCooked ? 'mark-as-cooked' : 'mark-as-not-cooked'}
                            onClick={() => setIsCooked(!isCooked)}
                        >
                            {isCooked ?
                                <>
                                        <i className='fa-solid fa-circle-check check-icon'/>
                                        <span>Yes I have</span>
                                </>
                                :
                                <>
                                    <i className='fa-regular fa-circle-check check-icon'/>
                                    <span>Mark As Cooked</span>
                                </>
                            }
                        </p>
                    </div>
            </div>
            <div className='review_right'>
                <h2 className='review_headers'>COOKING NOTES</h2>
                <div>
                    <h4 className='post_review_title'>Add Note</h4>
                    <div className='post_review_container'>
                        <TextareaAutoSize
                            value={review}
                            onChange={e => setReview(e.target.value)}
                            className='post_review'
                            onKeyUp={handlePostReview}
                            placeholder='Share your notes with other cooks...'
                        />
                        <span className={review.length >= 1800 ? review.length >= 2000 ? 'at_limit' : 'approaching_limit' : 'within_limit'}>{review.length} / 2000</span>
                    </div>
                    <div className='submit_review_container'>
                        <div className={`privacy_selector_main`}>
                            <p className={isPrivate ? 'privacy_unselected' : 'privacy_selected'} onClick={() => setIsPrivate(false)}>Public</p>
                            <p className={isPrivate ? "privacy_selected" : "privacy_unselected"} onClick={() => setIsPrivate(true)}>Private</p>
                        </div>
                        <div className='submit_cancel_review'>
                            {!!review.length && <span onClick={() => setReview('')}>Cancel</span>}
                            <button className='submit_review' onClick={handlePostReview}>Submit</button>
                        </div>
                    </div>
                    <div className='review_container'>
                    <div className='review_filter'>
                        <h3 id='public_comments' className={viewPrivate ? "hidden_comments" : "visible_comments"} onClick={() => setViewPrivate(false)}>Public ({totalPublicComments})</h3>
                        <h3 className={viewPrivate ? "visible_comments" : "hidden_comments"} onClick={() => setViewPrivate(true)}>Private ({totalPrivateComments})</h3>
                    </div>
                        {!sortedReviews.length && <h2>Be the first to post a note!</h2>}
                        {sortedReviews.map(review => {
                            if (!review.private && !viewPrivate){
                               return <ReviewTile review={review} key={`review${review.id}`}/>
                            } else if (review.private && viewPrivate && sessionUser?.id == review.user_id) {
                                return <ReviewTile review={review} key={`review${review.id}`} />
                            }
                        })}
                    </div>
                </div>
            </div>
        </div>
    )
}
