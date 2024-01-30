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
    <div className="nav_bar_container">
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
            onClick={() => {
              setShowMenu(true)
              navigate('/about-me')
            }}
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
                  <p className="about_me_header">Quick Links</p>
                  <div className="link-section-container">
                    <div>
                      <a className="about_me_links"
                        onClick={(() => navigate('/about-me'))}
                      >
                        <i className="fa-solid fa-user-ninja"/>
                        About Me
                      </a>
                      <a className="about_me_links"
                        target="_blank"
                        rel='noreferrer'
                        href="https://promingy.github.io"
                      >
                        <i className="fa-solid fa-address-card"/>
                        Portfolio
                      </a>
                      <a className="about_me_links"
                        target="_blank"
                        rel='noreferrer'
                        href="https://www.linkedin.com/in/corbin-ainsworth-18a885232/"
                      >
                        <i className="fa-brands fa-linkedin"/>
                        LinkedIn
                      </a>
                    </div>
                    <div>
                      <a
                        className="about_me_links"
                        target="_blank"
                        rel='noreferrer'
                        href="https://github.com/Promingy/Capstone">
                          <i className="fa-brands fa-git-alt"/>
                          Project Repo
                      </a>
                      <a
                        className="about_me_links"
                        target="_blank"
                        rel='noreferrer'
                        href="https://github.com/Promingy"
                        >
                          <i className="fa-brands fa-github"/>
                          Github
                      </a>
                    </div>
                  </div>
                </div>
              }
          </h2>
          </div>
          <h2 className="nav_links" >
            Contact
          </h2>
          {/* <h2 className="nav_links">
            Future Features
          </h2> */}
        </div>

      </div>
    </div>
  );
}

export default Navigation;
