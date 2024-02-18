import { useEffect } from "react";
import "./RecipeBox.css";
import { Outlet, useNavigate } from "react-router-dom";

export default function RecipeBox() {
    const navigate = useNavigate();

    useEffect(() => {
        window.scrollTo(0, 0);
    }, [])

    function addActiveClass(e) {
        const links = document.querySelectorAll('.saved-recipes-nav-link');
        links.forEach(link => link.classList.remove('active'));

        e.currentTarget.classList.add('active');
     }

    return (
        <div className="saved-recipe-wrapper">
            <div className="saved-recipe-left-wrapper">
                <ul
                    className="saved-recipes-nav-links-container"
                >
                    <li
                        id='saved-recipes'
                        className="saved-recipes-nav-link"
                        onClick={(e) => {
                            addActiveClass(e)
                            navigate('/recipe-box')
                            }}>
                        <i className="fa-solid fa-bookmark fa-lg"/>
                        <p>Saved Recipes</p>
                    </li>
                    <li
                        id='cooked-recipes'
                        className="saved-recipes-nav-link"
                        onClick={(e) => {
                            addActiveClass(e)
                            navigate('/recipe-box/cooked-recipes')
                            }}>
                        <i className="fa-solid fa-circle-check fa-lg"/>
                        <p>Cooked Recipes</p>
                    </li>
                    <li
                        id='recently-viewed'
                        className="saved-recipes-nav-link"
                        onClick={(e) => {
                            addActiveClass(e)
                            navigate('/recipe-box/recently-viewed')
                            }}>
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
