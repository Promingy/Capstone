const initialState = {}

const POST_REVIEW = 'review/POST_REVIEW'

const actionPostReview = (review) => {
    return {
        type: POST_REVIEW,
        review
    }
}

export const thunkPostReview = (review, recipeId) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}/reviews`, {
        method: 'POST',
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(review)
    })
}

function reviewReducer(state = initialState, action) {
    switch(action.type){
        default:
            return state
    }
}

export default reviewReducer
