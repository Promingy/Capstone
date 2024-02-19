const GET_ALL_RECIPES = 'recipe/getAllRecipes'
const GET_SAVED_RECIPES = 'recipe/getSavedRecipes'
const GET_SELECTED_RECIPE = 'recipe/getSelectedRecipe'
const CREATE_RECIPE = 'recipe/createRecipe'
const UPDATE_RECIPE = 'recipe/updateRecipe'
const DELETE_RECIPE = 'recipe/deleteRecipe'
const ADD_RATING =  'recipe/addRating'
const REMOVE_RATING = 'recipe/removeRating'
const UPDATE_RATING = 'recipe/updateRating'
const POST_REVIEW = 'recipe/postReview'
const DELETE_REVIEW = 'recipe/deleteReview'
const UPDATE_REVIEW = 'recipe/updateReview'
const LIKE_REVIEW = 'recipe/likeReview'
const DELETE_LIKE = 'recipe/deleteLike'
const SAVE_RECIPE = 'recipe/saveRecipe'
const UNSAVE_RECIPE = 'recipe/unsaveRecipe'

const actionGetAllRecipes = (recipes) => {
    return {
        type: GET_ALL_RECIPES,
        recipes
    }
}

const actionGetSavedRecipes = (recipes) => {
    return {
        type: GET_SAVED_RECIPES,
        recipes
    }
}

const actionGetSelectedRecipe = (recipe) => {
    return {
        type: GET_SELECTED_RECIPE,
        recipe
    }
}

const actionCreateRecipe = (recipe) => {
    return {
        type: CREATE_RECIPE,
        recipe
    }
}

const actionSaveRecipe = (recipeId) => {
    return {
        type: SAVE_RECIPE,
        recipeId
    }
}

const actionUnsaveRecipe = (recipeId) => {
    return {
        type: UNSAVE_RECIPE,
        recipeId
    }
}

const actionUpdateRecipe = (recipe) => {
    return {
        type: UPDATE_RECIPE,
        recipe
    }
}

const actionDeleteRecipe = (recipe) => {
    return {
        type: DELETE_RECIPE,
        recipe
    }
}

export const actionAddRating = (rating) => {
    return {
        type: ADD_RATING,
        rating
    }
}

export const actionRemoveRating = (ratingId) => {
    return {
        type: REMOVE_RATING,
        ratingId
    }
}

export const actionUpdateRating = (rating) => {
    return {
        type: UPDATE_RATING,
        rating
    }
}

export const actionPostReview = (review) => {
    return {
        type: POST_REVIEW,
        review
    }
}

export const actionDeleteReview = (review) => {
    return {
        type: DELETE_REVIEW,
        review
    }
}

export const actionUpdateReviw = (review) => {
    return {
        type: UPDATE_REVIEW,
        review
    }
}

export const actionLikeReview = (reviewId, user, recipeId) => {
    return {
        type: LIKE_REVIEW,
        reviewId,
        user,
        recipeId
    }
}

export const actionDeleteLike = (reviewId, user, recipeId) => {
    return {
        type: DELETE_LIKE,
        reviewId,
        user,
        recipeId
    }
}

export const thunkGetAllRecipes = () => async(dispatch) => {
    const res = await fetch(`/api/recipes`)

    if (res.ok){
        const data = await res.json()
        dispatch(actionGetAllRecipes(data))
        return data
    }
    return await res.json()
}

export const thunkGetSavedRecipes = (userId) => async(dispatch) => {
    const res = await fetch(`/api/users/${userId}/saved-recipes`)

    if (res.ok){
        const data = await res.json()
        dispatch(actionGetSavedRecipes(data.saved_recipes))
        return data
    }
    return await res.json()

}


export const thunkGetSelectedRecipe = (recipeId) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}`)

    if (res.ok){
        const data = await res.json()
        dispatch(actionGetSelectedRecipe(data))
    }
}

export const thunkSaveRecipe = (recipe) => async(dispatch) => {
    const res = await fetch(`/api/recipes/${recipe.id}/save`, {
        method: "POST"
    })

    const data = await res.json()

    if (res.ok){
        dispatch(actionSaveRecipe(recipe.id))
    }

    return data

}

export const thunkUnsaveRecipe = (recipe) => async(dispatch) => {
    const res = await fetch(`/api/recipes/${recipe.id}/unsave`, {
        method: "DELETE"
    })

    const data = await res.json()

    if (res.ok){
        dispatch(actionUnsaveRecipe(recipe.id))
    }

    return data
}

export const thunkCreateRecipe = (recipe) => async (dispatch) => {
    const res = await fetch("/api/recipes", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(recipe)
    })

    if (res.ok){
        const data = await res.json()
        dispatch(actionCreateRecipe(data))
        return data
    }

    return await res.json()
}

export const thunkUpdateRecipe = (recipeId, recipe) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(recipe)
    })

    if (res.ok) {
        const data = await res.json()
        dispatch(actionUpdateRecipe(data))
        return data
    }

    return await res.json()
}

export const thunkDeleteRecipe = (recipe) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipe.id}`, {
        method: "DELETE"
    })

    const data = await res.json()

    if (res.ok){
        dispatch(actionDeleteRecipe(recipe))
    }
    return data
}

