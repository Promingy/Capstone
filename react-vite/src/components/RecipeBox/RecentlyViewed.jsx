import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux"
import { thunkGetRecentlyViewed } from "../../redux/recipe";
import RecipeTile from "../MainPage/RecipeTile";

export default function RecentlyViewed() {
    const dispatch = useDispatch();
    const sessionUser = useSelector(state => state.session.user);
    const allRecipes = useSelector(state => state.recipes);
    const recentlyViewed = allRecipes.recentlyViewed;

    useEffect(() => {
        dispatch(thunkGetRecentlyViewed(sessionUser.id))
    }, [])

    if (!recentlyViewed) return null;

    return (
        <div className="saved-recipes-wrapper">
            <div className="saved-recipes-header-container">
                <h2 className="saved-recipes-header">Recently Viewed</h2>
                <p className="saved-recipes-subheader">{recentlyViewed.length} recipes</p>
            </div>

            <div className="saved-recipes-container">
                {recentlyViewed && recentlyViewed.map(recipe => {
                    return (
                        <RecipeTile key={recipe.id} recipe={recipe} />
                    )
                })}
            </div>
        </div>
    )
}
