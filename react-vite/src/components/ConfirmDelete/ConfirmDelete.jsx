import "./ConfirmDelete.css"
import { useModal } from "../../context/Modal"
import { useDispatch } from "react-redux";
import { thunkDeleteRecipe } from "../../redux/recipe";
export default function ConfirmDelete({ recipe }) {
    const { closeModal } = useModal();
    const dispatch = useDispatch()

    function handleDelete(e){
        e.preventDefault()
        dispatch(thunkDeleteRecipe(recipe))
        .then(closeModal)
    }

    return (
        <div className="confirm_delete_modal">
            <h2> Are you sure that you want to delete?</h2>
            <div className="confirm_delete_button_container">
                <button className="confirm_delete" onClick={handleDelete}>Confirm Delete</button>
                <button className='cancel_delete' onClick={closeModal}>Cancel</button>
            </div>
        </div>
    )
}
