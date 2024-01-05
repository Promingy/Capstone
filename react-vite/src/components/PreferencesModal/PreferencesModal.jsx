import { useSelector } from 'react-redux'
import './PreferencesModal.css'

function PreferencesModal({ close }) {
    const user = useSelector(state => state.session.user)

    return (
        <>
        <div className={close ? 'background_color_pref2': 'background_color_pref'} id='background_color_pref'/>
        <div className={close ? 'preferences_modal_container2':'preferences_modal_container'} id='preference_modal_container'>
            <div className='user_pref_header'>
                <p>{close ? '' : user.email}</p>
                <div className='exit_pref'>
                    <i id='xmark' className='fa-solid fa-xmark fa-xl'/>
                </div>
            </div>
            <div className='logout_button'>
                <p id='logout_button' className='logout_button'>Logout</p>
            </div>
        </div>
        </>
    )
}

export default PreferencesModal
