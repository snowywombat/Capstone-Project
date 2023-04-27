import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import sessionReducer from './session';
import recipeReducer from './recipes';
import reviewReducer from './reviews';
import tagReducer from './tags';
import cultureReducer from './culture';

const rootReducer = combineReducers({
  session: sessionReducer,
  reviews: reviewReducer,
  recipes: recipeReducer,
  tags: tagReducer,
  cultures: cultureReducer,
});


let enhancer;

if (process.env.NODE_ENV === 'production') {
  enhancer = applyMiddleware(thunk);
} else {
  const logger = require('redux-logger').default;
  const composeEnhancers =
    window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
  enhancer = composeEnhancers(applyMiddleware(thunk, logger));
}

const configureStore = (preloadedState) => {
  return createStore(rootReducer, preloadedState, enhancer);
};

export default configureStore;
