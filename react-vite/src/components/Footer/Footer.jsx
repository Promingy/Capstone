import './Footer.css'

export default function Footer() {

    return (
        <div className='footer_container'>
            <div className='footer_left'>
                <h3>About Me</h3>
                <p className='about_me'>With a recent foray into software engineering, I bring a fresh perspective shaped by my background as a professional content creator and musician. Amidst the challenges of the Covid pandemic, I seized the opportunity to self-learn Japanese, symbolizing my resilience and passion for embracing new skills.</p>
            </div>
            <div className='links-wrapper'>
                <div className='footer_center'>
                    <div className='footer_center_content'>
                        <h3 className='footer_center_header'>Contact</h3>
                        <a className='github_link' href="https://promingy.github.io/">
                            <i className='fa-solid fa-address-card'/> Portfolio
                        </a>
                        <a className='github_link' href="https://www.linkedin.com/in/corbin-ainsworth-18a885232/">
                            <i className='fa-brands fa-linkedin'/> LinkedIn
                        </a>
                        <a className='github_link' href="mailto:ainsworthcorbin@gmail.com">
                            <i className='fa-solid fa-envelope'/> ainsworthcorbin@gmail.com
                        </a>
                    </div>
                </div>
                <div className='footer_right'>
                    <div className='footer_right_content'>
                        <h3 className='footer-right-header'>Creator Github</h3>
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
        </div>
    )
}
