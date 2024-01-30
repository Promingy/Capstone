import { useNavigate } from 'react-router-dom'
import './Redirect.css'
import { useEffect, useState } from 'react'
export default function Redirect () {
    const navigate = useNavigate()
    const [timer, setTimer] = useState(10)

    // create a countdown timer that
    // redirects to the home page after 5 seconds
    useEffect(() => {
        const interval = setInterval(() => {
            setTimer((timer) => timer - 1)
        }, 1000)
        return () => clearInterval(interval)
    }, [])

    if (timer === 0) {
        navigate('/')
    }

    return (
        <div className='redirect'>
            <h1 className='redirect_title'>The resource you&apos;re looking for does not exist</h1>
            <p className='redirect_subtitle'>If you aren&apos;t redirected in {timer} seconds, click <a href='/' onClick={() => navigate('/')}>here</a> to return to the home page.
        </p>
        </div>
    )
}
