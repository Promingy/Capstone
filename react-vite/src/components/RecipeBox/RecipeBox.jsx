import { useEffect } from "react";
import { useLocation } from "react-router";
import "./RecipeBox.css";
import { Outlet, useNavigate } from "react-router-dom";

export default function RecipeBox() {
    const navigate = useNavigate();
    const url = useLocation().pathname.split('/')[2];

    useEffect(() => {
        window.scrollTo(0, 0);
    }, [])

    return (
        <div className="recipe-box-wrapper">
            <div className="recipe-box-left-wrapper">
                <ul
                    className="recipe-box-nav-links-container"
                >
                    <li
                        id='saved-recipes'
                        className={`recipe-box-nav-link ${(url === 'all' || url === undefined) && 'active'}`}
                        onClick={(e) => navigate('/recipe-box/all')}>
                        <i className="fa-solid fa-bookmark fa-lg"/>
                        <p>Saved Recipes</p>
                    </li>
                    {/* <li
                        id='cooked-recipes'
                        className={`recipe-box-nav-link ${url === 'cooked-recipes' && 'active'}`}
                        onClick={(e) => navigate('/recipe-box/cooked-recipes')}>
                        <i className="fa-solid fa-circle-check fa-lg"/>
                        <p>Cooked Recipes</p>
                    </li>
                    <li
                        id='recently-viewed'
                        className={`recipe-box-nav-link ${url === 'recently-viewed' && 'active'}`}
                        onClick={(e) => navigate('/recipe-box/recently-viewed')}>
                        <i className="fa-regular fa-clock fa-lg"/>
                        <p>Recently Viewed</p>
                    </li> */}
                </ul>
            </div>
            <div className="recipe-box-right-wrapper">
                <Outlet />
            </div>
        </div>
    )
}
