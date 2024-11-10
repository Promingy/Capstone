import { useEffect } from "react"

export default function PopupHandler() {

    useEffect(() => {
        if (window.opener) {
            window.opener.postMessage('oauth-success', '*')
            window.close()
        } 
    }, [])

    return (
        <div>Loading...</div>
    )
}