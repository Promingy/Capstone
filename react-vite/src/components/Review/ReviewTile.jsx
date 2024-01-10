import { useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import ConfirmDelete from "../ConfirmDelete"
import OpenModalButton from "../OpenModalButton/OpenModalButton"
import TextareaAutosize from "react-textarea-autosize"
import { thunkUpdateReview } from "../../redux/review"

export default function ReviewTile({ review }) {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)
    const [bounceLike, setBounceLike] = useState(false)
    const [isEditing, setIsEditing] = useState(false)
    const [body, setBody] = useState("")
    const [isPrivate, setIsPrivate] = useState(review.private || false)
    const sessionUserName =sessionUser &&
                            sessionUser.first_name[0].toUpperCase() +
                            sessionUser.first_name.slice(1) +
                            " " +
                            sessionUser.last_name[0].toUpperCase() +
                            sessionUser.last_name.slice(1)

    function handleReviewUpdate(e) {
        e.preventDefault()

        const updatedReview = {
            id: review.id,
            body,
            private: isPrivate,
            edited: true
        }

        dispatch(thunkUpdateReview(updatedReview))
    }

    return (
        <div className="review" onMouseOver={() => setBounceLike(true)} onMouseLeave={() => setBounceLike(false)}>
            <h3>{review.user_id == sessionUser?.id ? sessionUserName  : review.name}</h3>
            <div className="review_body_container">
                {!isEditing &&
                <div className="edited_body">
                    {review.edited && <span className="edited">(edited)</span>}
                    <p className="review_body">{review.body}</p>
                </div>
                }

                {isEditing &&
                    <div className="edit_review_box_container">
                        <TextareaAutosize
                        className="edit_review_box"
                            value={body}
                            onChange={e => setBody(e.target.value)}
                        />
                        <div className="edit_review_bottom">
                            <div className="edit_private_container">
                                <p className={isPrivate ? 'privacy_unselected' : 'privacy_selected'} onClick={() => setIsPrivate(false)}>Public</p>
                                <p className={isPrivate ? "privacy_selected" : "privacy_unselected"} onClick={() => setIsPrivate(true)}>Private</p>
                            </div>
                            <div>
                                <button className="submit_review submit_updated_review" onClick={handleReviewUpdate}>Submit</button>
                            </div>
                        </div>
                    </div>
                }

                { review.user_id == sessionUser?.id &&
                    <div className="review_owner_icons">
                        <span onClick={() => {
                            setBody(review.body)
                            setIsPrivate(review.private)
                            setIsEditing(!isEditing)
                            }}>
                            <i className={`fa-regular fa-${isEditing ? 'x' : 'pen-to-square'} fa-lg`} />
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
