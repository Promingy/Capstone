import { useState } from "react";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import { thunkSignup } from "../../redux/session";
import TextareaAutoSize from 'react-textarea-autosize'
import "./SignupForm.css";
import { thunkDeleteImage, thunkUploadImage } from "../../redux/recipe";

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
  const { closeModal } = useModal();
  const [submitted, setSubmitted] = useState(false)

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

  return (
    <div className="signup_form_container">
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
        <label className="signup_input">
          <p className="signup_errors">{errors.profile_pic && `*${errors.profile_pic}`}</p>
          <input
            type='file'
            className={errors.profile_pic && 'signup_error_inputs test'}
            accept='image/*'
            onChange={e => setProfilePic(e.target.files[0])}
          />
        </label>
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
      </form>
    </div>
  );
}

export default SignupFormModal;
