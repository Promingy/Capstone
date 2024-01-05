const GET_ALL_RECIPES = 'recipe/getAllRecipes'
const GET_SELECTED_RECIPE = 'recipe/getSelectedRecipe'

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
        body: JSON.stringify({
            "category_id": 1,
            "title": "the best meal ever",
            "description": "I just said it was the best thing in the entire universe",
            "servings": 3,
            "prep_time": 5,
            "cook_time": 20,
            "preview_image": "http://.png"
        })
    })
    console.log('TEST', await res.json())
    return res
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
        case GET_SELECTED_RECIPE: {
            const newState = { ...state }
            newState[action.recipe.id] = action.recipe
            return newState
        }
        default:
            return state
    }
}

export default recipeReducer
