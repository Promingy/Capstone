
const initialState = {}

const GET_DROP_DOWNS = 'dropdown/GET_DROP_DOWNS'

const actionGetDropdown = (measurements, categories) => {
    return {
        type: GET_DROP_DOWNS,
        measurements,
        categories
    }
}

export const thunkGetDropdowns = () => async (dispatch) => {
    const res = await fetch('/api/dropdowns')

    if (res.ok) {
        const data = await res.json()
        dispatch(actionGetDropdown(data.measurements, data.categories))
    }
    return res
}

function dropDownReducer(state = initialState, action) {
    switch(action.type){
        case GET_DROP_DOWNS :{
            const newState = { ...state, categories: {}, measurements: {} }

            for (let category of Object.values(action.categories)) {
                newState.categories[category.id] = category
            }

            for (let measurement of Object.values(action.measurements)){
                // newState.measurements[measurement.measurement_name] = measurement
                newState.measurements[measurement.id] = measurement
            }

            return newState
        }
        default:
            return state
    }
}

export default dropDownReducer
