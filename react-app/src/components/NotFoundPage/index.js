import './NotFoundPage.css'

const NotFoundPage = () => {
    return (
        <>
            <h1>
                404 Not Found
            </h1>
            <div className="not-found-photo-container">
                <img src="https://images.pexels.com/photos/6898855/pexels-photo-6898855.jpeg?auto=compress&cs=tinysrgb&w=1600" alt='sad face drawn on egg' className='not-found-photo'/>
            </div>
        </>
    )
}

export default NotFoundPage;
