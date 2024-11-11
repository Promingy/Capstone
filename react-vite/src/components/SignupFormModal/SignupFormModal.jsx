import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import TextareaAutoSize from 'react-textarea-autosize'
import "./SignupForm.css";
import { thunkDeleteImage, thunkUploadImage } from "../../redux/recipe";
import LoginFormModal from "../LoginFormModal/LoginFormModal";

function SignupFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [bio, setBio] = useState("")
  const [profilePic, setProfilePic] = useState("")
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal, setModalContent } = useModal();
  const [submitted, setSubmitted] = useState(false)
  const [ tempImage, setTempImage] = useState(null)

  useEffect(() => {
    // Listen for the message from the popup
    const messageHandler = (e) => {
      if (e.data === 'oauth-success') {
        closeModal()
        window.location.reload();
      }
    }

    window.addEventListener('message', messageHandler)

    // Clean up listener when component unmounts
    return () => {
      window.removeEventListener('message', messageHandler)
    }
  }, [])

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (submitted || bio.length > 1000) return

    setSubmitted(true)

    if (password !== confirmPassword) {
      setSubmitted(false)
      return setErrors({
        confirmPassword:
          "Confirm Password field must be the same as the Password field",
      });
    }

    const formData = new FormData()
    formData.append('image', profilePic)

    const returnImage = await dispatch(thunkUploadImage(formData))

    const serverResponse = await dispatch(
      thunkSignup({
        email,
        first_name: firstName,
        last_name: lastName,
        bio,
        profile_pic: returnImage?.url,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
      setSubmitted(false)

      if (returnImage.url) dispatch(thunkDeleteImage(returnImage.url))

    } else {
      closeModal();
    }
  };

  function handleOAuthClick(e) {
    e.preventDefault();

    // Open the OAuth URL in a popup window
    // const oauthUrl = "http://localhost:5173/api/auth/oauth_login";
    const oauthUrl = "https://recipes.corbinainsworth.com/api/auth/oauth_login";
    const title = "OAuth"
    const params = "width=800,height=600,location=no,toolbar=no,scrollbars=yes,resizable=yes,popup=yes"
    
    window.open(oauthUrl, title, params);
  }

  function previewImageSetter(e) {
    e.stopPropagation();

    const tempFile = e.target.files[0]

    if (!tempFile) {
        setTempImage (null)
        setProfilePic (null)
        return
    }

    // Check for max image size of 5mb
    if (tempFile?.size > 5000000) {
        return setErrors({profile_pic: "Selected image exceeds the maximum file size of 5MB"})
    }

    const newImgURL = URL.createObjectURL(tempFile); //generate a local url to render the image
    setTempImage(newImgURL)
    setProfilePic(tempFile)
}

  return (
    <div className="signup_form_container">
      <div className="signup_container_left">
    <h4 className="login_image_header">Unlock Recipe Rendezvous recipes and your personal recipe box with a free account.</h4>
        <img className="signup_image" src="https://recipe-rendezvous.s3.us-west-2.amazonaws.com/Mise-en-Place-Meal-Prep-3-960x1440+(1).png"/>
      </div>
      <div className="signup_container_right">
        <h1 className="signup_header">Sign Up</h1>
        {errors.server && <p>{errors.server}</p>}
        <form className='signup_form' onSubmit={handleSubmit}>
          <label className="signup_input">
            <p className="signup_errors">{errors.email && `*${errors.email}`}</p>
            <input
              placeholder="Email"
              className={errors.email && 'signup_error_inputs'}
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </label>
          <label className="signup_input">
            <p className="signup_errors">{errors.first_name && `*${errors.first_name}`}</p>
            <input
              placeholder="First Name"
              type="text"
              className={errors.first_name && 'signup_error_inputs'}
              value={firstName}
              onChange={(e) => setFirstName(e.target.value)}
              required
            />
          </label>
          <label className="signup_input">
            <p className="signup_errors">{errors.last_name && `*${errors.last_name}`}</p>
            <input
              placeholder="Last Name"
              type="text"
              className={errors.last_name && 'signup_error_inputs' }
              value={errors?.last_name || lastName}
              onChange={(e) => setLastName(e.target.value)}
              required
            />
          </label>
          <label className="signup_input">
            <p className="signup_errors">{errors.bio && `*${errors.bio}`}</p>
            <div className="bio_container">
              <TextareaAutoSize
                placeholder="Bio"
                className={`bio_text ${errors.bio ? 'signup_error_container' : ''}`}
                value={bio}
                onChange={e => setBio(e.target.value)}
                required
              />
              <span className={bio.length > 800 ? bio.length > 1000 ? "at_limit": "approaching_limit": "within_limit"}>{bio.length} / 1000</span>
            </div>
          </label>
          <div className="signup_input">
            <p className="signup_errors">{errors.profile_pic && `*${errors.profile_pic}`}</p>
            <div className="file_input_container">
              <input
                type='file'
                className={`profile_pic_input ${errors.profile_pic && 'signup_error_inputs'}`}
                accept='image/*'
                onChange={previewImageSetter}
              />
              <div className="signup_image_container">
                <i className="fa-regular fa-plus fa-xl temp_image_icon"/>
                <img className="temp_image_signup" src={tempImage}/>
              </div>
            </div>
          </div>
          <label className="signup_input">
            <p className="signup_errors signup_errors_password">{errors.confirmPassword && `*${errors.confirmPassword}`}</p>
            <input
              placeholder="Password"
              type="password"
              value={password}
              className={errors.confirmPassword && 'signup_error_inputs'}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </label>
          {errors.password && <p>{errors.password}</p>}
          <label className="signup_input">
            <input
              placeholder="Confirm Password"
              type="password"
              value={confirmPassword}
              className={errors.confirmPassword && 'signup_error_inputs'}
              onChange={(e) => setConfirmPassword(e.target.value)}
              required
            />
          </label>
          <button className="login_button_submit" disabled={bio.length > 1000} type="submit">Sign Up</button>
          {/* <a className="oAuth" href={`https://recipe-rendezvous.onrender.com/api/auth/oauth_login`}>
            <button type='button'>
              <img className="google_icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" />
              &nbsp; Continue with Google
            </button>
          </a> */}
          <a className="oAuth" href="#" onClick={handleOAuthClick}>
            <button type='button'>
              {/* <i className="fa-brands fa-google"/> */}
              <img className="google_icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/google/google-original.svg" />
              &nbsp; Continue with Google
            </button>
          </a>
          <span className="or_sign_up" onClick={() => setModalContent(<LoginFormModal />)}>Log in</span>
        </form>
      </div>
    </div>
  );
}

export default SignupFormModal;
