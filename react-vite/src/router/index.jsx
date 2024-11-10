import { Route, createBrowserRouter, createRoutesFromElements } from 'react-router-dom';
import LoginFormPage from '../components/LoginFormPage';
import SignupFormPage from '../components/SignupFormPage';
import Layout from './Layout';
import Redirect from '../components/Redirect'
import MainPage from '../components/MainPage';
import SelectedRecipe from '../components/SelectedRecipe'
import CreateRecipe from '../components/CreateRecipe'
import EditRecipe from '../components/EditRecipe';
import UserRecipe from '../components/UserRecipe/UserRecipe';
import AboutMe from '../components/AboutMe';
import Contact from '../components/Contact';
import RecipeBox from '../components/RecipeBox';
import {CookedRecipes, SavedRecipes, RecentlyViewed} from '../components/RecipeBox';
import PopupHandler from '../components/PopupHandler';

export const router = createBrowserRouter(
  createRoutesFromElements(
    <Route element={<Layout />} >
      <Route path='/' element={<MainPage />} />
      <Route path='/login' element={<LoginFormPage />} />
      <Route path='/about-me' element={<AboutMe />} />
      <Route path='/contact-me' element={<Contact />} />
      <Route path='/signup' element={<SignupFormPage />} />
      <Route path='/new-recipe' element={<CreateRecipe />} />
      <Route path='/recipes/:recipeId' element={<SelectedRecipe />} />
      <Route path='/recipes/:recipeId/edit' element={<EditRecipe />} />
      <Route path='/:userId/recipes' element={<UserRecipe />} />
      <Route path='/recipe-box' element={<RecipeBox />}>
        <Route path='' element={<SavedRecipes />} />
        <Route path='all' element={<SavedRecipes />} />
        <Route path='cooked-recipes' element={<CookedRecipes />} />
        <Route path='recently-viewed' element={<RecentlyViewed />} />
      </Route>
      <Route path='/oauth-popup-handler' element={<PopupHandler />} />
      <Route path='*' element={<Redirect />} />
    </Route>
  )
)
