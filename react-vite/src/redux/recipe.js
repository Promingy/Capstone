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

const initialState = {}
function recipeReducer(state=initialState, action){
    switch (action.type){
        case GET_ALL_RECIPES: {
            const newState = { ...state }
            for (let recipe of action.recipes) {
                newState[recipe.id] = recipe
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
