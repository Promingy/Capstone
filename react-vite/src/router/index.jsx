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

export const router = createBrowserRouter(
  createRoutesFromElements(
    <Route element={<Layout />} >
      <Route path='/' element={<MainPage />} />
      <Route path='/login' element={<LoginFormPage />} />
      <Route path='/signup' element={<SignupFormPage />} />
      <Route path='/new-recipe' element={<CreateRecipe />} />
      <Route path='/recipes/:recipeId' element={<SelectedRecipe />} />
      <Route path='/recipes/:recipeId/edit' element={<EditRecipe />} />
      <Route path='/:userId/recipes' element={<UserRecipe />} />
      <Route path='*' element={<Redirect />} />
    </Route>
  )
)
