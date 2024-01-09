import { actionAddRating, actionRemoveRating, actionUpdateRating } from "./recipe"

const POST_REVIEW = 'review/POST_REVIEW'
const POST_RATING = 'review/POST_RATING'

const actionPostReview = (review) => {
    return {
        type: POST_REVIEW,
        review
    }
}

const actionPostRating = (rating) => {
    return {
        type: POST_RATING,
        rating
    }
}

export const thunkPostReview = (review, recipeId) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}/reviews`, {
        method: 'POST',
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(review)
    })
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
