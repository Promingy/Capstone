import { useState, useEffect, useRef } from "react";
import { useDispatch, useSelector } from "react-redux";
import { thunkLogout } from "../../redux/session";
import OpenModalMenuItem from "./OpenModalMenuItem";
import LoginFormModal from "../LoginFormModal";
import SignupFormModal from "../SignupFormModal";
import PreferencesModal from "../PreferencesModal/PreferencesModal.jsx";

function ProfileButton() {
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

  const logout = () => {
    dispatch(thunkLogout());
    closeMenu();
  };

  function handleMouseClick (e) {
    e.preventDefault()
    const xBtn = document.getElementById('xmark')
    const prefModal = document.getElementById('pref_modal')
    const background = document.getElementById('background_color_pref')
    const logout_button = document.getElementById('logout_button')
    const conditions = [xBtn, background]
    let node = e.target

    for (let i = 0; i < 4; i++){
      console.log(node)
      if (conditions.some(ele => ele === node)){
        setTogglePref(false)
        setTogglePref2(true)
        setTimeout(() => setTogglePref2(false), 350)
        return window.removeEventListener('mousedown', handleMouseClick)
      }

      else if (node === logout_button) {
        setTogglePref(false)
        setTogglePref2(true)
        logout()
        setTimeout(() => setTogglePref2(false), 350)
        return window.removeEventListener('mousedown', handleMouseClick)
      }

      else if (node === prefModal) return

      else node = node.parentNode
    }
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
          onItemClick={closeMenu}
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
      { togglePref2 && <PreferencesModal close={true}/>}
    </>
  );
}

export default ProfileButton;
