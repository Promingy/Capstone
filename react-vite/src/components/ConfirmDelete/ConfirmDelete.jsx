import "./ConfirmDelete.css"
import { useModal } from "../../context/Modal"
import { useDispatch } from "react-redux";
import { thunkDeleteImage, thunkDeleteRecipe } from "../../redux/recipe";
import { thunkDeleteReview } from "../../redux/review";
import { useNavigate, useParams } from "react-router-dom";
export default function ConfirmDelete({ recipe, review }) {
    const { closeModal } = useModal();
    let { userId } = useParams()
    const navigate = useNavigate()
    const dispatch = useDispatch()

    async function handleDeleteRecipe(e){
        e.preventDefault()
        await dispatch(thunkDeleteImage(recipe.preview_image))
        const urlParts = userId.split(' ')

        await dispatch(thunkDeleteRecipe(recipe))
        .then(() => navigate(userId ? `${urlParts[0]} ${urlParts[1]} ${urlParts[2]}/recipes` : '/', {state: recipe.preview_image}))
        .then(closeModal)
    }

    async function handleDeleteReview(e) {
        e.preventDefault()


        dispatch(thunkDeleteReview(review))
        .then(closeModal)
    }

    return (
        <div className="confirm_delete_modal">
            <h2> Are you sure that you want to delete?</h2>
            <div className="confirm_delete_button_container">
                <button className="confirm_delete" onClick={review ? handleDeleteReview : handleDeleteRecipe}>Confirm Delete</button>
                <button className='cancel_delete' onClick={closeModal}>Cancel</button>
            </div>
        </div>
    )
}
