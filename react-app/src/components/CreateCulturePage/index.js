import React from "react";
import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory, useParams } from "react-router-dom";
import { thunkCreateCulture, thunkGetSingleCulture } from "../../store/culture";

function CreateCulturePage() {

    const dispatch = useDispatch();
    const history = useHistory();

    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [banner_img, setBannerImg] = useState("");
    const [article, setArticle] = useState("");
    const [errors, setErrors] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setErrors([]);

        const body = {
          title,
          description,
          banner_img,
          article,
        };

        try {
          await dispatch(thunkCreateCulture(body))
          .then((data) => {
              // dispatch(thunkGetSingleCulture(data.id))
              history.push(`/culture/${data.id}`)
          })
        } catch (e) {
          const errorResponse = e.errors;
          const errorMessages = errorResponse.map((error) => error.split(": ")[1]);
          setErrors(errorMessages);
        }
    };

    return (
        <div className="Global-Modal-Container3">
      <div className="Global-Modal-Header">Add your own food pop culture article</div>
      <div className="Global-Modal-Description">Fill out the form below to share your article!</div>
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
            value={article}
            onChange={(e) => setArticle(e.target.value)}
            required
            placeholder=""
            className="Global-Modal-input"
        />



        <button type="submit" className="Global-SubmitButton">
          Add Article
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
export default CreateCulturePage;
