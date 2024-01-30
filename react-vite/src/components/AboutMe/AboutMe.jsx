import { useState } from 'react'
import './AboutMe.css'

export default function AboutMe() {
    const [seeMore, setSeeMore] = useState(false)


    return (
        <div className="about-me">
            <h1>About Me</h1>
            <div className='about-me-body'>
                <p>
                    I'm a passionate learner and creative at heart, constantly seeking new challenges to fuel my growth. I welcome each opportunity and challenge with open arms, whether it's tackling complex problems or pushing creative boundaries. During my upbringing, which involved frequently relocating and during my time as professional content creator, I've learned how to adapt and thrive in fast-changing environments. Let's connect and explore the exciting possibilities together!
                </p>
                <p className='body-separator see-more-less' onClick={() => setSeeMore(!seeMore)}>
                    {!seeMore ?
                    <>
                    ⬇️ A bit more in depth ⬇️ <br/>
                    (click to expand)
                    </>
                    :
                    <>
                    ⬆️ A bit less in depth ⬆️ <br />
                    (click to collapse)
                    </>
                    }
                </p>
                {seeMore &&
                <>
                    <p>
                        I'm 25 and live in Denver, CO but am actually from Key West, FL... Kind of. I moved around a lot growing up, I was in 14 schools before graduating and Key West was where I had lived the longest, prior to CO. I was a content-creator from 14 - 21 and live-streaming professionally from 19-21. I made the grueling decision to put down content creation and move to CO after a falling-out with a previous romantic partner, which ultimately led to an overall career change for me.
                    </p>
                    <p>
                        When I first got to Colorado, I was fortunate enough to know some people that were willing to take me in as an apprentice for Welding and Metal Fabrication. Though, that was short lived due to the Covid pandemic going into full effect a few short months after I moved, which resulted in me being let go. This led me towards doing gig-work like Uber, Grubhub, Lyft, etc. Which has been my primary income for the last 3 1/2 years. This gig work provided me the opportunity to pay my bills amidst the pandemic but, also, more importantly the ability to reflect on what I wanted to pursue as a career path.
                    </p>
                    <p>
                        Throughout the latter half of 2022 I was working on my exit strategy from the gig industry and in April of 2023, there were some unsavory events that demonstrated that the dangers of picking up complete and total strangers are still very real, even on platforms like Uber and Lyft. These events promptly caused me to escalate the rate of my exit plan. I started doing heavy research into different programming bootcamps and after much consideration I eventually came to the decision that AppAcademy was the best choice for me. I enrolled in late July 2023 and officially started classes at the beginning of August.
                    </p>
                    <p>
                        My time at AppAcademy has stretched me in ways that I didn't know possible, but has thus allowed me to come out on the other end with a newfound passion, set of skills, and a new hope for the future.
                    </p>
                </>
                }
            </div>
        </div>
    )
}
