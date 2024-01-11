import { actionAddRating, actionRemoveRating, actionUpdateRating, actionPostReview, actionDeleteReview, actionUpdateReviw, actionLikeReview, actionDeleteLike } from "./recipe"

export const thunkPostReview = (review, recipeId) => async (dispatch) => {
    console.log('before dispatch', review)
    const res = await fetch(`/api/recipes/${recipeId}/reviews`, {
        method: 'POST',
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(review)
    })

    const data = await res.json()

    if (res.ok){
        dispatch(actionPostReview(data))
    }

    return data
}

export const thunkDeleteReview = (review) => async (dispatch) => {
    const res = await fetch(`/api/reviews/${review.id}`, {
        method: "DELETE"
    })

    const data = await res.json()

    if (res.ok){
        dispatch(actionDeleteReview(review))
    }

    return data
}

export const thunkLikeReview = (reviewId, user, recipeId, method) => async (dispatch) => {
    // handles both post and delete
    console.log('METHDO', method)
    const res = await fetch(`/api/reviews/${reviewId}/likes`, {
        method: method
    })

    const data = await res.json()

    if (res.ok) {
        dispatch(method == 'POST' ? actionLikeReview(reviewId, user, recipeId) : actionDeleteLike(reviewId, user, recipeId))
        return data
    }

    return data
}

export const thunkUpdateReview = (review) => async (dispatch) => {
    const res = await fetch(`/api/reviews/${review.id}`, {
        method: "PUT",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(review)
    })

    const data = await res.json()

    if (res.ok){
        dispatch(actionUpdateReviw(data))
    }

    return data
}

export const thunkPostRating = (rating, recipeId) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}/ratings`, {
        method: "POST",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(rating)
    })

    const data = await res.json()

    if (res.ok){
        dispatch(actionAddRating(data))
        return data
    }

    return data
}

export const thunkUpdateRating = (rating, ratingId) => async (dispatch) => {
    const res = await fetch(`/api/ratings/${ratingId}`,{
        method: "PUT",
        headers: {'Content-Type': "application/json"},
        body: JSON.stringify(rating)
    })

    const data = await res.json()

    if (res.ok) {
        dispatch(actionUpdateRating(data))
        return data
    }
    return data
}

export const thunkDeleteRating = (rating, ratingId) => async (dispatch) => {
    const res = await fetch(`/api/ratings/${ratingId}`, {
        method: 'DELETE'
    })

    const data = await res.json()

    if (res.ok){
        dispatch(actionRemoveRating(rating))
        return data
    }

    return data
}

const initialState = {}

function reviewReducer(state = initialState, action) {
    switch(action.type){
        default:
            return state
    }
}

export default reviewReducer
