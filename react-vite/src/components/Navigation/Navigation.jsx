import {  useNavigate } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  const navigate = useNavigate()
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
      </div>
    </div>
  );
}

export default Navigation;
