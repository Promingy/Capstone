import "./ConfirmDelete.css"
import { useModal } from "../../context/Modal"
import { useDispatch } from "react-redux";
import { thunkDeleteImage, thunkDeleteRecipe } from "../../redux/recipe";
import { thunkDeleteReview } from "../../redux/review";
import { useNavigate } from "react-router-dom";
export default function ConfirmDelete({ recipe, review }) {
    const { closeModal } = useModal();
    const navigate = useNavigate()
    const dispatch = useDispatch()

    async function handleDeleteRecipe(e){
        e.preventDefault()
        await dispatch(thunkDeleteImage(recipe.preview_image))

        await dispatch(thunkDeleteRecipe(recipe))
        .then(() => navigate('/'))
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
