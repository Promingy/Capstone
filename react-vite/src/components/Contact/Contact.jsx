import { useEffect, useState } from "react"
import './Contact.css'

export default function Contact() {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [message, setMessage] = useState('');

    useEffect(() => {
        window.scrollTo(0,0)
    }, [])

    return (
        <div className="contact-me-container">
            <h1 className="contact-me-header">Contact Me</h1>
            <p className="contact-me-subheader">
            Have a question or interested in my work? Feel free to reach out through the form below. I look forward to connecting and discussing how my skills and experience align with your organization's goals.
            </p>
            <div className="contact-me-wrapper">
                <form className="contact-me-form contact-form" onSubmit={(e) => onSubmit(e)}>

                    <div className="formcarry-block input-container">
                        <input type="text" value={name} onChange={(e) => setName(e.target.value)} id="name" required/>
                        <span className={name ? "input2" : "input1"}>Name</span>
                    </div>

                    <div className="formcarry-block input-container ">
                        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} id="email" required/>
                        <span className={email ? 'input2' : 'input1'}>Email</span>
                    </div>

                    <div className="formcarry-block input-container">
                        <textarea value={message} onChange={(e) => setMessage(e.target.value)} id="message" required />
                        <span className={message ? "input2" : "input1"}>Enter your message...</span>
                    </div>

                    <div className="formcarry-block">
                        <button className="submit-contact" type="submit">Send</button>
                    </div>
                </form>
                <div className="personal-info-container">
                        <ul className="personal-info-list">
                            <li className="personal-info-item">
                                <h3 className="fa-solid fa-home"/>
                                <span>
                                    8587 W Hampden Ave. <br />
                                    Denver, CO 80227 <br />
                                    United States
                                </span>
                            </li>
                            <li className="personal-info-item">
                                <h3 className="fa-solid fa-mobile-screen-button"/>
                                (305) 570-8392
                            </li>
                            <li className="personal-info-item">
                                <h3 className="fa-solid fa-envelope"/>
                                <a className="email" href="mailto:ainsworthcorbin@gmail.com">ainsworthcorbin@gmail.com</a>
                            </li>
                            <li className="personal-info-item">
                                <h3 className='fa-brands fa-linkedin'/>
                                <a className="linkedin" href="https://www.linkedin.com/in/corbin-ainsworth-18a885232/" target="_blank" rel="noreferrer">LinkedIn</a>
                            </li>
                        </ul>
                    </div>
            </div>
        </div>
    )
}
