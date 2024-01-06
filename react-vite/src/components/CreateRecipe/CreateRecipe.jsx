import { useEffect, useState } from "react"
import "./CreateRecipe.css"
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetDropdowns } from "../../redux/dropdown"
import { useNavigate } from "react-router-dom"
import TextareaAutoSize from 'react-textarea-autosize'

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
    const [description, setDescription] = useState('')
    const [servings, setServings] = useState(0)
    const [step, setStep] = useState('')
    const [steps, setSteps] = useState({})
    const [stepNumber, setStepNumber] = useState(1)

    useEffect(() => {
        dispatch(thunkGetDropdowns())
    }, [dispatch])

    function handleSubmit(e) {
        e.preventDefault()
    }

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
                    <div className="description_container">
                        <TextareaAutoSize
                        className='create_description'
                        placeholder="Description"
                        value={description}
                        onChange={e => setDescription(e.target.value)}
                        />
                        <span> {description.length} / 2000</span>
                    </div>
                </label>

                <label>
                    <input
                        type='number'
                        placeholder="Servings"
                        min={1}
                        value={servings || ''}
                        onChange={e => setServings(e.target.value)}
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
                                <div key={`ingredient${ingredients.ingredient}${ingredients.quantity}`}>
                                    {ingredient.ingredient}
                                    <div className="remove_ingredient" onClick={() => {
                                            const newIngredient = {...ingredients}
                                            delete newIngredient[ingredient.ingredient]
                                            setIngredients(newIngredient)
                                        }}>
                                        <i className="fa-solid fa-x fa-xs" />
                                    </div>
                                </div>
                            )
                        })}

                    </div>

                <label className="add_ingredients_container">
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
                        placeholder="Quantity"
                        value={quantity || ''}
                        min={1}
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

                        <div className="add_ingredient">
                            <i className="fa-solid fa-plus" />
                        </div>

                    </div>
                </label>

                <label>
                    <div className="steps_container">
                        <div className="added_steps">
                            {Object.keys(steps).map(key => {
                                const step = steps[key]
                                return (
                                <div key={`steps${step.stepNumber}`} className="steps_and_remove">
                                    {step.stepNumber} {step.step}
                                    <div className="remove_ingredient" onClick={() => {
                                            const newSteps = {...steps}
                                            delete newSteps[step.stepNumber]
                                            setSteps(newSteps)
                                        }}>
                                        <i className="fa-solid fa-x fa-xs" />
                                    </div>
                                </div>
                                )
                            })}
                        </div>
                    </div>

                    <div className="step_and_add">
                        <label>
                            <input
                                type="number"
                                placeholder="Step"
                                value={stepNumber}
                                onChange={e => setStepNumber(e.target.value)}
                                min={1}
                                />
                        </label>
                        <div className="add_step_text_container">
                            <TextareaAutoSize
                                className="add_step_text_area"
                                placeholder="Add Step"
                                value={step}
                                onChange={e => setStep(e.target.value)}
                            />
                            {step.length} / 2000
                        </div>
                        <div className='add_ingredient' onClick={() => {
                            // add step to steps obj
                            if (!step) return

                            let newStepNum = stepNumber
                            let test = 1

                            while (steps[newStepNum - 1] == undefined && newStepNum !== 1){
                                newStepNum -= 1
                            }

                            const newStep = {newStepNum, step}

                            setSteps({...steps, [newStepNum]: newStep})

                            // reset step values
                            setStep('')
                            setStepNumber(newStepNum + 1)
                        }}>

                        <div className="add_ingredient">
                            <i className="fa-solid fa-plus" />
                        </div>

                    </div>

                    </div>
                </label>

                <label>
                        <span>Prep time:</span>
                        <input
                            type='number'
                            placeholder="Hours"
                            min={0}
                            />
                        <input
                            type='number'
                            placeholder="Minutes"
                            min={0}
                            max={60}
                            />
                </label>

                <label>
                        <span>Cook time:</span>
                        <input
                            type='number'
                            placeholder="Hours"
                            min={0}/>
                        <input
                            type='number'
                            placeholder="Minutes"
                            max={60}
                            min={0}/>
                </label>

                <button>Submit</button>
            </form>
        </div>
    )
}
