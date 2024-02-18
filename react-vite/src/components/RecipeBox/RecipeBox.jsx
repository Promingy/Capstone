import { useEffect } from "react";
import "./RecipeBox.css";
import { Outlet } from "react-router-dom";

export default function RecipeBox() {

    useEffect(() => {
        window.scrollTo(0, 0);
    }, [])

    return (
        <div className="saved-recipe-wrapper">
            <div className="saved-recipe-left-wrapper">
                <ul className="saved-recipes-nav-links-container">
                    <li className="saved-recipes-nav-link">
                        <i className="fa-solid fa-bookmark fa-lg"/>
                        <p>Saved Recipes</p>
                    </li>
                    <li className="saved-recipes-nav-link">
                        <i className="fa-solid fa-circle-check fa-lg"/>
                        <p>Cooked Recipes</p>
                    </li>
                    <li className="saved-recipes-nav-link">
                        <i className="fa-regular fa-clock fa-lg"/>
                        <p>Recently Viewed</p>
                    </li>
                </ul>
            </div>
            <div className="saved-recipe-right-wrapper">
                <Outlet />
            </div>
        </div>
    )
}
