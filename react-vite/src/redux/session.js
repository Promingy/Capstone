const SET_USER = 'session/setUser';
const REMOVE_USER = 'session/removeUser';
const GET_USER_RECIPES = 'recipe/getUserRecipes';


const setUser = (user) => ({
  type: SET_USER,
  payload: user
});

const removeUser = () => ({
  type: REMOVE_USER
});

const actionGetUserRecipes = (recipes, ownerId) => {
  return {
      type: GET_USER_RECIPES,
      recipes,
      ownerId
  }
}

export const thunkAuthenticate = () => async (dispatch) => {
	const response = await fetch("/api/auth/");
	if (response.ok) {
		const data = await response.json();
		if (data.errors) {
			return;
		}

		dispatch(setUser(data));
	}
};

export const thunkLogin = (credentials) => async dispatch => {
  const response = await fetch("/api/auth/login", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(credentials)
  });

  if(response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
  } else if (response.status < 500) {
    const errorMessages = await response.json();
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
};

export const thunkSignup = (user) => async (dispatch) => {
  const response = await fetch("/api/auth/signup", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(user)
  });

  if(response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
  } else if (response.status < 500) {
    const errorMessages = await response.json();
    return errorMessages
  } else {
    return { server: "Something went wrong. Please try again" }
  }
};

export const thunkLogout = () => async (dispatch) => {
  await fetch("/api/auth/logout");
  dispatch(removeUser());
};

export const thunkGetUserRecipes = (userId) => async (dispatch) => {
  const res = await fetch(`/api/users/${userId}/recipes`)

  const data = await res.json()
  console.log('data', data)
  if (res.ok) {
      dispatch(actionGetUserRecipes(data, userId))
      return data
  }
  return data
}

const initialState = { user: null };

function sessionReducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { ...state, user: action.payload };
    case REMOVE_USER:
      return { ...state, user: null };
    case GET_USER_RECIPES: {
      const newState = { ...state, [action.ownerId]: {} }

        for (let recipe of Object.values(action.recipes)) {
            newState[action.ownerId][recipe.id] = recipe
        }

        return newState
    }
    default:
      return state;
  }
}

export default sessionReducer;
