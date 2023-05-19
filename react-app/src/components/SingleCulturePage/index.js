import { useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory, Route } from "react-router-dom";
import { thunkGetSingleCulture, thunkDeleteCulture, thunkEditCulture} from "../../store/culture";
import EditCulturePage from "../EditCulturePage";
import './SingleCulturePage.css'

const SingleCulturePage = () => {
    const { cultureId } = useParams();
    const dispatch = useDispatch();
    const history = useHistory();

    const singleArticle = useSelector(state => state.cultures);
    const user = useSelector(state => state.session.user);

    useEffect(() => {
        dispatch(thunkGetSingleCulture(cultureId))
    }, [dispatch, cultureId]);


    if(!singleArticle) {
        return <div>Loading...</div>
    }

    const article = Object.values(singleArticle).find(el => el.id === Number(cultureId))

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

                        <div className='article-banner'>
                            <img src={article.banner_img}
                                alt={"image of " + article.description}
                                id='banner-img'>
                            </img>
                        </div>


                        <div key={article.id} className='article-info-container'>
                            <div className='article-info-container-name'>
                                {article.title}
                            </div>
                            <div className='article-info-container-author'>
                                By: {article.user && article.user.firstName} {article.user && article.user.lastName}
                            </div>
                            <div className='article-info-container-date'>
                                {formattedDate}
                            </div>
                        </div>


                        {user && article.user_id === user.id &&
                            <div className='article-buttons' key={article.id}>
                                <div>
                                    <button onClick={() => handleEdit(article.id)} type="submit" className='open-modal-button-edit'>
                                        Edit Article
                                    </button>
                                </div>

                                <div>
                                    <button onClick={() => handleClick(article.id)} type="submit" className='open-modal-button-delete'>
                                    Delete Article
                                    </button>
                                </div>
                            </div>
                        }



                        <div className = 'single-page-main'>
                            <div className='article-description'>
                                {article.description}
                            </div>

                            <div className='article-body'>
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
