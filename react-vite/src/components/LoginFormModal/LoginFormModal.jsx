import { useState } from "react";
import { thunkLogin } from "../../redux/session";
import { useDispatch } from "react-redux";
import { useModal } from "../../context/Modal";
import "./LoginForm.css";

function LoginFormModal() {
  const dispatch = useDispatch();
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errors, setErrors] = useState({});
  const { closeModal } = useModal();
  const [submitted, setSubmitted] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault();

    setSubmitted(true)

    const serverResponse = await dispatch(
      thunkLogin({
        email,
        password,
      })
    );

    if (serverResponse) {
      setErrors(serverResponse);
    } else {
      closeModal();
    }
  };

  return (
    <div className="login_form_container">
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
      </form>
    </div>
  );
}

export default LoginFormModal;
