import { useEffect } from "react";
import "./SavedRecipes.css";

export default function SavedRecipes() {

    useEffect(() => {
        window.scrollTo(0, 0);
    }, [])

    return (
        <div className="saved-recipe-wrapper">
            <div className="saved-recipe-left-wrapper">
                <ul className="saved-recipes-nav-links-container">
                    <li className="saved-recipes-nav-link">
                        <i className="fa-solid fa-bookmark fa-lg"/>
                        <h3>Saved Recipes</h3>
                    </li>
                    <li className="saved-recipes-nav-link">
                        <h3>Cooked Recipes</h3>
                    </li>
                    <li className="saved-recipes-nav-link">
                        <h3>Recently Viewed</h3>
                    </li>
                </ul>
            </div>
            <div className="saved-recipe-right-wrapper">
                <h3>Saved Recipes</h3>
                test
            </div>
        </div>
    )
}
