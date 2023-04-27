import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory, Route } from "react-router-dom";
import { thunkGetSingleCulture, thunkDeleteCulture, thunkEditCulture} from "../../store/culture";
import EditCulturePage from "../EditCulturePage";

const SingleCulturePage = () => {
    const { cultureId } = useParams();
    const dispatch = useDispatch();
    const history = useHistory();

    const singleArticle = useSelector(state => state.cultures);
    const user = useSelector(state => state.session.user);

    console.log(singleArticle, 'single')


    useEffect(() => {
        dispatch(thunkGetSingleCulture(cultureId))
    }, [dispatch, cultureId]);


    if(!singleArticle) {
        return <div>Loading...</div>
    }

    const article = Object.values(singleArticle).find(el => el.id === Number(cultureId))
    console.log(article, 'article')

    const dateObj = new Date(article?.createdAt);
    const formattedDate = dateObj.toLocaleDateString("en-US", {
        month: "long",
        day: "numeric",
        year: "numeric"
    });

    const handleEdit = (cultureId) => {
        dispatch(thunkGetSingleCulture(cultureId)).then(() => {
          const article = Object.values(singleArticle).find(el => el.id === Number(cultureId));
          history.push({
            pathname: `/culture/${cultureId}/edit`,
            state: { article }
          });
        });
    }

    const handleDelete = (cultureId) => {
        dispatch(thunkDeleteCulture(cultureId))
        .then(() => dispatch(thunkGetSingleCulture(cultureId)))
        .then(() => history.push('/culture'))
    }

    const handleClick = (cultureId) => {
        const confirmed = window.confirm("Are you sure you want to delete your article?");
        if (confirmed) {
            handleDelete(cultureId);
        }
    }

    return (
        <>
            {article && article.user && formattedDate && (
                <section className='details-page'>
                    <div className = 'details-main'>
                        <div className='delete-button'>
                            {user && article.user_id === user.id &&
                                <div key = {article.id}>
                                    <div>
                                        <button onClick={() => handleEdit(article.id)} type="submit" className='delete-review-button'>
                                            Edit Article
                                        </button>
                                    </div>

                                    <div className='delete-review-button-div'>
                                        <button onClick={() => handleClick(article.id)} type="submit" className='delete-review-button'>
                                        Delete Article
                                        </button>
                                    </div>
                                </div>
                            }
                        </div>
                        <div className = 'details-header'>
                            <div key={article.id} className='recipe-info-container'>
                                <div className='recipe-info-container-name'>
                                    {article.title}
                                </div>
                                <div className='recipe-info-container-author'>
                                    By: {article.user && article.user.firstName} {article.user && article.user.lastName}
                                </div>
                                <div className='recipe-info-container-date'>
                                    {formattedDate}
                                </div>
                            </div>
                            <div className='photo-container'>
                                <img src={article.banner_img}
                                    alt={"image of " + article.description}
                                    id='bannerImg'>
                                </img>
                            </div>
                        </div>

                        <div className = 'single-page-main'>
                            <div className='recipe-description'>
                                {article.description}
                            </div>

                            <div>
                                {article.article}
                            </div>
                        </div>
                    </div>

                </section>
            )}
        </>
    )

}

export default SingleCulturePage;
