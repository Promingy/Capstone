import { useEffect, useState } from "react"
import "./CreateRecipe.css"
import { useDispatch, useSelector } from 'react-redux'
import { thunkGetDropdowns } from "../../redux/dropdown"
import { useNavigate } from "react-router-dom"
import TextareaAutoSize from 'react-textarea-autosize'
import { thunkCreateRecipe, thunkDeleteImage, thunkUpdateRecipe, thunkUploadImage } from "../../redux/recipe"

export default function CreateRecipe ({ prevForm, update }) {
    const dispatch = useDispatch()
    const navigate = useNavigate()
    const measurements = useSelector(state => state.dropdowns.measurements)
    const categories = useSelector(state => state.dropdowns.categories)
    const sessionUser = useSelector(state => state.session.user)
    const [category, setCategory] = useState( prevForm?.category || 0)
    const [measurement, setMeasurement] = useState('Measurement')
    const [ingredient, setIngredient] = useState('')
    const [quantity, setQuantity] = useState(1)
    const [ingredients, setIngredients] = useState(prevForm?.ingredients || {})
    const [delIngredients, setDelIngredients] = useState({})
    const [title, setTitle] = useState(prevForm?.title || '')
    const [description, setDescription] = useState( prevForm?.description || '')
    const [servings, setServings] = useState(prevForm?.servings || 1)
    const [step, setStep] = useState('')
    const [steps, setSteps] = useState(prevForm?.steps || {})
    const [delSteps, setDelSteps] = useState({})
    const [stepNumber, setStepNumber] = useState( prevForm?.steps && (Object.values(prevForm?.steps).length + 1).toFixed(1) || 1.0)
    const [prepTimeHours, setPrepTimeHours] = useState(Math.floor(prevForm?.prepTime / 60)|| 0)
    const [prepTimeMinutes, setPrepTimeMinutes] = useState(prevForm?.prepTime % 60|| 0)
    const [cookTimeHours, setCookTimeHours] = useState(Math.floor(prevForm?.cookTime / 60) || 0)
    const [cookTimeMinutes, setCookTimeMinutes] = useState(prevForm?.cookTime % 60|| 0)
    const [previewImage, setPreviewImage] = useState(prevForm?.previewImage || null)
    const [imageLoading, setImageLoading] = useState(false)
    const [submitted, setSubmitted] = useState(false)
    const [lastStepNum, setLastStepNum] = useState(Object.values(steps).length)
    const [countType, setCountType] = useState(true)
    const [tempImage, setTempImage] = useState(prevForm?.previewImage || null)

    const [errors, setErrors] = useState({})

    useEffect(() => {
        window.scrollTo(0, 0)
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

    function previewImageSetter(e) {
        e.stopPropagation();

        const tempFile = e.target.files[0]

        if (!tempFile) {
            setTempImage (prevForm?.previewImage || null)
            setPreviewImage (prevForm?.previewImage || null)
            return
        }

        // Check for max image size of 5mb
        if (tempFile?.size > 5000000) {
            return setErrors({preview_image_size: "Selected image exceeds the maximum file size of 5MB"})
        }

        const newImgURL = URL.createObjectURL(tempFile); //generate a local url to render the image
        setTempImage(newImgURL)
        setPreviewImage(tempFile)
    }
    async function handleSubmit(e) {
        e.preventDefault();

        if (description.length > 2000) return setErrors({description: ['Description must be 2000 characters or less']})

        setSubmitted(true);
        let returnImage;
        const formData = new FormData();
        formData.append("image", previewImage);

        if (!update){
            // aws uploads can be a bit slow-displaying
            // some sort of loading message is a good idea
            setImageLoading(true)
            returnImage = await dispatch(thunkUploadImage(formData))
        }else {
            if (prevForm?.previewImage != previewImage){
                setImageLoading(true)
                formData.append("image", previewImage)

                await dispatch(thunkDeleteImage(prevForm?.previewImage))

                returnImage = await dispatch(thunkUploadImage(formData))

        }
    }

        const newErrors = {};
        const newRecipe = {
            category_id: category,
            title,
            description,
            servings: +servings,
            prep_time: +prepTimeHours * 60 + +prepTimeMinutes,
            cook_time: +cookTimeHours * 60 + +cookTimeMinutes,
            preview_image: update? returnImage?.url || prevForm?.previewImage : returnImage.url,
            ingredients,
            steps,
            ingredientsToDelete: delIngredients,
            stepsToDelete: delSteps
        };

        updateStepNums();

        dispatch(update ? thunkUpdateRecipe(prevForm?.id, newRecipe) : thunkCreateRecipe(newRecipe))
        .then(res => {
            const data = res

            if (data.errors){
                for (let error in data.errors){
                    newErrors[error] = data.errors[error]
                    setSubmitted(false)
                    setImageLoading(false)
                }
                setErrors({...newErrors})
            }else {
                navigate(`/recipes/${res.id}-${res.title}`)
            }
        })
        .catch(() => {
            setSubmitted(false)
        })
    }

    useEffect(() => {
        window.scrollTo({top: 0, behavior: "smooth"})
    }, [errors])
    if (sessionUser?.id !== prevForm?.owner_id && prevForm || !sessionUser) navigate('/')
    if (!measurements || !categories) return

    return(
        <div className="new_recipe_form_container">
            <form className="new_recipe_form" onSubmit={handleSubmit} encType="multipart/form-data">

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
                    {errors.preview_image_size && <p className="errors">*{errors.preview_image_size}</p>}
                </div>

                <label className="recipe_title_container">
                    <div className="form_question_container">
                        <h2 className="form_question">What&apos;s the title of your recipe?</h2>
                        <p className="form_question_description">A short, descriptive name to quickly catch people attention.</p>
                    </div>
                    {/* <span>Title:</span> */}
                    <input
                        type='text'
                        placeholder="Title"
                        className = {`recipe_title ${errors.title ? 'error_container' : ''}`}
                        value={title}
                        onChange={ e => setTitle(e.target.value)}
                    />
                </label>

                <label className="recipe_description_container">
                    <div className="form_question_container">
                        <h2 className="form_question">A short description for your recipe.</h2>
                        <p className="form_question_description">Share with others what you love about this recipe.</p>
                    </div>
                    {/* <span>Description:</span> */}
                    <div className={`description_container ${errors.description ? "error_container" : ""}`}>
                        <TextareaAutoSize
                        className='create_description'
                        placeholder="Description"
                        value={description}
                        onChange={e => setDescription(e.target.value)}
                        />
                        <span className={description.length > 1800 ? description.length > 2000 ? 'at_limit' : 'approaching_limit' : 'within_limit'}> {description.length} / 2000</span>
                    </div>
                </label>

                <label className="recipe_servings_container">
                    <div className="form_question_container">
                        <h2 className="form_question">What type of food and how many servings does this recipe make?</h2>
                        <p className="form_question_description">Choose what time of food this is and how many servings this makes.</p>
                    </div>
                    <div className="servings_category_container">
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
                        <div className="custom_quantity custom_w_title">
                                <span className="custom_title">Servings:</span>
                                <div className="inner_input">
                                    <span className="custom_input_arrows_container" onClick={() => setServings(prevNum => prevNum + 1)}>
                                        <i className="fa-solid fa-caret-up"/>
                                    </span>
                                    <p className={`custom_input_text ${errors.servings && "error_container"}`}>{servings}</p>
                                    <span className="custom_input_arrows_container" onClick={() => setServings(prevNum => prevNum - 1 >= 1 ? prevNum - 1 : prevNum)}>
                                        <i className="fa-solid fa-caret-down"/>
                                    </span>

                                </div>
                            </div>
                    </div>
                </label>
                    <div className="form_question_container">
                        <h2 className="form_question">What ingredients are required to make this this recipe?</h2>
                        <p className="form_question_description">List all of the different ingredients that are needed to make this recipe.</p>
                    </div>
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

                                             if (update) {
                                                    setDelIngredients({...delIngredients, [ingredient.id]: ingredient})
                                             }

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
                        className={`${errors.ingredient && "error_container"}`}
                    />

                    <div className="custom_quantity">
                        <span className="custom_input_arrows_container" onClick={() => {
                                if (countType) {
                                    setQuantity(prevNum => prevNum + 1)
                                } else {
                                    setQuantity(prevNum => prevNum + .25)
                                }
                            }}>
                            <i className="fa-solid fa-caret-up"/>
                        </span>
                        <p className="custom_input_text">{quantity.toFixed(2)}</p>
                        <span className="custom_input_arrows_container" onClick={() => {
                            if (countType) {
                                setQuantity(prevNum => prevNum - 1 > 1 ? prevNum - 1 : 1)
                            } else {
                                setQuantity(prevNum => prevNum - .25 > 0.25 ? prevNum - .25 : 0.25)
                            }
                            }}>
                            <i className="fa-solid fa-caret-down"/>
                        </span>
                    </div>
                    <div className={`add_ingredient ${errors.ingredient && "error_container"}`} onClick={() => {
                            // add ingredient to ingredients obj
                            if (+quantity < 0) setQuantity(1)
                            if (ingredient && quantity && measurement != 'Measurement' && !ingredients[ingredient]){
                                const newIngredient = { ingredient,
                                                        ingredient_quantity: +quantity,
                                                        ingredient_measurement_id: measurements[measurement].id
                                                    }

                                setIngredients({...ingredients, [ingredient]: newIngredient})

                                // reset ingredient values
                                setIngredient('')
                                setQuantity(1)
                            }

                            else if (ingredients[ingredient]) {
                                const newIngredient = {...ingredients[ingredient]}

                                newIngredient.ingredient_quantity = +quantity
                                newIngredient.ingredient_measurement_id = measurements[measurement].id
                                newIngredient.ingredient = ingredient

                                setIngredients({...ingredients, [ingredient]: newIngredient})

                                // reset ingredient values
                                setIngredient('')
                                setQuantity(1)

                                }
                        }}>

                        <div>
                            <i className="fa-solid fa-plus" />
                        </div>

                    </div>
                </label>

                <label className="add_step_container">
                    <div className="form_question_container">
                        <h2 className="form_question">What steps are required to make this dish?</h2>
                        <p className="form_question_description">List all of the different steps to follow in order to successfully create this recipe.</p>
                    </div>
                    <div className="steps_container">
                        <div className="added_steps">
                            {Object.keys(steps).map(key => {
                                const step = steps[key]
                                return (
                                <div key={`steps${step.step_number}`} className="steps_and_remove">
                                    <div className="full_step">
                                        <p>
                                            Step {(+step.step_number).toFixed(0)}.
                                        </p>
                                        <p className="step_description">
                                            {step.description}
                                        </p>
                                    </div>
                                    <div className="remove_ingredient" onClick={() => {
                                            const newSteps = {...steps}
                                            delete newSteps[(+step.step_number).toFixed(1)]
                                            setLastStepNum(Object.values(steps).length - 1)

                                            if (+stepNumber === lastStepNum + 1){
                                                setStepNumber(+lastStepNum)
                                            }
                                            if (step.id) {
                                                setDelSteps({...delSteps, [step.id]: step})
                                            }
                                            
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
                            {/* Create custom number input element */}
                                <div className="step_custom">
                                    <span className="custom_input_arrows_container"
                                    // onClick runs logic to make sure that the number can only be incremented to the next step
                                    // example. if the last step was 2 then our new step can only be up step 3
                                        onClick={() => setStepNumber(prevNum => +prevNum + 1 <= +lastStepNum + 1 ?  +prevNum + 1 : lastStepNum + 1)}>
                                        <i className="fa-solid fa-caret-up custom_input_arrows"/>
                                    </span>
                                    <p className="custom_input_text">{(+stepNumber).toFixed(0)}</p>
                                    <span className="custom_input_arrows_container"
                                    // onClick runs logic to make sure that our decremented step never goes below 1
                                        onClick={() => setStepNumber(prevNum => +prevNum - 1 > 0 ? +prevNum - 1 : 1)}>
                                        <i className="fa-solid fa-caret-down custom_input_arrows"/>
                                    </span>
                                </div>
                        </label>
                        <div className={`add_step_text_container
                                        ${errors.step_description ? "error_container" : ""}
                                        ${step.length > 1800 ? step.length > 2000 ? 'at_limit' : 'approaching_limit' : 'within_limit'}`}>
                            <TextareaAutoSize
                                className="add_step_text_area"
                                placeholder="Add Step"
                                value={step}
                                onChange={e => setStep(e.target.value)}
                            />
                            {step.length} / 2000
                        </div>
                        <div className={`add_ingredient ${errors.step_description && "error_container"}`} onClick={() => {
                            // add step to steps obj
                            if (!step || step.length > 2000) return

                            const newStep = {step_number: stepNumber, description: step}

                            setSteps({...steps, [(+stepNumber).toFixed(1)]: newStep})
                            // reset step values
                            setStep('')
                            setStepNumber((+stepNumber + 1).toFixed(1))
                            setLastStepNum(Object.values(steps).length + 1)
                        }}>

                        <div>
                            <i className="fa-solid fa-plus" />
                        </div>

                    </div>

                    </div>
                </label>

                <label className="recipe_prep_container">
                    <div className="form_question_container">
                        <h2 className="form_question">How long is the prep-work for this dish?</h2>
                        <p className="form_question_description">Choose how long it the prep work for this dish is. (Hours OR minutes required.)</p>
                    </div>
                        {/* <span>Prep time:</span> */}
                        <div className="hours_minutes_container">
                            <div className="custom_quantity custom_w_title">
                                <span className="custom_title">Hours:</span>
                                <div className="inner_input">
                                    <span className="custom_input_arrows_container" onClick={() => setPrepTimeHours(prevNum => prevNum + 1)}>
                                        <i className="fa-solid fa-caret-up"/>
                                    </span>
                                    <p className={`custom_input_text ${errors.prep_time && "error_container"}`}>{prepTimeHours}</p>
                                    <span className="custom_input_arrows_container" onClick={() => setPrepTimeHours(prevNum => prevNum - 1 >= 0 ? prevNum - 1 : prevNum)}>
                                        <i className="fa-solid fa-caret-down"/>
                                    </span>

                                </div>
                            </div>
                            <div className="custom_quantity custom_w_title">
                                <span className="custom_title">Minutes:</span>
                                <div className="inner_input">
                                    <span className="custom_input_arrows_container" onClick={() => setPrepTimeMinutes(prevNum => prevNum + 1)}>
                                        <i className="fa-solid fa-caret-up"/>
                                    </span>
                                    <p className={`custom_input_text ${errors.prep_time && "error_container"}`}>{prepTimeMinutes}</p>
                                    <span className="custom_input_arrows_container" onClick={() => setPrepTimeMinutes(prevNum => prevNum - 1 >= 0 ? prevNum - 1 : prevNum)}>
                                        <i className="fa-solid fa-caret-down"/>
                                    </span>

                                </div>
                            </div>

                        </div>
                </label>

                <label className="recipe_prep_container">
                    <div className="form_question_container">
                        <h2 className="form_question">How long does this dish take to cook?</h2>
                        <p className="form_question_description">Choose how long it takes to cook this dish. (Hours OR minutes required.)</p>
                    </div>
                         {/* <span>Cook time:</span> */}
                         <div className="hours_minutes_container">
                            <div className="custom_quantity custom_w_title">
                                <span className="custom_title">Hours:</span>
                                <div className="inner_input">
                                    <span className="custom_input_arrows_container" onClick={() => setCookTimeHours(prevNum => prevNum + 1)}>
                                        <i className="fa-solid fa-caret-up"/>
                                    </span>
                                    <p className={`custom_input_text ${errors.cook_time && "error_container"}`}>{cookTimeHours}</p>
                                    <span className="custom_input_arrows_container" onClick={() => setCookTimeHours(prevNum => prevNum - 1 >= 0 ? prevNum - 1 : prevNum)}>
                                        <i className="fa-solid fa-caret-down"/>
                                    </span>

                                </div>
                            </div>
                            <div className="custom_quantity custom_w_title">
                                <span className="custom_title">Minutes:</span>
                                <div className="inner_input">
                                    <span className="custom_input_arrows_container" onClick={() => setCookTimeMinutes(prevNum => prevNum + 1)}>
                                        <i className="fa-solid fa-caret-up"/>
                                    </span>
                                    <p className={`custom_input_text ${errors.cook_time && "error_container"}`}>{cookTimeMinutes}</p>
                                    <span className="custom_input_arrows_container" onClick={() => setCookTimeMinutes(prevNum => prevNum - 1 >= 0 ? prevNum - 1 : prevNum)}>
                                        <i className="fa-solid fa-caret-down"/>
                                    </span>

                                </div>
                            </div>

                         </div>
                </label>

                <div className="preview_image_container">
                    {/* <span>Image:</span> */}
                    <div className="form_question_container">
                        <h2 className="form_question">Select a cover image for your recipe.</h2>
                        <p className="form_question_description">Choose an image to showcase your delicious recipe!</p>
                    </div>
                    <div className="file_content_container">
                        <div className="preview_image_wrapper">
                            <input
                                type='file'
                                className={`preview_image ${errors.preview_image || errors.preview_image_size ? "error_container" : ""}`}
                                accept='image/*'
                                onChange={previewImageSetter}
                            />
                        </div>
                        <p className="loading_text">{imageLoading && "Loading..."}</p>
                        <div className="temp_image_container">
                            <i className="fa-regular fa-plus fa-xl temp_image_icon"/>
                            {tempImage && <img className="temp_image" src={tempImage} />}
                        </div>

                    </div>
                </div>

                <button disabled={submitted} className="submit_recipe">Submit</button>
            </form>
        </div>
    )
}
