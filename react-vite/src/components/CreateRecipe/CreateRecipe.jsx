import { useEffect, useState } from "react"
import "./CreateRecipe.css"
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetDropdowns } from "../../redux/dropdown"
import { useNavigate } from "react-router-dom"

export default function CreateRecipe () {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const measurements = useSelector(state => state.dropdowns.measurements)
    const categories = useSelector(state => state.dropdowns.categories)
    const sessionUser = useSelector(state => state.session.user)
    const [category, setCategory] = useState('Category')
    const [measurement, setMeasurement] = useState('Measurement')
    const [ingredient, setIngredient] = useState('')
    const [quantity, setQuantity] = useState(0)
    const [ingredients, setIngredients] = useState({})
    const [title, setTitle] = useState('')


    useEffect(() => {
        dispatch(thunkGetDropdowns())
    }, [dispatch])

    console.log('ingredients', ingredients)

    if (!sessionUser) navigate('/')
    if (!measurements || !categories) return
    return(
        <div>
            <form className="new_recipe_form">
                <legend>Create new Recipe</legend>

                <label>
                    <input
                        type='text'
                        placeholder="Title"
                        value={title}
                        onChange={ e => setTitle(e.target.value)}
                    />
                </label>

                <label>
                    <select
                        value={category}
                        onChange={e => setCategory(e.target.value)}
                    >
                        <option disabled>Category</option>
                        {Object.values(categories).map(category => (
                            <option key={`dropdown_category${category.category}`}>
                                    {category.category}
                            </option>
                        ))}
                    </select>
                </label>

                    <div className="added_ingredients">
                        {Object.values(ingredients).map(ingredient => {
                            return (
                                <p key={`ingredient${ingredients.ingredient}${ingredients.quantity}`}>
                                    {ingredient.ingredient}
                                    <div className="remove_ingredient" onClick={() => {
                                                const newIngredient = {...ingredients}
                                                delete newIngredient[ingredient.ingredient]
                                                setIngredients(newIngredient)

                                        }}>
                                        <i className="fa-solid fa-x fa-xs" />
                                    </div>
                                </p>
                            )
                        })}

                    </div>

                <label className="add_ingredients">
                    <select
                        value={measurement}
                        onChange={e => setMeasurement(e.target.value)}
                    >
                        <option disabled>Measurement</option>

                        {Object.values(measurements).map(measurement => (
                            <option key={`dropdown_measurement${measurement.measurement_name}`}>
                                {measurement.measurement_name}
                            </option>
                        ))}
                    </select>

                    <input
                        type='text'
                        placeholder="Ingredients"
                        value={ingredient}
                        onChange={e => setIngredient(e.target.value)}
                    />

                    <input
                        type='number'
                        value={quantity}
                        onChange={e => setQuantity(e.target.value)}
                    />
                    <div className='add_ingredient' onClick={() => {
                            // add ingredient to ingredients obj
                            if (ingredient && quantity && measurement){
                                const newIngredient = { ingredient,
                                                        quantity,
                                                        measurement}
                                setIngredients({...ingredients, [ingredient]: newIngredient})
                                // reset ingredient values
                                setIngredient('')
                                setQuantity(0)
                                setMeasurement('Measurement')
                            }
                        }}>
                        <i className="fa-solid fa-plus" />

                    </div>
                </label>
            </form>
        </div>
    )
}
