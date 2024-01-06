import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import PreferencesModal from "../PreferencesModal/PreferencesModal.jsx";
import { useNavigate } from "react-router-dom";

function ProfileButton() {
  const navigate = useNavigate()
  const dispatch = useDispatch();
  const [showMenu, setShowMenu] = useState(false);
  const user = useSelector((store) => store.session.user);
  const ulRef = useRef();
  const [togglePref, setTogglePref] = useState(false)
  const [togglePref2, setTogglePref2] = useState(false)

  const toggleMenu = (e) => {
    e.stopPropagation(); // Keep from bubbling up to document and triggering closeMenu
    // setShowMenu(!showMenu);
    if (user){
      setTogglePref(true)

      window.addEventListener('mousedown', handleMouseClick)
    }
  };

  useEffect(() => {
    if (!showMenu) return;

    const closeMenu = (e) => {
      if (ulRef.current && !ulRef.current.contains(e.target)) {
        setShowMenu(false);
      }
    };

    document.addEventListener("click", closeMenu);

    return () => document.removeEventListener("click", closeMenu);
  }, [showMenu]);

  const closeMenu = () => setShowMenu(false);

  function logout () {
    dispatch(thunkLogout());
    closeMenu();
  };

  useEffect(() => {
    // if the url has changed, and the prefModal is open, close the modal
    if (togglePref) closePref()
  }, [window.location.href])

  // handle closing the preference slide out bar
  function closePref() {
      setTogglePref(false)
      setTogglePref2(true)
      setTimeout(() => setTogglePref2(false), 350)
      return window.removeEventListener('mousedown', handleMouseClick)
  }

  function handleMouseClick (e) {
    if (!e) return closePref()

    e.preventDefault()
    // get items that can and can't be clicked on
    const xBtn = document.getElementById('xmark')
    const prefModal = document.getElementById('preference_modal_container')
    const background = document.getElementById('background_color_pref')
    const createRecipe = document.getElementById('create_recipe')
    const logout_button = document.getElementById('logout_button')
    const conditions = [xBtn, background]
    let node = e.target

    // iterate over the e.target to verify if we're clicking off the modal or on the exit button
    for (let i = 0; i < 4; i++){
      // if clicking off modal, or on exit button, close modal
      if (conditions.some(ele => ele === node)) closePref()

      // if clicking logout, close modal AND logout
      else if (node === logout_button) {
        closePref()
        logout()
      }

      else if (node === createRecipe) {
        closePref()
        navigate('/new-recipe')
      }

      // check if e.target is our preference modal, if so, do nothing
      else if (node === prefModal) return

      // if none of the previous are true, set the node to the parent node of current e.target
      else node = node.parentNode
    }

    window.removeEventListener('mousedown', handleMouseClick)
  }

  return (
    <>
    {user &&
      <i onClick={toggleMenu} className="fas fa-user user_profile" />
    }

    {!user &&

    <div className='log_in_sign_up_buttons'>
      <div className="login_button">
        <OpenModalMenuItem
          itemText='Login'
          modalComponent={<LoginFormModal />}
        />
      </div>

      <div className="sign_up_button">
      <OpenModalMenuItem
          itemText='Sign Up'
          onItemClick={closeMenu}
          modalComponent={<SignupFormModal />}
        />
      </div>
    </div>
    }

      { togglePref && <PreferencesModal />}
      { togglePref2 &&  <PreferencesModal close={true} />}
    </>
  );
}

export default ProfileButton;
