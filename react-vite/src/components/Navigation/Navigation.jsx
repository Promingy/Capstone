import {  useNavigate } from "react-router-dom";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";

function Navigation() {
  const navigate = useNavigate()
  return (
    <div className="nav_bar">
      <div className="header_top_container">
        <img className="logo_image" onClick={() => navigate('/')} src="https://recipe-rendezvous.s3.us-west-2.amazonaws.com/recipe-rendezvous-high-resolution-logo-transparent%20%281%29.png?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLWVhc3QtMiJGMEQCIGkYTyGXMdWsvuA4L%2BXzzMu1iO7NJY52PzdOrpJXr3SBAiBYO9PNf%2B%2F1MHFy3hzb5lfyvicd2NrMVZBSo5NIy3AK4SrkAgghEAAaDDU1MDM4MzYyNDAyMiIMH52Cw654RknS7ud3KsECL7HO7gkYzrAyS3dxLAaDPHMMB4%2Fthpib9%2F7kqKDXdww4SUAwBmkAgElitZEzcIgdYj2CMHTHKQcW2vQArAyLvvB9LIbarq8r%2BDZ31ERKx%2BlN7D9fUx52bdGE5raQ5M%2FV39X6QjVuFfDeaQwF12FrQFO7sGUA9leLctgG%2B2zf5qxuV5az0fpRxUEszyeDqYSYL0PZ97qXL5qAbhvrIJltLutrARWySHY%2BqcmMPH%2BPXvJkj3HLhzzfCnCpwxS%2B%2F8ntP2S8OVTzqpq2jRy7RGpnfaVOm0%2FHabQU%2BlCwaI3ZArMW4gFNGRVHeDuE50XTYl%2BJUwldai0sSvRJRFLud88vAQRu%2BRAbdFJoVbPHcMQtWlWwN1sfd7TxYnYdW4S6qGAPSyqx7hCzE%2Bm9zH%2F%2B20Q%2BTb9VIB0kcB%2Fntg%2FH4OE632ilMOXR%2FKwGOrQCsC%2BfDcE4CL%2FGvWK1iWzlZR4j4A%2FdDyqolX47orNMAI0sfxnasYMiHSiJA1RcLGSPhJ2auU0Jmo48jpSudpKMTOTWmIVPiokVfU74HbSzNdu4hpqfbX9f0XG2ulaolUEtwjKzkNFnY2ts5taMEq%2Ff8a7dsjZNNVjNRu8wD%2FMWIteTiIhP6Ld26ESsmnHJLfxIgEI5DCWeYFmQLLlWf7E4NZVWhTlJxFqLm47pBJSCQgT6GdMj2kGcwTYMZUK%2F2Q0bpojliDY%2BP6EvU4dZ9D1UKAzgObMDnY9nS%2BVRMBvMCFh5nJPoOyZ5PKvw8%2BDEGb78NfXAxYuYaDzksV%2FlYjBDMk%2BTcQ8jtUf0swwrpny5fnDwCMvuPpgqq303LYrbv1VgkOOznmBuiFgJF8q%2Ff%2Bp7xYB6RgU%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20240111T000149Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAYAJLLT5LKTVZEUVD%2F20240111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=6ba8207b15cbc67be548c4c0449d0dd578628a63a3e07fd0397f1e42c0b99a2a" />
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
