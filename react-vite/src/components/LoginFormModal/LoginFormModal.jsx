import { useState, useEffect } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import SignupFormModal from '../SignupFormModal'
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal, setModalContent } = useModal();
  const [submitted, setSubmitted] = useState(false)
  const demoUser = {
    email: 'demo@aa.io',
    password: 'password'
  }

  useEffect(() => {
    // listen for messaage from popup
    const messageHandler = msg => {
      if (msg.data == 'oauth-success') {
        closeModal();
        window.location.reload();
      }
    }

    window.addEventListener("message", messageHandler)

    return () => window.removeEventListener("message", messageHandler)
  }, [])

  const handleOAuthClick = (e) => {
    e.preventDefault();

    // Open the OAuth URL in a popup window
    const oAuthUrl = "https://recipes.corbinainsworth.com/api/auth/oauth_login";
    const title = "OAuth";
    const params = "width=800,height=600,location=no,toolbar=no,scrollbars=yes,resizable=yes,popup=yes"

    window.open(oAuthUrl, title, params);
  }

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (submitted) return

    setSubmitted(true)

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
      setSubmitted(false)
    } else {
      closeModal();
    }
  };

  return (
    <div className="login_form_container">
      <div className="login_modal_left">
        <h4 className="login_image_header">Unlock Recipe Rendezvous recipes and your personal recipe box with a free account.</h4>
        <img className="login_image" src="https://recipe-rendezvous.s3.us-west-2.amazonaws.com/Mise-en-Place-Meal-Prep-3-960x1440+(1).png" />
      </div>
      <div className="login_modal_right">
        <h1 className="login_header">Log In</h1>
        <form className="login_form" onSubmit={handleSubmit}>
          <label>
            <p className="login_errors">{errors.email && `*${errors.email}`}</p>
            <input
              type="email"
              placeholder="Email"
              className={errors.email && 'login_error_inputs'}
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
          <label>
            <p className="login_errors">{errors.password && `*${errors.password}`}</p>
            <input
              placeholder="Password"
              type="password"
              className={errors.password && 'login_error_inputs'}
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          <button className="login_button_submit" type="submit">Log In</button>
          {/* <a className="oAuth" href={`https://recipe-rendezvous.onrender.com/api/auth/oauth_login`}> */}
          <a className="oAuth" href="#" onClick={handleOAuthClick}>
            <button type='button'>
              {/* <i className="fa-brands fa-google"/> */}
              <img className="google_icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" />
              &nbsp; Continue with Google
            </button>
          </a>
          <button type='button' className="demo_button_submit" onClick={() => dispatch(thunkLogin(demoUser)).then(closeModal)}>Demo User</button>
          <span className="or_sign_up" onClick={() => setModalContent(<SignupFormModal />)}>Sign up</span>
        </form>
      </div>
    </div>
  );
}

export default LoginFormModal;
