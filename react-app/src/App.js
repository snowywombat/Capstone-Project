import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Switch } from "react-router-dom";
import SignupFormPage from "./components/SignupFormPage";
import LoginFormPage from "./components/LoginFormPage";
import AllRecipesPage from "./components/AllRecipesPage/index.js";
import SingleRecipePage from "./components/SingleRecipePage";
import AllCulturePage from "./components/AllCulturePage";
import SingleCulturePage from "./components/SingleCulturePage";
import CreateCulturePage from "./components/CreateCulturePage";
import EditCulturePage from "./components/EditCulturePage";
import SplashPage from "./components/SplashPage";
import NotFoundPage from "./components/NotFoundPage";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />
      {isLoaded && (
        <Switch>
          {/* <Route path="/login" >
            <LoginFormPage />
          </Route>
          <Route path="/signup">
            <SignupFormPage />
          </Route> */}

          <Route exact path="/culture/create">
            <CreateCulturePage />
          </Route>

          <Route exact path="/culture/:cultureId/edit">
            <EditCulturePage />
          </Route>

          <Route exact path="/recipes/:recipeId">
            <SingleRecipePage />
          </Route>

          <Route exact path="/culture/:cultureId">
            <SingleCulturePage />
          </Route>

          <Route path="/recipes">
            <AllRecipesPage />
          </Route>

          <Route path="/culture">
            <AllCulturePage />
          </Route>

          <Route path="/" exact>
            <SplashPage />
          </Route>

          <Route path="*">
            <NotFoundPage />
          </Route>

        </Switch>
      )}
    </>
  );
}

export default App;
