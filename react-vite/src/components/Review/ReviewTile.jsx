import { useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import ConfirmDelete from "../ConfirmDelete"
import OpenModalButton from "../OpenModalButton/OpenModalButton"

export default function ReviewTile({ review }) {
    const [bounceLike, setBounceLike] = useState(false)
    const sessionUser = useSelector(state => state.session.user)


    return (
        <div className="review" onMouseOver={() => setBounceLike(true)} onMouseLeave={() => setBounceLike(false)}>
            <h3>{review.name}</h3>
            <div className="review_body">
                <p>{review.body}</p>
                { review.user_id == sessionUser.id &&
                    <div className="review_owner_icons">
                        <span>
                            <i className="fa-regular fa-pen-to-square fa-lg" />
                        </span>
                        <span className="delete_review_modal">
                            <OpenModalButton
                            buttonText={<span className="fa-regular fa-trash-can fa-xl"/>}
                            modalComponent={<ConfirmDelete review={review} />}
                            />
                        </span>
                    </div>
                }
            </div>
            <div className="is_this_helpful_container">
                <span className="is_this_helpful_text">Is this helpful?</span>
                <i className={`fa-regular fa-thumbs-up ${bounceLike && 'fa-bounce'}`}/>
            </div>
        </div>
    )
}

{/* <span className='delete_recipe_icon'>
    <OpenModalButton
        buttonText={<span
            id='delete_recipe'
            className='fa-regular fa-trash-can fa-xl delete_recipe'
            onClick={() => setConfirmDelete(!confirmDelete)}
        />}
        modalComponent={<ConfirmDelete recipe={recipe} />}
    />
</span> */}
