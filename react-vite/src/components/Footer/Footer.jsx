import './Footer.css'

export default function Footer() {

    return (
        <div className='footer_container'>
            <div className='footer_left'>
                <h4>About Me</h4>
                <p className='about_me'>With a recent foray into software engineering, I bring a fresh perspective shaped by my background as a professional content creator and musician. Amidst the challenges of the Covid pandemic, I seized the opportunity to self-learn Japanese, symbolizing my resilience and passion for embracing new skills.</p>
            </div>
            <div className='footer_right'>
                <div className='footer_right_content'>
                    <h4>Creator Github</h4>
                    <a className='github_link' href='https://github.com/Promingy' target="_blank" rel='noreferrer'>
                        <i className='fa-brands fa-github'/> Corbin
                    </a>
                    <a className='github_link' href='https://github.com/Promingy/Capstone' target='_blank' rel='noreferrer'>
                        <i className='fa-brands fa-git-alt'/> Corbin
                        Project Repo
                    </a>
                </div>
            </div>
        </div>
    )
}
