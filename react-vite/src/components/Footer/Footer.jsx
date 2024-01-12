import './Footer.css'

export default function Footer() {

    return (
        <div className='footer_container'>
            <div className='footer_left'>
                <h4>About Me</h4>
                <p></p>
            </div>
            <div className='footer_right'>
                <h4>Creator Github</h4>
                <a className='github_link' href='https://github.com/Promingy' target="_blank" rel='noreferrer'>
                    <i className='fa-brands fa-github'/> Corbin
                </a>
                <a className='github_link' href='https://github.com/Promingy/Capstone' target='_blank' rel='noreferrer'>
                    Project Repo
                </a>
            </div>
        </div>
    )
}
