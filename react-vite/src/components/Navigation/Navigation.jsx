import {  useNavigate } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import { useState } from "react";

function Navigation() {
  const navigate = useNavigate()
  const [showMenu, setShowMenu] = useState(false)
  let timeout1;
  let timeout2;

  function createDelay() {
    clearTimeout(timeout1)
    clearTimeout(timeout2)

    timeout1 = null
    timeout2 = null

    setShowMenu(true)
  }

  function removeDelay() {
    clearTimeout(timeout2)

    timeout2 = null

    setShowMenu(false)
  }

  return (
    <div className="nav_bar">
      <div className="header_top_container">
        <img className="logo_image" onClick={() => navigate('/')} src="https://recipe-rendezvous.s3.us-west-2.amazonaws.com/recipe-rendezvous-high-resolution-logo-transparent+(1).png" />
        <div className="header_top_right">
          <h3 className="your_recipe_box">
            {/* <i className="fa-bookmark fa-solid"/> &nbsp; */}
            {/* Your Recipe Box */}
            </h3>
          <ProfileButton />
        </div>
      </div>

      <div className="header_bottom_container">
        <h2 className="nav_links" onClick={() => navigate('/')}>Home</h2>
        <div>
        <h2 className='nav_links'
          onMouseOver={() => {
            clearTimeout(timeout1)
            clearTimeout(timeout2)

            timeout1 = null
            timeout2 = null
            
            timeout1 = setTimeout(createDelay, 250)
          }}
          onMouseLeave={() => {
            clearTimeout(timeout1)
            clearTimeout(timeout2)

            timeout1 = null
            timeout2 = null

            timeout2 = setTimeout(removeDelay, 250)
          }}
          >
            About
            {showMenu &&
              <div className="about_me_menu">
                <a
                  className="about_me_links"
                  target="_blank"
                  rel='noreferrer'
                  href="https://github.com/Promingy"
                  >
                    <i className="fa-brands fa-github"/>
                    Corbin&apos;s Github
                </a>
                <a
                  className="about_me_links"
                  target="_blank"
                  rel='noreferrer'
                  href="https://github.com/Promingy/Capstone">
                    <i className="fa-brands fa-git-alt"/>
                    Project Repo
                </a>
              </div>
            }
        </h2>
        </div>
      </div>

    </div>
  );
}

export default Navigation;
