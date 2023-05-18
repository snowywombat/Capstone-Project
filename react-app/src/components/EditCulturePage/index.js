import React from "react";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams, useLocation } from "react-router-dom";
import { thunkEditCulture, thunkGetSingleCulture } from "../../store/culture";

function EditCulturePage() {

    const dispatch = useDispatch();
    const history = useHistory();
    const location = useLocation();
    const article = location.state.article;

    const [title, setTitle] = useState(article.title);
    const [description, setDescription] = useState(article.description);
    const [banner_img, setBannerImg] = useState(article.banner_img);
    const [editArticle, setEditArticle] = useState(article.article);
    const [errors, setErrors] = useState([]);

    const handleSubmit = async (e) => {
      e.preventDefault();
      setErrors([]);

      const body = {
        title: title,
        description: description,
        banner_img: banner_img,
        article: editArticle,
      };

      try {
        const data = await dispatch(thunkEditCulture(body, article.id));
        history.push(`/culture/${data.id}`);
      } catch (e) {
        const errorResponse = e.errors;
        const errorMessages = errorResponse.map((error) => error.split(': ')[1]);
        setErrors(errorMessages);
      }
    };

    return (
        <div className="Global-Modal-Container3">
      <div className="Global-Modal-Header">Edit your article</div>
      <div className="Global-Modal-Description">Edit the form below to share your article!</div>
      <form onSubmit={handleSubmit} className="Global-ModalForm-Container">
        <ul>
					{errors.map((error, idx) => (
						<li className='errors-div' key={idx}>{error}</li>
					))}
				</ul>

        <label className='form-labels'>Title of your article:</label>
        <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            required
            placeholder=""
            className="Global-Modal-input"
        />


        <label className='form-labels form-lables-exclude-first'>Add a description:</label>
        <textarea
            rows="3"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            required
            placeholder=""
            className="Global-Modal-input"
        />


        <label className='form-labels form-lables-exclude-first'>Banner Image:</label>
        <input
            type="text"
            value={banner_img}
            onChange={(e) => setBannerImg(e.target.value)}
            required
            placeholder=""
            className="Global-Modal-input"
        />

        <label className='form-labels form-lables-exclude-first'>Your Article:</label>
        <textarea
            value={editArticle}
            onChange={(e) => setEditArticle(e.target.value)}
            required
            placeholder=""
            className="Global-Modal-input"
        />



        <button type="submit" className="Global-SubmitButton">
          Edit Article
        </button>

        <ul className='errors-bottom'>
					{errors.map((error, idx) => (
						<li className='errors-div' key={idx}>{error}</li>
					))}
				</ul>

      </form>
    </div>
  );


}
export default EditCulturePage;
