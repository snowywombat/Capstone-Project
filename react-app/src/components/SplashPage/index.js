import SignupFormModal from "../SignupFormModal";
import LoginFormModal from "../LoginFormModal";
import DemoFormModal from "../DemoModal"
import "./SplashPage.css";
import OpenModalButtonSplashPage from "../OpenModalSplashPage";

const SplashPage = () => {


    return (
      <>
        <div className="SplashPage-Container">
          <div className="SplashPage-Image-Slides">
            <div className="pic" id="pic10" />
            <div className="pic" id="pic9" />
            <div className="pic" id="pic8" />
            <div className="pic" id="pic7" />
            <div className="pic" id="pic6" />
            <div className="pic" id="pic5" />
            <div className="pic" id="pic4" />
            <div className="pic" id="pic3" />
            <div className="pic" id="pic2" />
            <div className="pic" id="pic1" />
          </div>
          <div className="SplashPage-Body-Text">
            <h1>
              Sign in or create an account
            </h1>
            <div className = 'splashpage-buttons'>
              <button className='sign-up-button-splashpage'>
                <OpenModalButtonSplashPage
                  buttonText="SIGN UP"
                  modalComponent={<SignupFormModal
                  />}
                />
              </button>
              <button>
                <OpenModalButtonSplashPage
                  buttonText="LOG IN"
                  modalComponent={<LoginFormModal
                  />}
                />
              </button>
              <div className='or-divider'>
                <p>
                ––––––––––––– or –––––––––––––
                </p>
              </div>
              <button>
                <OpenModalButtonSplashPage
                  buttonText="TRY THE DEMO"
                  modalComponent={<DemoFormModal
                  />}
                />
              </button>
            </div>
          </div>
        </div>
      </>
    );
  };

  export default SplashPage;