export const thunkUploadImage = (image) => async (dispatch) => {
    const res = await fetch('/api/image_routes',{
        method: "POST",
        body: image
    })

    const data = await res.json()
    if (res.ok) {
        return data
    }

    return data
}

export const thunkDeleteImage = (imageUrl) => async (dispatch) => {
    const img = imageUrl.split('/')[imageUrl.split('/').length - 1]
    const res = await fetch (`/api/image_routes/${img}`, {
        method: "DELETE"
    })

    return await res.json()
}

const initialState = {}
function recipeReducer(state=initialState, action){
    switch (action.type){
        case GET_ALL_RECIPES: {
            const newState = { ...state, categories: {} }

            for (let category in action.recipes) {
                newState.categories[category] = {}

                for (let recipe of action.recipes[category]){
                    newState.categories[category][recipe.id] = recipe
                    newState[recipe.id] = recipe
                }
            }

            return newState
        }
        case GET_SAVED_RECIPES: {
            const newState = { ...state, savedRecipes: {}};

            for (let recipe in action.recipes){
                newState.savedRecipes[recipe] = action.recipes[recipe];
            }

            return newState;
        }
        case SAVE_RECIPE: {
            const newState = { ...state }

            newState[action.recipeId].saved = true

            return newState
        }
        case UNSAVE_RECIPE: {
            const newState = { ...state }

            delete newState[action.recipeId].saved

            if (newState.savedRecipes) {
                delete newState.savedRecipes[action.recipeId]
            }

            return newState
        }
        case GET_SELECTED_RECIPE: {
            const newState = { ...state }

            newState[action.recipe.id] = action.recipe

            const newReviews = {}

            for (let review of newState[action.recipe.id].reviews) {
                newReviews[review.id] = review
            }

            newState[action.recipe.id].reviews = newReviews

            return newState
        }
        case CREATE_RECIPE: {
            const newState = { ...state, categories: {[action.recipe.category_id]: {}} }

            newState[action.recipe.id] = action.recipe

            newState.categories[action.recipe.category_id][action.recipe.id] = action.recipe

            return newState
        }
        case UPDATE_RECIPE: {
            const newState = { ...state }

            newState[action.recipe.id] = action.recipe

            return newState
        }
        case DELETE_RECIPE: {
            const newState = { ...state }
            delete newState[action.recipe.id]

            if (newState.categories) {
                delete newState.categories[+action.recipe.category_id][action.recipe.id]
            }

            return newState
        }
        case ADD_RATING: {
            const newState = { ...state }

            newState[action.rating.recipe_id].all_ratings ++

            newState[action.rating.recipe_id].user_rating = action.rating

            let newAvg = action.rating.rating

            for (let rating of newState[action.rating.recipe_id].ratings){
                newAvg += rating.rating
            }

            newState[action.rating.recipe_id].avg_rating = newAvg / newState[action.rating.recipe_id].all_ratings

            return newState
        }
        case UPDATE_RATING: {
            const newState = { ...state }
            
            newState[action.rating.recipe_id].user_rating = action.rating

            let newAvg = action.rating.rating

            for (let rating of newState[action.rating.recipe_id].ratings){
                if (rating.id != action.rating.id){
                    newAvg += rating.rating
                }
            }

            newState[action.rating.recipe_id].avg_rating = (newAvg / newState[action.rating.recipe_id].all_ratings) || 0

            return newState
        }
        case REMOVE_RATING: {
            const newState = { ...state }
            newState[action.ratingId.recipe_id].all_ratings --
            let newAvg = 0

            for (let rating of newState[action.ratingId.recipe_id].ratings){
                if (rating.id != action.ratingId.id){
                    newAvg += rating.rating
                }
            }
            newState[action.ratingId.recipe_id].avg_rating = newAvg / newState[action.ratingId.recipe_id].all_ratings || 0

            return newState
        }
        case POST_REVIEW: {
            const newState = { ...state }
            newState[action.review.recipe_id].reviews[action.review.id] = action.review
            return newState
        }
        case UPDATE_REVIEW: {
            const newState = { ...state }
            newState[action.review.recipe_id].reviews[action.review.id] = action.review
            return newState
        }
        case DELETE_REVIEW: {
            const newState = { ...state }

            delete newState[action.review.recipe_id].reviews[action.review.id]

            return newState
        }
        case LIKE_REVIEW: {
            const newState = { ...state }
            newState[action.recipeId].reviews[action.reviewId].review_likes[action.user.id] = action.user
            return newState
        }
        case DELETE_LIKE: {
            const newState = { ...state }
            delete newState[action.recipeId].reviews[action.reviewId].review_likes[action.user.id]
            return newState
        }
        default:
            return state
    }
}

export default recipeReducer
