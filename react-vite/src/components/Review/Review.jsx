import './Review.css'

export default function Review ({ recipe }) {
    console.log(recipe)
    return (
        <div className='review_container'>
            <div className='review_left'>
                <h2 className='review_headers'>RATINGS</h2>
                <div className='ratings_container'>
                    <p className='fa-solid fa-star fa-xl ratings_star'/>
                    <div className='reviews_out_of_container'>
                        <h3 className='reviews_out_of'>{recipe.avg_rating} out of 5</h3>
                        <p className='reviews_out_of reviews_out_of_p'>{recipe.reviews.length} user ratings</p>
                    </div>
                </div>
                    <p>Your rating</p>
            </div>
            <div className='review_right'>
                <h2 className='review_headers'>COOKING NOTES</h2>
            </div>
        </div>
    )
}
