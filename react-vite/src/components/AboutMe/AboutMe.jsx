import { useEffect, useState } from "react"
import "./AboutMe.css"
import { useNavigate } from "react-router-dom"

export default function AboutMe() {
    const navigate = useNavigate()
    const [seeMore, setSeeMore] = useState(false)

    useEffect(() => {
        window.scrollTo(0,0)
    }, [])

    return (
        <div className="about-me">
            <div className="about-me-left">
                <img className="about-me-pic" src='/profile.png' />
                <button
                    type='button'
                    className="contact-me-btn"
                    onClick={() => navigate('/contact-me')}
                    >
                        Contact Me
                </button>

            </div>
            <div className="about-me-right">
                {/* <h1>About Me</h1> */}
                <div className="about-me-body">
                    <h2 className="about-me-subheader">
                        I'm Corbin, a Software Engineer, Musician and language enthusiast in Denver, Colorado.
                    </h2>
                    <p>
                        I&apos;m a passionate learner and creative at heart, constantly seeking new challenges to fuel my growth. I welcome each opportunity and challenge with open arms, whether it&apos;s tackling complex problems or pushing creative boundaries. During my upbringing, which involved frequently relocating and during my time as professional content creator, I&apos;ve learned how to adapt and thrive in fast-changing environments. Let&apos;s connect and explore the exciting possibilities together! &ensp; &ensp; &ensp;{!seeMore ? <span className="see-more-less" onClick={() => setSeeMore(true)}>See More...</span> : <span className="see-more-less" onClick={() => setSeeMore(false)}>See Less...</span>}
                    </p>
                    {seeMore &&
                    <>
                        <p className="body-separator">⬇️ A bit more in depth ⬇️</p>
                        <p>
                            I&apos;m 25 and live in Denver, CO but am actually from Key West, FL... Kind of. I moved around a lot growing up, I was in 14 schools before graduating and Key West was where I had lived the longest, prior to CO. I was a content-creator from 14 - 21 and live-streaming professionally from 19-21. I made the grueling decision to put down content creation and move to CO after a falling-out with a previous romantic partner, which ultimately led to an overall career change for me.
                        </p>
                        <p>
                            When I first got to Colorado, I was fortunate enough to know some people that were willing to take me in as an apprentice for Welding and Metal Fabrication. Though, that was short lived due to the Covid pandemic going into full effect a few short months after I moved, which resulted in me being let go. This led me towards doing gig-work like Uber, Grubhub, Lyft, etc. Which has been my primary income for the last 3 1/2 years. This gig work provided me the opportunity to pay my bills amidst the pandemic but, also, more importantly the ability to reflect on what I wanted to pursue as a career path.
                        </p>
                        <p>
                            Throughout the latter half of 2022 I was working on my exit strategy from the gig industry and in April of 2023, there were some unsavory events that demonstrated that the dangers of picking up complete and total strangers are still very real, even on platforms like Uber and Lyft. These events promptly caused me to escalate the rate of my exit plan. I started doing heavy research into different programming bootcamps and after much consideration I eventually came to the decision that AppAcademy was the best choice for me. I enrolled in late July 2023 and officially started classes at the beginning of August.
                        </p>
                        <p>
                            My time at AppAcademy has stretched me in ways that I didn&apos;t know possible, but has thus allowed me to come out on the other end with a newfound passion, set of skills, and a new hope for the future.
                        </p>
                    </>
                    }
                </div>
            </div>

            {/* <h2 className="section-header">My Skills</h2>
            <div className="technologies">
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-plain.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/jquery/jquery-plain-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-plain.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/npm/npm-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/express/express-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sequelize/sequelize-plain-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlalchemy/sqlalchemy-original.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-plain-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original-wordmark.svg" />
                <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original-wordmark.svg" />
            </div> */}

        </div>
    )
}
