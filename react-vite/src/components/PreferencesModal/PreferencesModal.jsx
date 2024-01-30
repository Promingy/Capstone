import { useSelector } from 'react-redux'
import './PreferencesModal.css'
import { useState } from 'react'
import { useNavigate } from 'react-router-dom'

function PreferencesModal({ close }) {
    const user = useSelector(state => state.session.user)
    const [iconGlow, setIconGlow] = useState(false)
    const [iconGlow2, setIconGlow2] = useState(false)
    const navigate = useNavigate()


    return (
        <>
        <div className={close ? 'background_color_pref2': 'background_color_pref'} id='background_color_pref'/>
        <div className={close ? 'preferences_modal_container2':'preferences_modal_container'} id='preference_modal_container'>
            <div className='user_pref_header'>
                <div className='user_info'>
                    <img className='user_profile_pic' src={user?.profile_pic}/>
                    <p>{close ? 'hidden' : user.email}</p>
                </div>
                <div className='exit_pref'>
                    <i id='xmark' className='fa-solid fa-xmark fa-xl'/>
                </div>
            </div>

            <div className='create_recipe'
                id='create_recipe'
                onMouseOver={() => setIconGlow2(true)}
                onMouseLeave={() => setIconGlow2(false)}>
                Create a Recipe
                <i className={`fa-solid fa-chevron-right no_glow ${iconGlow2 && 'enter_icons'}`}/>
            </div>
            <div className='your_recipes'
                id='your_recipes'
                onMouseOver={() => {setIconGlow(true)}}
                onMouseLeave={() => {setIconGlow(false)}}>
                Your Recipes
                <i className={`fa-solid fa-chevron-right no_glow ${iconGlow && "enter_icons"}`}/>
            </div>

            <div className='logout_button'>
                <p id='logout_button' className='logout_button'>Logout</p>
            </div>
            <div className='preference-links-wrapper'>
                <h3 className='preference-links-header'>Links</h3>
                <div className='preference-links'>
                    <div className='links-left'>
                        <a className='preference-link' href='https://promingy.github.io/'>
                            <i className='fa-solid fa-address-card'/> Portfolio
                        </a>
                        <a className='preference-link' href='https://www.linkedin.com/in/corbin-ainsworth-18a885232/'>
                            <i className='fa-brands fa-linkedin'/> LinkedIn
                        </a>
                        <a className='preference-link' href='https://github.com/Promingy'>
                            <i className='fa-brands fa-github'/> Github
                        </a>
                    </div>
                    <div className='links-right'>
                        <a className='preference-link' onClick={() => navigate('/about-me')}>
                            <i className='fa-solid fa-user'/> About
                        </a>
                        <a className='preference-link' onClick={() => navigate('/contact-me')}>
                            <i className='fa-solid fa-envelope'/> Contact
                        </a>

                    </div>
                </div>
            </div>
        </div>
        </>
    )
}

export default PreferencesModal
