import { useDispatch, useSelector } from 'react-redux'
import './PreferencesModal.css'
import { useEffect } from 'react'

function PreferencesModal() {
    const user = useSelector(state => state.session.user)

    return (
        <>
        <div className='background_color_pref'/>
        <div className='preferences_modal_container'>
            <div className='user_pref_header'>
                <p>{user.email}</p>
                <i onClick={() => set} className='fa-solid fa-xmark fa-xl'/>
            </div>
        </div>
        </>
    )
}

export default PreferencesModal
