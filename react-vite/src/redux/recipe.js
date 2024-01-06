const GET_ALL_RECIPES = 'recipe/getAllRecipes'
const GET_SELECTED_RECIPE = 'recipe/getSelectedRecipe'
const CREATE_RECIPE = 'recipe/createRecipe'
const DELETE_RECIPE = 'recipe/deleteRecipe'

const actionGetAllRecipes = (recipes) => {
    return {
        type: GET_ALL_RECIPES,
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

const actionDeleteRecipe = (recipe) => {
    return {
        type: DELETE_RECIPE,
        recipe
    }
}

export const thunkGetAllRecipes = () => async(dispatch) => {
    const res = await fetch(`/api/recipes`)

    if (res){
        const data = await res.json()
        dispatch(actionGetAllRecipes(data))
    }
    return res
}

export const thunkGetSelectedRecipe = (recipeId) => async (dispatch) => {
    const res = await (fetch(`/api/recipes/${recipeId}`))

    if (res.ok){
        const data = await res.json()
        dispatch(actionGetSelectedRecipe(data))
    }
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

    return res.json()
}

export const thunkUpdateRecipe = (recipeId) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipeId}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            "category_id": 2,
            "title": "the SECOND best meal ever",
            "description": "THIS MEAL IS ONLY PARITLALLY THE BEST",
            "servings": 4,
            "prep_time": 15,
            "cook_time": 30,
            "preview_image": "http://.png"
        })
    })

    return res
}

export const thunkDeleteRecipe = (recipe) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipe.id}`, {
        method: "DELETE"
    })

    if (res.ok){
        dispatch(actionDeleteRecipe(recipe))
    }
    return res
}

const initialState = {}
function recipeReducer(state=initialState, action){
    switch (action.type){
        case GET_ALL_RECIPES: {
            const newState = { ...state, categories: {} }

            for (let category in action.recipes) {
                console.log('category', category, action)
                newState.categories[category] = {}

                for (let recipe of action.recipes[category]){
                    newState.categories[category][recipe.id] = recipe
                    newState[recipe.id] = recipe
                }
            }

            return newState
        }
        case GET_SELECTED_RECIPE: {
            const newState = { ...state }
            newState[action.recipe.id] = action.recipe
            return newState
        }
        case CREATE_RECIPE: {
            const newState = { ...state }
            newState[action.recipe.id] = action.recipe
            return newState
        }
        case DELETE_RECIPE: {
            const newState = { ...state }
            delete newState[action.recipe.id]
            delete newState.categories[action.recipe.category_id][action.recipe.id]
            return newState
        }
        default:
            return state
    }
}

export default recipeReducer
