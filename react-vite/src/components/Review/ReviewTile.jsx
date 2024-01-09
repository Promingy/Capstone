import { useState } from "react"

export default function ReviewTile({ review }) {
    const [bounceLike, setBounceLike] = useState(false)

    return (
        <div className="review" onMouseOver={() => setBounceLike(true)} onMouseLeave={() => setBounceLike(false)}>
            <h3>{review.name}</h3>
            <p>{review.body}</p>
            <div className="is_this_helpful_container">
                <span className="is_this_helpful_text">Is this helpful?</span>
                <i className={`fa-regular fa-thumbs-up ${bounceLike && 'fa-bounce'}`}/>
            </div>
        </div>
    )
}
