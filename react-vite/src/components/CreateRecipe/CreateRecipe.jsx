import { useEffect, useState } from "react"
import "./CreateRecipe.css"
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetDropdowns } from "../../redux/dropdown"
import { useNavigate } from "react-router-dom"
import TextareaAutoSize from 'react-textarea-autosize'
import { thunkCreateRecipe, thunkUpdateRecipe } from "../../redux/recipe"

export default function CreateRecipe ({ prevForm, update }) {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const measurements = useSelector(state => state.dropdowns.measurements)
    const categories = useSelector(state => state.dropdowns.categories)
    const sessionUser = useSelector(state => state.session.user)
    const [category, setCategory] = useState( prevForm?.category || 0)
    const [measurement, setMeasurement] = useState('Measurement')
    const [ingredient, setIngredient] = useState('')
    const [quantity, setQuantity] = useState(0)
    const [ingredients, setIngredients] = useState(prevForm?.ingredients || {})
    const [title, setTitle] = useState(prevForm?.title || '')
    const [description, setDescription] = useState( prevForm?.description || '')
    const [servings, setServings] = useState(prevForm?.servings || 0)
    const [step, setStep] = useState('')
    const [steps, setSteps] = useState(prevForm?.steps || {})
    const [stepNumber, setStepNumber] = useState( prevForm?.steps && Object.values(prevForm?.steps).length + 1 || 1)
    const [prepTimeHours, setPrepTimeHours] = useState(Math.floor(prevForm?.prepTime / 60)|| 0)
    const [prepTimeMinutes, setPrepTimeMinutes] = useState(prevForm?.prepTime % 60|| 0)
    const [cookTimeHours, setCookTimeHours] = useState(Math.floor(prevForm?.cookTime / 60) || 0)
    const [cookTimeMinutes, setCookTimeMinutes] = useState(prevForm?.cookTime % 60|| 0)
    const [previewImage, setPreviewImage] = useState(prevForm?.previewImage || '')
    const [submitted, setSubmitted] = useState(false)

    const [errors, setErrors] = useState({})

    useEffect(() => {
        dispatch(thunkGetDropdowns())
    }, [dispatch])

    function updateStepNums() {
        const newSteps = Object.values(steps)
        const returnSteps = {}

        for (let i = 0; i < newSteps.length; i++) {
            let currStep = newSteps[i]
            currStep.stepNumber = i + 1
            returnSteps[currStep.stepNumber] = currStep
        }

        setSteps(returnSteps)
    }

    function handleSubmit(e) {
        e.preventDefault()
        setSubmitted(true)

        const newErrors = {}

        const newRecipe = {
            category_id: category,
            title,
            description,
            servings: +servings,
            prep_time: +prepTimeHours * 60 + +prepTimeMinutes,
            cook_time: +cookTimeHours * 60 + +cookTimeMinutes,
            preview_image: previewImage,
            ingredients,
            steps
        }

        updateStepNums()

        dispatch(update ? thunkUpdateRecipe(prevForm?.id, newRecipe) : thunkCreateRecipe(newRecipe))
        .then(res => {
            const data = res

            if (data.errors){
                console.log(data.errors)
                for (let error in data.errors){
                    newErrors[error] = data.errors[error]
                    setSubmitted(false)
                }
                setErrors({...newErrors})
            }else {
                navigate(`/recipes/${res.id}-${res.title}`)
            }
        })

    }

    console.log(prevForm)
    if (!sessionUser) navigate('/')
    if (!measurements || !categories) return

    return(
        <div>
            <form className="new_recipe_form" onSubmit={handleSubmit}>

                <div className="error_spacer top_error">
                    {errors.title && <p className="errors">* Please include a Title</p>}
                    {errors.description && <p className="errors">* Please include a Description</p>}
                    {errors.servings && <p className="errors">* Please include serving size</p>}
                    {errors.category_id && <p className="errors">* Please select a category</p>}
                    {errors.ingredient && <p className="errors">* Please include at least 1 ingredient</p>}
                    {errors.step_description && <p className='errors'>* Please include at least 1 step.</p>}
                    {errors.prep_time && <p className="errors">* Please include the prep time</p>}
                    {errors.cook_time && <p className="errors">* Please include the cook time</p>}
                    {errors.preview_image && <p className="errors">* Please include a preview image</p>}
                </div>

                <label className="recipe_title_container">
                    <span>Title:</span>
                    <input
                        type='text'
                        placeholder="Title"
                        className = {`recipe_title ${errors.title ? 'error_container' : ''}`}
                        value={title}
                        onChange={ e => setTitle(e.target.value)}
                    />
                </label>

                <label className="recipe_description_container">
                    <span>Description:</span>
                    <div className={`description_container ${errors.description ? "error_container" : ""}`}>
                        <TextareaAutoSize
                        className='create_description'
                        placeholder="Description"
                        value={description}
                        onChange={e => setDescription(e.target.value)}
                        />
                        <span> {description.length} / 2000</span>
                    </div>
                </label>

                <label className="recipe_servings_container">
                    <span>Servings:</span>
                    <input
                        type='number'
                        placeholder="Servings"
                        className={`recipe_servings ${errors.servings ? "error_container" : ""}`}
                        min={1}
                        value={servings || ''}
                        onChange={e => setServings(+e.target.value > 1 ? +e.target.value : 1)}
                    />
                </label>
                    <div className="added_ingredients">
                        {Object.values(ingredients).map(ingredient => {
                            let measurement_name = measurements[ingredient.ingredient_measurement_id].measurement_name
                            measurement_name = +ingredient.ingredient_quantity > 1 ?  measurement_name + 's' : measurement_name

                            return (
                                <div key={`ingredient${ingredient.ingredient}${ingredient.quantity}`} className="ingredient_container">

                                    <div className="ingredient_measurement">
                                        <p className="ingredient_amount">
                                            {ingredient.ingredient_quantity} {measurement_name}:
                                        </p>
                                        <p className="ingredient">{ingredient.ingredient}</p>
                                    </div>
                                     <div className="remove_ingredient" onClick={() => {
                                             const newIngredient = {...ingredients}
                                             delete newIngredient[ingredient[update ? 'id' : 'ingredient']]
                                             delete newIngredient?.[ingredient?.ingredient]
                                             setIngredients(newIngredient)
                                         }}>
                                         <i className="fa-solid fa-x fa-xs" />
                                     </div>
                                </div>
                            )
                        })}
                    </div>
                <label className="recipe_category_ingredient_container">

                    <select
                        value={categories[category]?.category || 'Category'}
                        onChange={e => setCategory(e.target.selectedIndex)}
                        className={errors.category_id ? "error_container" : ""}
                    >
                        <option disabled>Category</option>
                        {Object.keys(categories).map(key => (
                            <option key={`dropdown_category${categories?.[key]?.id}`} id={`category_${categories?.[key]?.id}`}>
                                    {categories[key].category}
                            </option>
                        ))}
                    </select>
                {/* </label> */}

                {/* <label className="add_ingredients_container"> */}
                    <select
                        className={`measurement_select ${errors.ingredient ? "error_container" : ""}`}
                        value={measurements[measurement]?.measurement_name || 'Measurement'}
                        onChange={e => setMeasurement(e.target.selectedIndex)}
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
                        className={`${errors.ingredient ? "error_container" : ''}`}
                    />

                    <input
                        type='number'
                        placeholder="Quantity"
                        value={quantity || ''}
                        min={1}
                        onChange={e => setQuantity(e.target.value)}
                        className={`${errors.ingredient ? "error_container" : ''}`}
                    />
                    <div className='add_ingredient' onClick={() => {
                            // add ingredient to ingredients obj
                            if (+quantity < 0) setQuantity(1)
                            if (ingredient && quantity && measurement != 'Measurement'){
                                const newIngredient = { ingredient,
                                                        ingredient_quantity: +quantity,
                                                        ingredient_measurement_id: measurements[measurement].id}

                                setIngredients({...ingredients, [ingredient]: newIngredient})

                                // reset ingredient values
                                setIngredient('')
                                setQuantity(0)
                                // setMeasurement('Measurement')
                            }
                        }}>

                        <div className="add_ingredient">
                            <i className="fa-solid fa-plus" />
                        </div>

                    </div>
                </label>

                <label className="add_step_container">
                    <div className="steps_container">
                        <div className="added_steps">
                            {Object.keys(steps).map(key => {
                                const step = steps[key]
                                return (
                                <div key={`steps${step.step_number}`} className="steps_and_remove">
                                    <div className="full_step">
                                        <p>
                                            Step {step.step_number}.
                                        </p>
                                        <p className="step_description">
                                            {step.description}
                                        </p>
                                    </div>
                                    <div className="remove_ingredient" onClick={() => {
                                            const newSteps = {...steps}
                                            delete newSteps[step.step_number]
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
                                max={Object.values(steps).length + 1}
                                />
                        </label>
                        <div className={`add_step_text_container ${errors.step_description ? "error_container" : ""}`}>
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

                            let newStepNum = +stepNumber >= 1 ? +stepNumber : 1

                            while (steps[+newStepNum - 1] == undefined && +newStepNum !== 1){
                                newStepNum -= 1

                                if (newStepNum < 1) break
                            }

                            const newStep = {step_number: newStepNum, description: step}
                            setSteps({...steps, [newStepNum]: newStep})
                            // reset step values
                            setStep('')
                            setStepNumber(+newStepNum + 1)
                        }}>

                        <div className="add_ingredient">
                            <i className="fa-solid fa-plus" />
                        </div>

                    </div>

                    </div>
                </label>

                <label className="recipe_prep_container">
                        <span>Prep time:</span>
                        <div className="time_format">
                            <span>Hours:</span>
                            <input
                                className={`${errors.prep_time ? "error_container": ""}`}
                                type='number'
                                placeholder="Hours"
                                min={0}
                                value={prepTimeHours}
                                onChange={e => setPrepTimeHours(e.target.value)}
                                />
                        </div>
                        <div className="time_format">
                            <span>Minutes:</span>
                            <input
                                className={`${errors.prep_time ? "error_container": ""}`}
                                type='number'
                                placeholder="Minutes"
                                min={0}
                                max={60}
                                value={prepTimeMinutes}
                                onChange={e => setPrepTimeMinutes(e.target.value)}
                                />
                        </div>
                </label>

                <label className="recipe_cook_container">
                        <span>Cook time:</span>
                        <div className="time_format">
                            <span>Hours:</span>
                            <input
                                className={`${errors.cook_time ? "error_container": ""}`}
                                type='number'
                                placeholder="Hours"
                                min={0}
                                value={cookTimeHours}
                                onChange={e => setCookTimeHours(e.target.value)}
                                />
                        </div>
                        <div className="time_format">
                            <span>Minutes:</span>
                            <input
                                className={`${errors.cook_time ? "error_container": ""}`}
                                type='number'
                                placeholder="Minutes"
                                max={60}
                                min={0}
                                value={cookTimeMinutes}
                                onChange={e => setCookTimeMinutes(e.target.value)}
                                />
                        </div>
                </label>

                <label className="preview_image_container">
                    <span>Image:</span>
                    <input
                        type='url'
                        placeholder="Image"
                        className={`preview_image ${errors.preview_image ? "error_container" : ""}`}
                        value={previewImage}
                        onChange={e => setPreviewImage(e.target.value)}
                    />
                </label>

                <button disabled={submitted} className="submit_recipe">Submit</button>
            </form>
        </div>
    )
}
