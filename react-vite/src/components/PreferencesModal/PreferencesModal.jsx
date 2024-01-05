import { useSelector } from 'react-redux'
import './PreferencesModal.css'
import { useNavigate } from 'react-router-dom'

function PreferencesModal({ close }) {
    const user = useSelector(state => state.session.user)
    const navigate = useNavigate()

    return (
        <>
        <div className={close ? 'background_color_pref2': 'background_color_pref'} id='background_color_pref'/>
        <div className={close ? 'preferences_modal_container2':'preferences_modal_container'} id='preference_modal_container'>
            <div className='user_pref_header'>
                <p>{close ? 'hidden' : user.email}</p>
                <div className='exit_pref'>
                    <i id='xmark' className='fa-solid fa-xmark fa-xl'/>
                </div>
            </div>

            <div className='create_recipe' id='create_recipe' onClick={() => navigate('/new-recipe')}>
                Create a Recipe
            </div>

            <div className='logout_button'>
                <p id='logout_button' className='logout_button'>Logout</p>
            </div>
        </div>
        </>
    )
}

export default PreferencesModal
